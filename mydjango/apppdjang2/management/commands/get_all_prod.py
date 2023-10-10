from django.core.management.base import BaseCommand
from apppdjang2.models import Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        prod = Product.objects.all()
        self.stdout.write(f'{prod}')