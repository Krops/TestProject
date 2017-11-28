from django.test import TestCase
from django.test.client import Client
from prod.models import User, Comment
from .models import Product


class ProductPageTests(TestCase):
    def test_add_comment(self):
        """
        Check adding comment without authorization
        """
        c = Client()
        user = User.objects.create_user('krop', 'lennon@thebeatles.com', 'mypassword')
        Product(name='iPhone X', description='olo', slug='iphonex', price=1000, rate=5).save()
        c.post(path="/product/iphonex", data={'form_message': 'test message'})
        Comment(form_message="test message", product=Product.objects.get(slug='iphonex'), user=user, rate=0).save()
        assert 'test message' == str(Comment.objects.first().form_message)

    def test_add_comment_auth(self):
        """
        Check adding comment with authorization
        """
        c = Client()
        user = User.objects.create_user('krop', 'lennon@thebeatles.com', 'mypassword')
        Product(name='iPhone X', description='olo', slug='iphonex', price=1000, rate=5).save()
        c.login(username='krop', password='mypassword')
        c.post(path="/product/iphonex", data={'form_message': 'test message'})
        Comment(form_message="test message", product=Product.objects.get(slug='iphonex'), user=user, rate=0).save()
        assert 'test message' == str(Comment.objects.first().form_message)

    def test_vote_with_auth(self):
        """
        Check vote if authorized
        """
        c = Client()
        User.objects.create_user('krop', 'lennon@thebeatles.com', '555manda')
        c.login(username='krop', password='555manda')
        Product(name='iPhone X', description='olo', slug='iphonex', price=1000).save()
        response = c.get('/product/iphonex/vote', follow=True)
        assert response.status_code == 200
        assert response.json()['liked']
        assert response.json()['rate'] == 1
        response = c.get('/product/iphonex/vote', follow=True)
        assert not response.json()['liked']
        assert response.json()['rate'] == 0
        response = c.get('/product/iphonex/vote', follow=True)
        assert response.json()['liked']
        assert response.json()['rate'] == 1

    def test_vote_without(self):
        """
        Check vote if not authorized
        """
        c = Client()
        Product(name='iPhone X', description='olo', slug='iphonex', price=1000).save()
        response = c.get('/product/iphonex/vote', follow=True)
        assert response.status_code == 200
        assert 'Please sign in with one' in response.content.__str__()

    def test_without_product(self):
        """
        Check page after deleting the product
        """
        c = Client()
        product = Product(name='iPhone X', description='olo', slug='iphonex', price=1000)
        product.save()
        response = c.get('/product/iphonex', follow=True)
        assert response.status_code == 200
        product.delete()
        response = c.get('/product/iphonex', follow=True)
        assert response.status_code == 404
