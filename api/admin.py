from django.contrib import admin
from .models import Company
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    name = 'company'
    verbose_name = 'Compañía'
    list_display = ('name', 'website', 'foundation')


admin.site.register(Company, CompanyAdmin)
