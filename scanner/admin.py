from django.contrib import admin
from rango.models import UserProfile  #FOR USER PROFİLES
from scanner.models import LifestylePage, FoodAndDrinkPage,NightlifePage,Culture

#name,price range,culture and post code are the briefly enough to see on database I guess we dont need any other details for each page.!
class CultureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class FoodandDrinkAdmin(admin.ModelAdmin):
    list_display = ('culture','name','price_range', 'post_code')
class NightLifeAdmin(admin.ModelAdmin):
    list_display = ('culture','name', 'price_range', 'post_code')
class LifeStyleAdmin(admin.ModelAdmin):
    list_display = ('culture','name', 'price_range', 'post_code')

admin.site.register(Culture,CultureAdmin)
admin.site.register(FoodAndDrinkPage, FoodandDrinkAdmin)
admin.site.register(NightlifePage,NightLifeAdmin)
admin.site.register(LifestylePage,LifeStyleAdmin)

#admin.site.register(UserProfile) we need this as well in the models.py