import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                                   'CityScanner.settings')

import django
django.setup()
from scanner.models import Culture, FoodAndDrinkPage,LifestylePage,NightlifePage





def add_NightLifePage(cul, name, price_range,post_code):
    p = Page.objects.get_or_create(category=cul, title=name)[0]
    p.price_range = price_range
    p.post_code = post_code
    p.save()
    return p

def add_cul(name):
    c = Culture.objects.get_or_create(name=name)[0]
    c.save()
    return c
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()