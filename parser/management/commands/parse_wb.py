import requests, time
from decimal import Decimal
from django.core.management.base import BaseCommand
from products.models import Product

API_URL   = "https://search.wb.ru/exactmatch/ru/common/v4/search"
HEADERS   = {"User-Agent": "Mozilla/5.0"}
BASE_P    = {"dest": "-1257786", "curr": "rub", "resultset": "catalog", "appType": 1}

class Command(BaseCommand):
    help = "Парсит Wildberries по запросу или категории"

    def add_arguments(self, parser):
        parser.add_argument("query", type=str, help="Поисковый запрос/категория")
        parser.add_argument("--all", action="store_true", help="Парсить до конца")

    def handle(self, *a, **o):
        q, page, total = o["query"], 1, 0
        while True:
            params = {**BASE_P, "query": q, "page": page}
            r = requests.get(API_URL, params=params, headers=HEADERS, timeout=10)
            try:
                r.raise_for_status()
                items = r.json()["data"]["products"]
            except Exception as exc:
                self.stderr.write(f"[page {page}] error → {exc}")
                break

            if not items:
                break

            for p in items:
                total += 1
                Product.objects.update_or_create(
                    wb_id=p["id"],
                    defaults={
                        "title": p["name"],
                        "price":          Decimal(p["priceU"])      / 100,
                        "discounted_price": Decimal(p.get("salePriceU", p["priceU"])) / 100,
                        "rating":       p.get("reviewRating", 0),
                        "review_count": p.get("feedbacks", 0),
                    },
                )
            self.stdout.write(f"Страница {page}: сохранено {len(items)} товаров")
            page += 1
            if not o["all"]:
                break
            time.sleep(0.4)
        self.stdout.write(self.style.SUCCESS(f"Итого добавлено/обновлено: {total}"))
