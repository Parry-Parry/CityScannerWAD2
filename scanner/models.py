from django.db import models
from django.template.defaultfilters import slugify #ædded for slugs(not comitted yet)
from django.contrib.auth.models import User

class UserProfile(models.Model): # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username

class Culture(models.Model):
    name = models.CharField(max_length=128, unique=True)


    #the slug and save is needed for the admin.py.CultureAdmin thing needs these (not comitted these)
    slug = models.SlugField(unique=True) #unique sluq field (not committed yet)

     # save method added makes population easier in admin.py CultureAdmin class (not comitted I guess)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)




    def __str__(self):
        return self.name

class FoodAndDrinkPage(models.Model):
    NAME_MAX_LENGTH =128
    SHORT_DESC_MAX_LENGTH =200
    TIME_MAX=2400
    STREET_NUM_MAX_LENGTH =999
    POSTCODE_MAX_LENGTH =6
    culture = models.ForeignKey(Culture)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    url = models.URLField()
    short_desc = models.CharField(max_length=SHORT_DESC_MAX_LENGTH)
    vegan_option = models.BooleanField()
    price_range = models.IntegerField(min_value=0, max_value=100)

    ## Assuming google maps api can take in this format
    street_num = models.IntegerField(min_value=0,max_value=999)
    post_code = models.StringField(max_length=6)

    ## Assumes restaurants will be open for only one block period per day
    mon_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    tues_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    wed_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    thur_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    fri_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    sat_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    sun_open = models.IntegerField(min_value=0, max_value=TIME_MAX)

class NightlifePage(models.Model):
    NAME_MAX_LENGTH =128
    SHORT_DESC_MAX_LENGTH =200
    TIME_MAX=2400
    STREET_NUM_MAX_LENGTH =999
    POSTCODE_MAX_LENGTH =6
    culture = models.ForeignKey(Culture)
    name = models.CharField(max_length=128)
    url = models.URLField()
    short_desc = models.CharField(max_length=200)
    price_range = models.IntegerField(min_value=0,max_value=100)
    liscenced = models.BooleanField()

    ## Assuming google maps api can take in this format
    street_num = models.IntegerField(min_value=0,max_value=STREE)
    post_code = models.StringField(max_length=6)

    mon_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    tues_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    wed_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    thur_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    fri_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    sat_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    sun_open = models.IntegerField(min_value=0, max_value=TIME_MAX)



class LifestylePage(models.Model):
    NAME_MAX_LENGTH =128
    SHORT_DESC_MAX_LENGTH =200
    TIME_MAX=2400
    STREET_NUM_MAX_LENGTH =999
    POSTCODE_MAX_LENGTH =6

    culture = models.ForeignKey(Culture)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    business = models.CharField(max_length=50)
    url = models.URLField()
    short_desc = models.CharField(max_length=SHORT_DESC_MAX_LENGTH)
    price_range = models.IntegerField(min_value=0,max_value=100)

    ## Assuming google maps api can take in this format
    street_num = models.IntegerField(min_value=0,max_value=STREET_NUM_MAX_LENGTH)
    post_code = models.StringField(max_length=POSTCODE_MAX_LENGTH)

    ## Assumes restaurants will be open for only one block period per day
    mon_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    tues_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    wed_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    thur_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    fri_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    sat_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
    sun_open = models.IntegerField(min_value=0, max_value=TIME_MAX)
