# products/tests/test_parser.py
import pytest
from decimal import Decimal
from django.core.management import call_command
from products.models import Product



fake_json = {
    "data": {
        "products": [
            {
                "id": 111,
                "name": "Тестовый товар",
                "priceU": 15000,          # 150.00 ₽
                "salePriceU": 9900,       # 99.00 ₽
                "reviewRating": 4.8,
                "feedbacks": 321,
            }
        ]
    }
}


class MockResp:
    """Мини-объект, имитирующий response от requests."""
    def __init__(self, data):
        self._data = data

    def raise_for_status(self):
        return True

    def json(self):
        return self._data


@pytest.mark.django_db
def test_parse_wb_command_creates_product(monkeypatch):
    """
    Команда parse_wb должна создать хотя бы одну запись Product.
    Запросы к реальному сайту не выполняются – подменяем их monkeypatch-ем.
    """
    import requests

    monkeypatch.setattr(requests, "get", lambda *a, **kw: MockResp(fake_json))

    call_command("parse_wb", "тест")

    p = Product.objects.get(wb_id=111)
    assert p.title == "Тестовый товар"
    assert p.price == Decimal("150.00")
    assert p.discounted_price == Decimal("99.00")
    assert p.rating == pytest.approx(4.8)
    assert p.review_count == 321
