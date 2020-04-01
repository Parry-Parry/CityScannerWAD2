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
        super(Culture, self).save(*args, **kwargs)




    def __str__(self):
        return self.name

class FoodAndDrinkPage(models.Model):
    type='foodanddrink'
    NAME_MAX_LENGTH =128
    SHORT_DESC_MAX_LENGTH =200
    TIME_MAX=2400
    STREET_NUM_MAX_LENGTH =999
    POSTCODE_MAX_LENGTH =6
    culture = models.ForeignKey(Culture, on_delete =models.CASCADE)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    url = models.URLField()
    short_desc = models.CharField(max_length=SHORT_DESC_MAX_LENGTH)
    vegan_option = models.BooleanField()
    price_range = models.IntegerField()

    ## Assuming google maps api can take in this format
    street_num = models.IntegerField()
    post_code = models.CharField(max_length=POSTCODE_MAX_LENGTH)



class NightlifePage(models.Model):
    type='nightlife'
    NAME_MAX_LENGTH =128
    SHORT_DESC_MAX_LENGTH =200
    TIME_MAX=2400
    STREET_NUM_MAX_LENGTH =999
    POSTCODE_MAX_LENGTH =6
    culture = models.ForeignKey(Culture, on_delete =models.CASCADE)
    name = models.CharField(max_length=128)
    url = models.URLField()
    short_desc = models.CharField(max_length=200)
    price_range = models.IntegerField()
    liscenced = models.BooleanField()

    ## Assuming google maps api can take in this format
    street_num = models.IntegerField()
    post_code = models.CharField(max_length=6)




class LifestylePage(models.Model):
    type='lifestyle'
    NAME_MAX_LENGTH =128
    SHORT_DESC_MAX_LENGTH =200
    TIME_MAX=2400
    STREET_NUM_MAX_LENGTH =999
    POSTCODE_MAX_LENGTH =6

    culture = models.ForeignKey(Culture, on_delete= models.CASCADE)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    business = models.CharField(max_length=50)
    url = models.URLField()
    short_desc = models.CharField(max_length=SHORT_DESC_MAX_LENGTH)
    price_range = models.IntegerField()

    ## Assuming google maps api can take in this format
    street_num = models.IntegerField()
    post_code = models.CharField(max_length=POSTCODE_MAX_LENGTH)
