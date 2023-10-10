from django.core.management.base import BaseCommand
from apppdjang2.models import Product

class Command(BaseCommand):
    help = "Create product"

    def handle(self, *args, **kwargs):
        prod = Product (name_product= 'Соус', desctiption='состав:', price='45.99', quantity_product='50', date_upload='2022-12-30')
        prod.save()
        self.stdout.write(f'{prod}')