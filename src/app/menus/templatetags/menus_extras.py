from django import template

from app.menus.models import Menu, MenuSection

register = template.Library()


@register.filter
def hash(h, key):
    return h[key]


@register.filter
def to_list(obj):
    return list(obj)


@register.inclusion_tag('menus/menu_single.html', takes_context=True)
def draw_menu(context, url_name):

    def populate_tree(
            menu: Menu,
            node: MenuSection,
            mapping_dict: dict,
    ) -> None:
        for section in sections:
            if section.parent_id == node.id:
                section_dict = {
                    section: {
                        'is_opened': menu.is_opened,
                        'children': []
                    }
                }
                if section.url_slug == active_section_url_slug:
                    menu.is_opened = False
                mapping_dict[node]['children'].append(section_dict)
                populate_tree(menu, section, section_dict)

    menu = Menu.objects.get(url_name=url_name)
    sections = menu.sections.all()
    sections_mapping = dict()

    active_section_url_slug = context.get('active_section_url_slug')
    menu.is_opened = active_section_url_slug is not None

    for section in sections:
        if section.parent_id is None:
            sections_mapping[section] = {
                'is_opened': menu.is_opened,
                'children': []
            }
            if section.url_slug == active_section_url_slug:
                menu.is_opened = False
            populate_tree(menu, section, sections_mapping)

    data = {
        'menu': menu,
        'sections_mapping': sections_mapping,
        'active_section_url_slug': active_section_url_slug
    }

    return data

