import json
import urllib2

from products.models import Production
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    args = ''
    help = 'Creating the list of products in local database'

    def handle(self, *args, **options):
        # This will actually read the https, which we need to use
        products_url = r"http://www.unisport.dk/api/sample/"
        database_site = urllib2.urlopen(products_url).read().decode("utf-8")
        # This will encode python objects from the json and save data
        database_list = json.loads(database_site)['latest']
        for product in database_list:
            Production(name=product['name'],
                       sizes=product['sizes'],
                       price=''.join(product['price'].split("."))[:-3],
                       price_old=''.join(product['price_old'].split("."))[:-3],
                       production_id=product['id'],
                       delivery=product['delivery'],
                       kids=(True if product['kids'] == '1' else False),
                       kid_adult=(True if product['kid_adult'] == '1' else False),
                       free_porto=(True if product['free_porto'] == 'True' else False),
                       package=(True if product['package'] == '1' else False),
                       women=(True if product['women'] == '1' else False),
                       url=product['url'],
                       img_url=product['img_url']).save()
        self.stdout.write('Successfully created objects')