from django.contrib import admin
from friends_mapping.models import friend, location


class locations_inline(admin.TabularInline):
    model = location
    extra = 3
    ordering = ['-departure_date']

class friend_admin(admin.ModelAdmin):
    fieldsets = [
        ('Name: ',           {'fields': ['name']}),
        ('Dif. information', {'fields': ['age', 'sex', 'meeting_date'], 'classes': ['collapse']}),
    ]
    inlines = [locations_inline]
    list_display = ('name', 'meeting_date')
    search_fields = ['name']
    ordering = ['-meeting_date']


admin.site.register(friend, friend_admin)
admin.site.register(location)
