from django.core.management.base import BaseCommand
from apppdjang2.models import Customer


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        cust = Customer.objects.all()
        self.stdout.write(f'{cust}')