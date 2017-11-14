from django.views.generic import ListView
from prod.models import Product, Comment, Vote
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormMixin
from prod.forms import CommentForm
from prod.utils import render_to_json_response, convert_context_to_json
from prod.models import User
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseForbidden
from django import forms


class IndexView(ListView):
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
        products = get_object_or_404(Product, slug__iexact=self.kwargs['slug'])
        context['comments'] = Comment.objects.all().filter(product=products)
        context['slug'] = self.kwargs['slug']
        try:
            context['liked'] = get_object_or_404(Vote, author_id=self.request.user.id, product_id=products).rate
        except Http404:
            context['liked'] = False
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        print(form.errors)
        if form.is_valid():
            print("___helo")
            return self.form_valid(form)
        else:
            print("___helos")
            print(form.cleaned_data)
            return self.form_invalid(form)

    def form_valid(self, form):
        form = form.cleaned_data
        print(form)
        Comment(user=User.objects.get(name='dron'), product=Product.objects.get(slug=self.object.slug),
                message=form.get('message')).save()
        return super(ProductView, self).form_valid(form)

    def form_invalid(self, form):
        return super(ProductView, self).form_invalid(form)


def vote(request, slug):
    p = get_object_or_404(Product, slug__iexact=slug)
    product_id = Product.objects.get(slug=slug).pk
    context = {}
    try:
        if request.user.is_authenticated():
            try:
                v = get_object_or_404(Vote, author_id=request.user.id, product_id=product_id)
                v.rate = not v.rate
                if v.rate:
                    p.rate -= 1
                else:
                    p.rate += 1
                v.save()
                p.save()
            except Http404:
                v = Vote(rate=True, product_id=product_id, author_id=request.user.id)
                p.rate += 1
                v.save()
                p.save()
            finally:
                context['rate'] = p.rate
            return render_to_json_response(context, status=200)
        else:
            context = {'errors': "User is not authenticated"}
            return render_to_json_response(context, status=200)

    except (KeyError, Product.DoesNotExist):
        context = {'errors': "User is not authenticated"}
        return render_to_json_response(context, status=200)
