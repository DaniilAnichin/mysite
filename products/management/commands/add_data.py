import json
import os

from products.models import production
#import pysqlite2
#conn = pysqlite2.connect('C:/Python27/mysite/db.sqlite3')
from django.core.management.base import BaseCommand, CommandError


try:
    # for python 2.*
    import urllib2
except:
    # for python 3.*
    import urllib.request

class Command(BaseCommand):
    args = ''
    help = 'Creating the list of products in local database'

    def handle(self, *args, **options):
        # This will actualy read the https, which we need to use
        products_url = r"http://www.unisport.dk/api/sample/"
        try:
            database_site = urllib2.urlopen(products_url).read().decode("utf-8")
        except:
            database_site = urllib.request.urlopen(products_url).read().decode("utf-8")
        # This will encode python objects from the json and delete duplicates
        database_list = json.loads(database_site)['latest']
        for product in database_list:
            production(name=product['name'],
                       sizes=product['sizes'],
                       price=''.join(product['price'].split("."))[:-3],
                       price_old=''.join(product['price_old'].split("."))[:-3],
                       id=product['id'],
                       delivery=product['delivery'],
                       kids=(True if product['kids'] == '1' else False),
                       kid_adult=(True if product['kid_adult'] == '1' else False),
                       free_porto=(True if product['free_porto'] == 'True' else False),
                       package=(True if product['package'] == '1' else False),
                       women=(True if product['women'] == '1' else False),
                       url=product['url'],
                       img_url=product['img_url']).save()
        """dest_dir = r'c:\python27\database_viev'
        if not os.access(dest_dir, os.F_OK):
            os.makedirs(dest_dir)
        database_file = open(dest_dir + r'\data.txt', 'w')
        database_file.write(str(database_dict))
        database_file.close()"""
        self.stdout.write('Successfully created objects')
