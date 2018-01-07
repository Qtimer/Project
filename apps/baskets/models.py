from django.db import models

from apps.accounts.models import Account
from apps.products.models import Product


class Basket(models.Model):
    owner = models.ForeignKey(Account, verbose_name="Owner")
    product = models.ForeignKey(Product, verbose_name="Product")
    in_basket = models.BooleanField(verbose_name="Status", default=True)

    def __str__(self):
        return "Basket: " + self.product.name
