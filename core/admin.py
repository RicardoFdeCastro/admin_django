from django.contrib import admin
from .models import categoria, product


@admin.register(product)
@admin.register(categoria)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
