from django.db import models

class Product(models.Model):
    wb_id           = models.BigIntegerField(unique=True)
    title           = models.CharField(max_length=255)
    price           = models.DecimalField(max_digits=12, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=12, decimal_places=2)
    rating          = models.FloatField(null=True, blank=True)
    review_count    = models.PositiveIntegerField()

    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title