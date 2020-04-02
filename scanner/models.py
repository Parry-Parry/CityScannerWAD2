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
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Culture, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class FoodAndDrinkPage(models.Model):

    NAME_MAX_LENGTH =128
    SHORT_DESC_MAX_LENGTH =200
    TIME_MAX=2400
    STREET_NUM_MAX_LENGTH =9999
    POSTCODE_MAX_LENGTH =6
    culture = models.ForeignKey(Culture, on_delete =models.CASCADE, null=True) #default=Culture.objects.get_or_create(name='None')[0])
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    url = models.URLField(blank=True)
    short_desc = models.CharField(max_length=SHORT_DESC_MAX_LENGTH)
    vegan_option = models.BooleanField(default=False)
    price_range = models.IntegerField(default=50)

    ## Assuming google maps api can take in this format
    street_num = models.IntegerField(default=0)
    post_code = models.CharField(max_length=POSTCODE_MAX_LENGTH, default='G00aa')



class NightlifePage(models.Model):
    NAME_MAX_LENGTH =128
    SHORT_DESC_MAX_LENGTH =200
    TIME_MAX=2400
    STREET_NUM_MAX_LENGTH =9999
    POSTCODE_MAX_LENGTH =6
    culture = models.ForeignKey(Culture, on_delete =models.CASCADE, null=True)# default=Culture.objects.get_or_create(name='None')[0])
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField(blank=True)
    short_desc = models.CharField(max_length=200, null=True)
    price_range = models.IntegerField(default=50)
    liscenced = models.BooleanField(default=False)
    business = models.CharField(max_length=50, null=True)

    ## Assuming google maps api can take in this format
    street_num = models.IntegerField(default=0)
    post_code = models.CharField(max_length=6, default='G00aa')




class LifestylePage(models.Model):
    NAME_MAX_LENGTH =128
    SHORT_DESC_MAX_LENGTH =200
    TIME_MAX=2400
    STREET_NUM_MAX_LENGTH =9999
    POSTCODE_MAX_LENGTH =6

    culture = models.ForeignKey(Culture, on_delete= models.CASCADE, null=True)#default=Culture.objects.get_or_create(name='None')[0])
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    business = models.CharField(max_length=50, null=True)
    url = models.URLField(blank=True)
    short_desc = models.CharField(max_length=SHORT_DESC_MAX_LENGTH)
    price_range = models.IntegerField(default=50)

    ## Assuming google maps api can take in this format
    street_num = models.IntegerField(default=0)
    post_code = models.CharField(max_length=POSTCODE_MAX_LENGTH,default='G00aa')
