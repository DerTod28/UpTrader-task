from django.shortcuts import render

from app.menus.models import Menu, MenuSection


def menu_list(request):
    menus = Menu.objects.all()
    context = {'menus': [menu.url_name for menu in menus]}
    return render(request, "menus/main.html", context)


def menu_detail(request, global_menu_url_name):
    context = {'menus': [global_menu_url_name, ]}
    return render(request, "menus/main.html", context)


def menu_section_detail(request, global_menu_url_name, section_url_slug):
    context = {'menus': [global_menu_url_name, ], 'active_section_url_slug': section_url_slug}
    return render(request, "menus/main.html", context)
