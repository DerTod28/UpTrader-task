from django.db import models


class Menu(models.Model):
    url_name = models.CharField(max_length=30, null=False, unique=True)
    verbose_name = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.verbose_name


class MenuSection(models.Model):
    verbose_name = models.CharField(max_length=100)
    global_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='sections')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    url_slug = models.SlugField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.verbose_name
