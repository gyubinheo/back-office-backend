# tests/test_views.py
import pytest
from rest_framework.test import APIClient
from shop.models import Product, Tag, ProductOption


@pytest.fixture
def create_tags():
    tag1 = Tag.objects.create(name='ExistTag')

    return tag1


@pytest.fixture
def create_product():
    product = Product.objects.create(name='TestProduct')
    option1 = ProductOption.objects.create(product=product, name='TestOption1', price=1000)
    option2 = ProductOption.objects.create(product=product, name='TestOption2', price=500)
    option3 = ProductOption.objects.create(product=product, name='TestOption3', price=0)
    product.option_set.add(option1, option2, option3)
    tag1 = Tag.objects.create(name='ExistTag')
    tag2 = Tag.objects.create(name='NewTag')
    product.tag_set.add(tag1, tag2)

    return product


@pytest.mark.django_db
def test_create_product(create_tags):
    client = APIClient()

    url = "/shop/products/"
    data = {
        "name": "TestProduct",
        "option_set": [
            {
                "name": "TestOption1",
                "price": 1000
            },
            {
                "name": "TestOption2",
                "price": 500
            },
            {
                "name": "TestOption3",
                "price": 0
            }
        ],
        "tag_set": [
            {
                "pk": create_tags.pk,
                "name": "ExistTag"
            },
            {
                "name": "NewTag"
            }
        ]
    }

    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data['name'] == 'TestProduct'
    assert len(response.data['option_set']) == 3
    assert len(response.data['tag_set']) == 2


@pytest.mark.django_db
def test_update_product(create_product):
    client = APIClient()

    url = "/shop/products/1/"
    data = {
        "pk": 1,
        "name": "TestProduct",
        "option_set": [
            {
                "pk": 1,
                "name": "TestOption1",
                "price": 1000
            },
            {
                "pk": 2,
                "name": "Edit TestOption2",
                "price": 1500
            },
            {
                "name": "Edit New Option",
                "price": 300
            }
        ],
        "tag_set": [
            {
                "pk": 1,
                "name": "ExistTag"
            },
            {
                "pk": 2,
                "name": "NewTag"
            },
            {
                "name": "Edit New Tag"
            }
        ]
    }

    response = client.patch(url, data, format='json')

    assert response.status_code == 200
    assert response.data['name'] == 'TestProduct'
    assert len(response.data['option_set']) == 3
    assert len(response.data['tag_set']) == 3


@pytest.mark.django_db
def test_retrieve_product(create_product):
    client = APIClient()

    url = "/shop/products/1/"
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['pk'] == create_product.pk
    assert response.data['name'] == create_product.name
    assert len(response.data['option_set']) == 3
    assert len(response.data['tag_set']) == 2


@pytest.mark.django_db
def test_delete_product(create_product):
    client = APIClient()

    url = "/shop/products/1/"
    response = client.delete(url)

    assert response.status_code == 204
    assert Product.objects.count() == 0
