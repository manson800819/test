from django.contrib import admin

from .models import Category, Product,Type1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class Type1Admin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Type1, Type1Admin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock',
                    'available', 'created', 'updated','description']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available',"description"]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.site_header = "NCFU Admin"
admin.site.site_title = "NCFU Admin Portal"
admin.site.index_title = "Welcome to NCFU  Portal"
