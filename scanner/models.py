from django.db import models

class Culture(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class FoodAndDrinkPage(models.Model):

    culture = models.ForeignKey(Culture)
    name = models.CharField(max_length=128)
    url = models.URLField()
    short_desc = models.CharField(max_length=200)
    vegan_option = models.BooleanField()
    price_range = models.IntegerField(min_value=0, max_value=100)

    ## Assuming google maps api can take in this format
    street_num = models.IntegerField(min_value=0,max_value=999)
    post_code = models.StringField(max_length=6)

    ## Assumes restaurants will be open for only one block period per day
    mon_open = models.IntegerField(min_value=0, max_value=2400)
    tues_open = models.IntegerField(min_value=0, max_value=2400)
    wed_open = models.IntegerField(min_value=0, max_value=2400)
    thur_open = models.IntegerField(min_value=0, max_value=2400)
    fri_open = models.IntegerField(min_value=0, max_value=2400)
    sat_open = models.IntegerField(min_value=0, max_value=2400)
    sun_open = models.IntegerField(min_value=0, max_value=2400)

class NightlifePage(models.Model):

    culture = models.ForeignKey(Culture)
    name = models.CharField(max_length=128)
    url = models.URLField()
    short_desc = models.CharField(max_length=200)
    price_range = models.IntegerField(min_value=0,max_value=100)
    liscenced = models.BooleanField()

    ## Assuming google maps api can take in this format
    street_num = models.IntegerField(min_value=0,max_value=999)
    post_code = models.StringField(max_length=6)


class LifestylePage(models.Model):

    culture = models.ForeignKey(Culture)
    name = models.CharField(max_length=128)
    business = models.CharField(max_length=50)
    url = models.URLField()
    short_desc = models.CharField(max_length=200)
    price_range = models.IntegerField(min_value=0,max_value=100)

    ## Assuming google maps api can take in this format
    street_num = models.IntegerField(min_value=0,max_value=999)
    post_code = models.StringField(max_length=6)

    ## Assumes restaurants will be open for only one block period per day
    mon_open = models.IntegerField(min_value=0, max_value=2400)
    tues_open = models.IntegerField(min_value=0, max_value=2400)
    wed_open = models.IntegerField(min_value=0, max_value=2400)
    thur_open = models.IntegerField(min_value=0, max_value=2400)
    fri_open = models.IntegerField(min_value=0, max_value=2400)
    sat_open = models.IntegerField(min_value=0, max_value=2400)
    sun_open = models.IntegerField(min_value=0, max_value=2400)
