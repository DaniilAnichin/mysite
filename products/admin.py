from django.contrib import admin

from products.models import production


class production_admin(admin.ModelAdmin):
    fieldsets = [
        ('Name: ',           {'fields': ['name']}),
        ('Sizes: ',          {'fields': ['sizes']}),
        ('Price: ',          {'fields': ['price']}),
        ('Delivery: ',       {'fields': ['delivery']}),
        ('ID: ',             {'fields': ['id']}),
        ('Dif. information', {'fields': ['package', 'price_old', 'free_porto',
                                         'kids', 'kid_adult', 'women'],
                              'classes': ['collapse']}),
        ('Links',            {'fields': ['img_url', 'url'],
                              'classes': ['collapse']}),
    ]
    list_display = ('name', 'price')
    search_fields = ['name', 'price', 'id']
    ordering = ['price']


admin.site.register(production, production_admin)
