from django.contrib import admin
from election.profile.models import UserProfile, UserCity, UserTown

def get_cities_and_towns():
   print('Dosya import edeceğim')

class UserCityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)

    def import_cities_and_towns(modeladmin, request, queryset):
        get_cities_and_towns()

    actions = [import_cities_and_towns,]
    import_cities_and_towns.short_description = 'İl ve İlçeleri Yükle'

class UserTownAdmin(admin.ModelAdmin):
    list_display = ('name', 'city',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_staff', 'is_superuser', 'created_at', 'is_active', 'town',)
    list_filter = ('town',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserCity, UserCityAdmin)
admin.site.register(UserTown, UserTownAdmin)