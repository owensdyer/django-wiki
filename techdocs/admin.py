from django.contrib import admin

from . import models


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ["parent", "name"]


class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ["parent", "name", "description"]


class TechnicalDocAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ["category", "title"]


admin.site.register(models.Supercategory)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Subcategory, SubcategoryAdmin)
admin.site.register(models.TechnicalDoc, TechnicalDocAdmin)
