import os
from csv import DictReader
from datetime import datetime
from django.core.management.base import BaseCommand
from sales.models import Sale
from sellers.models import Seller
from countries.models import Country


class Command(BaseCommand):
    help = 'Load data from CSV files into the database'

    def handle(self, *args, **kwargs):
        self.load_countries()
        self.load_sellers()
        self.load_sales()
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from CSV files'))

    def load_countries(self):
        with open(os.path.join('data', 'paises.csv'), encoding='latin1') as f:
            reader = DictReader(f)
            for row in reader:
                Country.objects.create(ISO2=row['ISO2'], name=row['Pais'])

    def load_sellers(self):
        with open(os.path.join('data', 'vendedores.csv'), encoding='latin1') as f:
            reader = DictReader(f, delimiter=';')
            for row in reader:
                Seller.objects.create(
                    seller_id=row['ID Vendedor'], language=row['Idioma'], team=row['Equipo']
                )

    def load_sales(self):
        with open(os.path.join('data', 'ventas.csv'), encoding='latin1') as f:
            reader = DictReader(f, delimiter=';')
            for row in reader:
                seller_ids = row['Operador'].split(',')
                date_str = row['Fecha de venta']
                date_obj = datetime.strptime(date_str, '%d/%m/%Y').date()
                region = row['Región']
                if len(region) > 2:
                    try:
                        country = Country.objects.get(name=region)
                        region = country.ISO2
                    except Country.DoesNotExist:
                        continue  # Skip this row

                sale = Sale.objects.create(
                    order_number=row['Número de Pedido'],
                    date=date_obj,
                    country=region,
                    income=row['Ingreso'],
                    type=row['Tipo de venta'],
                )
                for seller_id in seller_ids:
                    seller = Seller.objects.get(seller_id=seller_id)
                    sale.sellers.add(seller)
