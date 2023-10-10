from django.core.management.base import BaseCommand
from apppdjang2.models import Customer

class Command(BaseCommand):
    help = "Create USer"

    def handle(self, *args, **kwargs):
        #customer = Customer(name='Alex', email='alex221@shota.exe', phone='9627757689', address='soon',
         #                   date_registration='1999-06-05')
        customer = Customer(name='Igor', email='Igor221@shota.exe', phone='9627227689', address='soon',
                            date_registration='1999-02-09')
        customer.save()
        self.stdout.write(f'{customer}')