from django.contrib import admin
from election.models import Survey
from import_export import resources
from election.models import Survey
from election.models import Soru
from import_export.admin import ImportExportModelAdmin
from django.dispatch import receiver
from import_export.signals import post_import, post_export

class SurveyResource(resources.ModelResource):

    class Meta:
        model = Survey
        fields = ('name', 'active', 'created_at', 'updated_at')

class SurveyAdmin(ImportExportModelAdmin):
    resource_class = SurveyResource
    list_display = ('name', 'active', 'created_at', 'updated_at')
    list_filter = ('active',)
    search_fields = ('name',)

class SoruAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'soru', 'survey','unique_id','created_at')
    search_fields = ('unique_id',)

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Soru, SoruAdmin)