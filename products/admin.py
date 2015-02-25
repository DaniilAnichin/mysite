from django.contrib import admin

from products.models import Production


class ProductionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name: ',           {'fields': ['name']}),
        ('Sizes: ',          {'fields': ['sizes']}),
        ('Price: ',          {'fields': ['price']}),
        ('Delivery: ',       {'fields': ['delivery']}),
        ('ID: ',             {'fields': ['production_id']}),
        ('Dif. information', {'fields': ['package', 'price_old', 'free_porto',
                                         'kids', 'kid_adult', 'women'],
                              'classes': ['collapse']}),
        ('Links',            {'fields': ['img_url', 'url'],
                              'classes': ['collapse']}),
    ]
    list_display = ('name', 'price')
    search_fields = ['name', 'price', 'production_id']
    ordering = ['price']


admin.site.register(Production, ProductionAdmin)
