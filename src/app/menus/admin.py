from django.contrib import admin
from app.menus.models import Menu, MenuSection


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("verbose_name", "url_name", "created_at")
    model = Menu


@admin.register(MenuSection)
class MenuSectionsAdmin(admin.ModelAdmin):
    list_display = ("verbose_name", "parent_id", "created_at")
    list_filter = (
        "global_menu_id",
        "parent_id",
    )
    prepopulated_fields = {'url_slug': ('verbose_name', 'parent', 'global_menu')}

    model = MenuSection
