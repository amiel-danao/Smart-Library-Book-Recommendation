# smart_library/admin.py
from django.contrib import admin
from django.contrib.admin import AdminSite
from import_export.admin import ImportExportModelAdmin, ImportMixin
from .models import Book
from import_export import fields, widgets, resources



class SmartLibraryAdminSite(AdminSite):
    site_header = 'Smart Library Admin'
    site_title = 'Smart Library Admin'
    index_title = 'Welcome to Smart Library Admin'

admin_site = SmartLibraryAdminSite(name='smart_library_admin')

# class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('author', 'title', 'year', 'popularity', 'rating', 'course')
# admin_site.register(Book, BookAdmin)

class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        exclude = ('total_rating', 'rating_count')

    # Specify the widget for the CharField (assuming course is a CharField)
    widgets = {
        'course': {'widget': widgets.CharWidget()},
    }

    # Skip rows where all values are None (blank rows)
    skip_rows = lambda instance, original: all(value is None for value in instance.dict.values())

class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BookResource
    list_display = ('author', 'title', 'year', 'popularity', 'rating', 'course')
    readonly_fields = ('rating', )

admin_site.register(Book, BookAdmin)