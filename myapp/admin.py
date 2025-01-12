from django.contrib import admin
from .models import TodoItem, OGL, MineralTract

# Register your models here.
admin.site.register(TodoItem)

class MineralTractInline(admin.TabularInline):
    model = MineralTract
    extra = 1  # Number of empty forms for adding new tracts

@admin.register(OGL)
class OGLAdmin(admin.ModelAdmin):
    list_display = ('docNo', 'effDate', 'recDate', 'lessor', 'royalty', 'lessee', 'legal_desc', 'term_in_years', 'royalty')
    inlines = [MineralTractInline]

@admin.register(MineralTract)
class MineralTractAdmin(admin.ModelAdmin):
    list_display = ('township', 'range', 'section', 'gross', 'owner', 'percent', 'net', 'ogl')
