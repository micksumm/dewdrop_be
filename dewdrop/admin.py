# Register your models here.
from django.contrib import admin
from .models import Product, Condition


# Register your models here.
# @admin.register(models.Post)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('title', 'id', 'status', 'slug', 'author')
#     prepopulated_fields = { 'slug': ('title',), }

# admin.site.register(models.Category)
class ProductConditionInline(admin.TabularInline):
    model = Product.conditions.through
    extra = 1

class ConditionAdmin(admin.ModelAdmin):
    inlines = [ProductConditionInline]
    filter_horizontal = ('products',)

# class ConditionInline(admin.TabularInline):
#     model = Condition.products.through

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductConditionInline]
    exclude = ('conditions',)

admin.site.register(Condition, ConditionAdmin)
admin.site.register(Product, ProductAdmin)