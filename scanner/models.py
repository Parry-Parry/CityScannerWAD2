from django.db import models
from django.template.defaultfilters import slugify #ædded for slugs(not comitted yet)


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
