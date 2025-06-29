import pytest
from django.urls import reverse
from products.models import Product

@pytest.mark.django_db
def test_min_price_filter(api_client):
    Product.objects.create(
        wb_id=1, title="Cheap", price=100, discounted_price=90, rating=2, review_count=10
    )
    Product.objects.create(
        wb_id=2, title="Expensive", price=6000, discounted_price=6000,
        rating=5, review_count=500
    )

    url = reverse("products")
    resp = api_client.get(url, {"min_price": 5000})
    assert resp.status_code == 200
    assert len(resp.data["results"]) == 1
    assert resp.data["results"][0]["title"] == "Expensive"
