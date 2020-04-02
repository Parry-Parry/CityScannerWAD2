import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CityScanner.settings')
import django
django.setup()
from scanner.models import Culture, NightlifePage,LifestylePage,FoodAndDrinkPage
def populate():
    cultures = [{'name': 'Greek'},
                {'name': 'Chinese'},
                {'name': 'Spanish'}]
    foodanddrink_pages = [{'culture': 'Spanish','name': 'Iberica Glasgow','url': 'https://www.ibericarestaurants.com/locations/glasgow', 'desc':'Located on the corner of St Vincent Street and Hope Street, Ibérica Glasgow is set within an historic building, this restaurant provides signature tapas.', 'vegan':True, 'price':60, 'street_num':140 ,'post_code':'G25LA'},
                        {'culture': 'Spanish','name': 'The Spanish Butcher','url': 'https://www.spanishbutcher.com', 'desc':'Located at 80 Miller Street, The Spanish Butcher serves the finest grades of Galician beef, the most premium Iberican Jamon and the freshest of seafood; combining Spanish and Mediterranean food', 'vegan':False, 'price':85, 'street_num':80 ,'post_code':'G11DT'},
                        {'culture': 'Greek','name': 'Halloumi Glasgow','url': 'http://www.halloumiglasgow.co.uk', 'desc':'A friendly atmosphere providing a greek take on tapas.', 'vegan':True, 'price':40, 'street_num':161 ,'post_code':'G22UQ'},
                        {'culture': 'Chinese','name': 'Lychee Oriental','url': 'https://lycheeoriental.co.uk', 'desc':'Winner of the “Best Chinese Restaurant in Scotland ” award, Lychee Oriental offers the very best in Oriental cuisine, cocktails & wines', 'vegan':False, 'price':50, 'street_num':59 ,'post_code':'G13LN'}]

    nightlife_pages = [{'culture': 'Spanish','name': 'Mango Tropical','url': 'https://www.mangolatino.co.uk', 'desc':'Two floors of Latin music, dancing and drinking.', 'business':'Bar','liscenced':True, 'price':45, 'street_num':373 ,'post_code':'G23HU'}]

    lifestyle_pages = [{'culture': 'Greek','name': 'Greek Orthodox Cathedral of St. Luke','url': 'http://www.greekcommunitystluke.scot/home', 'desc':'Greek orthodox church in Glasgow.', 'business':'Church', 'price':0, 'street_num':27 ,'post_code':'G129LL'},
                    {'culture': 'Greek','name': 'Style City','url': 'https://www.stylecitybarber.co.uk', 'desc':'Greek/Turkish barber shop.', 'business':'Barbers', 'price':10, 'street_num':1148 ,'post_code':'G38TE'},
                    {'culture': 'Chinese','name': 'Lims','url':'n/a', 'desc':'Chinese Supermarket in Glasgow city center', 'business':'Supermarket', 'price':50, 'street_num':63 ,'post_code':'G36QX'}]

    for culture in cultures:
        c = add_culture(culture['name'])
    for fadp in foodanddrink_pages:
        add_foodanddrink_page(Culture.objects.get(name=fadp['culture']), fadp['name'], fadp['url'], fadp['desc'], fadp['vegan'], fadp['price'], fadp['street_num'], fadp['post_code'])
    for np in nightlife_pages:
        add_nightlife_page(Culture.objects.get(name=np['culture']), np['name'], np['business'], np['url'], np['desc'], np['liscenced'], np['price'], np['street_num'], np['post_code'])
    for lp in lifestyle_pages:
        add_lifestyle_page(Culture.objects.get(name=lp['culture']),lp['name'],lp['business'], lp['url'], lp['desc'], lp['price'], lp['street_num'], lp['post_code'])


def add_foodanddrink_page(culture, name, url, desc, vegan, price, street_num, post_code):
    fadp = FoodAndDrinkPage.objects.get_or_create(name=name)[0]
    fadp.culture=culture
    fadp.short_desc=desc
    fadp.vegan_option=vegan
    fadp.price_range=price
    fadp.street_num=street_num
    fadp.post_code=post_code
    if url!='n/a':
        fadp.url=url
    fadp.save()
    return fadp

def add_nightlife_page(culture, name, business, url, desc, liscenced, price, street_num, post_code):
    np =  NightlifePage.objects.get_or_create(name=name)[0]
    np.culture=culture
    np.business=business
    np.short_desc=desc
    np.liscenced=liscenced
    np.price_range=price
    np.street_num=street_num
    np.post_code=post_code
    if url!='n/a':
        np.url=url
    np.save()
    return np

def add_lifestyle_page(culture, name, business, url, desc, price, street_num, post_code):
    lp =  LifestylePage.objects.get_or_create(name=name)[0]
    lp.culture=culture
    lp.business=business
    lp.short_desc=desc
    lp.price_range=price
    lp.street_num=street_num
    lp.post_code=post_code
    if url!='n/a':
        lp.url=url
    lp.save()
    return lp

def add_culture(name):
    c=Culture.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Scanner Population...")
    populate()
    print("Population Complete!")
