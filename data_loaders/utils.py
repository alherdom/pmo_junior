from csv import DictReader
from sales.models import Sale
from sellers.models import Seller
from countries.models import Country

def load_countries():
    with open('data/paises.csv') as f:
        reader = DictReader(f)
        for row in reader:
            country = Country(ISO2=row['ISO2'], name=row['País'])
            country.save()

def load_sellers():
    with open('data/vendedores.csv') as f:
        reader = DictReader(f)
        for row in reader:
            seller = Seller(seller_id=row['ID'], language=row['Idioma'], team=row['Equipo'])
            seller.save()

def load_sales():
    with open('data/ventas.csv') as f:
        reader = DictReader(f)
        for row in reader:
            seller = Seller.objects.get(seller_id=row['seller_id'])
            sale = Sale(order_number=row['Número'], date=row['Fecha de venta'], country=row['Región'], income=row['Ingreso'], type=row['Tipo de venta'], seller=seller)
            sale.save()

