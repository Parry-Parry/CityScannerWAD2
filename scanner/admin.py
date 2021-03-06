from django.contrib import admin
from scanner.models import UserProfile
from scanner.models import LifestylePage, FoodAndDrinkPage,NightlifePage,Culture

#name,price range,culture and post code are the briefly enough to see on database I guess we dont need any other details for each page.!
class CultureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class FoodandDrinkAdmin(admin.ModelAdmin):
    list_display = ('culture','name','price_range', 'post_code','street_num', 'url', 'vegan_option', 'short_desc')
class NightLifeAdmin(admin.ModelAdmin):
    list_display = ('culture','name', 'price_range', 'post_code','street_num', 'url', 'short_desc', 'liscenced')
class LifeStyleAdmin(admin.ModelAdmin):
    list_display = ('culture','name', 'price_range', 'post_code','street_num','url', 'short_desc', 'business')

admin.site.register(Culture,CultureAdmin)
admin.site.register(FoodAndDrinkPage, FoodandDrinkAdmin)
admin.site.register(NightlifePage,NightLifeAdmin)
admin.site.register(LifestylePage,LifeStyleAdmin)
admin.site.register(UserProfile) #if we wish to include any other features we want to see about the users we can create UserProfileAdmin as well
                                #right now all we see is the usernames.
