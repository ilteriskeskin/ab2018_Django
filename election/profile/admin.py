from django.contrib import admin
from election.profile.models import UserProfile, UserCity, UserTown
import openpyxl
from openpyxl.utils.cell import col
from django.http import *
from django.core.exceptions import ObjectDoesNotExist

def get_cities_and_towns():

    print("Dosya import edeceğim")
    path = '/home/ilteriskeskin/İndirilenler/sehirler.xlsx'
    wb = openpyxl.load_workbook(path, data_only=True)
    sheet = wb.active

    for row in sheet.iter_rows(row_offset=1):
        code = str(row[0].value).strip()
        city_name = str(row[1].value).strip()
        town_name = str(row[2].value).strip()

        try:
            city = UserCity.objects.get(code=code)
            town = UserTown(name=town_name, city = city)
            town.save()

        except ObjectDoesNotExist:
            city = UserCity(name=city_name, code=code)
            city.save()
            town = UserTown(name=town_name, city=city)
            town.save()


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

    def city_name(self, obj):
        return obj.town.city.name

    def get_queryset(self, request):
        town = request.user.town
        users = UserProfile.objects.filter(town=town)
        return users

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserCity, UserCityAdmin)
admin.site.register(UserTown, UserTownAdmin)