from django.contrib import admin
from .models import Data, FacultyData, PercentageData
# Register your models here.

# admin.site.register(Data)
admin.site.register(FacultyData)
admin.site.register(PercentageData)
# admin.site.register(AnotherData)


@admin.register(Data)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'program', 'percentage']