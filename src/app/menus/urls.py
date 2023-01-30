from django.urls import path

import app.menus.views as views

app_name = 'menus'
urlpatterns = [
    path('main/', views.menu_list, name='main'),
    path('<str:global_menu_url_name>/', views.menu_detail, name='menu_detail'),
    path('<str:global_menu_url_name>/<str:section_url_slug>/', views.menu_section_detail, name='section_menu_detail'),
]
