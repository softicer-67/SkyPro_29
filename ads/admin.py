from django.contrib import admin
from .models import Category, Ad, User, Location, Selection
from .custom_filter import DuplicatSlugFilter


# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = (DuplicatSlugFilter,)


admin.site.register(Category, CategoryAdmin)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'price', 'image']
    search_fields = ['name', 'price']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role', 'age', 'email']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']


# @admin.register(Selection)
# class SelectionAdmin(admin.ModelAdmin):
#     list_display = ['name', 'items', 'owner']


admin.site.register(Selection)
