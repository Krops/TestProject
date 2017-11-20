from django.views.generic import ListView
from prod.models import Product, Comment, Vote
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormMixin
from prod.forms import CommentForm
from prod.utils import render_to_json_response
from prod.models import User
from django.shortcuts import redirect, reverse
from django.http import Http404
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def index(request):
    return redirect('products')


class ProductsView(ListView):
    template_name = 'prod/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()


class ProductView(DetailView, FormMixin):
    template_name = 'prod/product.html'
    form_class = CommentForm
    model = Product
    success_url = 'product'

    def get_success_url(self):
        return reverse('product', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        product = get_object_or_404(Product, slug__iexact=self.kwargs['slug'])
        time_threshold = timezone.now() - timezone.timedelta(hours=24)
        context['comments'] = Comment.objects.all().filter(
            product=product, time_edit__gt=time_threshold)
        context['slug'] = self.kwargs['slug']
        try:
            context['liked'] = get_object_or_404(
                Vote, author_id=self.request.user.id, product_id=product).rate
        except Http404:
            context['liked'] = False
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form = form.cleaned_data
        user = 'krop'
        if self.request.user.is_authenticated:
            user = self.request.user
        Comment(
            user=User.objects.get(
                username=user),
            product=Product.objects.get(
                slug=self.object.slug),
            message=form.get('message')).save()
        return super(ProductView, self).form_valid(form)

    def form_invalid(self, form):
        return super(ProductView, self).form_invalid(form)


@login_required
def vote(request, slug):
    p = get_object_or_404(Product, slug__iexact=slug)
    v = False
    product_id = Product.objects.get(slug=slug).pk
    context = {}
    try:
        v = get_object_or_404(
            Vote,
            author_id=request.user.id,
            product_id=product_id)
        if v.rate:
            p.rate -= 1
        else:
            p.rate += 1
        v.rate = not v.rate
        v.save()
        p.save()
    except Http404:
        v = Vote(rate=True, product_id=product_id, author_id=request.user.id)
        p.rate += 1
        v.save()
        p.save()
    finally:
        context['rate'] = p.rate
        context['liked'] = v.rate
    return render_to_json_response(context, status=200)
