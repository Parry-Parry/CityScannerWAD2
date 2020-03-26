from django import forms
from scanner.models import Culture, NightlifePage, LifestylePage, FoodAndDrinkPage
from django.contrib.auth.models import User
from rango.models import UserProfile

class NightlifePageForm(forms.ModelForm):

    name = forms.CharField(max_length=NightlifePage.NAME_MAX_LENGTH,
                            help_text="Name of the location.")
    business = forms.CharField(max_length=50,
                help_text="What kind of business is this location")
    url = forms.URLField(help_text="URL to the website")

    street_num = forms.IntegerField(min_value=0,max_value=NightlifePage.STREET_NUM_MAX_LENGTH,
                    help_text="Street number of building")
    post_code = forms.StringField(max_length=NightlifePage.POSTCODE_MAX_LENGTH,
                help_text="Postcode")

    mon_open = forms.IntegerField(min_value=0, max_value=NightlifePage.TIME_MAX,
            help_text="Monday Opening Hours")
    tues_open = modls.IntegerField(min_value=0, max_value=NightlifePage.TIME_MAX,
            help_text="Tuesday Opening Hours")
    wed_open = models.IntegerField(min_value=0, max_value=NightlifePage.TIME_MAX,
            help_text="Wednesday Opening Hours")
    thur_open = models.IntegerField(min_value=0, max_value=NightlifePage.TIME_MAX,
            help_text="Thursday Opening Hours")
    fri_open = models.IntegerField(min_value=0, max_value=NightlifePage.TIME_MAX,
            help_text="Friday Opening Hours")
    sat_open = models.IntegerField(min_value=0, max_value=NightlifePage.TIME_MAX,
            help_text="Saturday Opening Hours")
    sun_open = models.IntegerField(min_value=0, max_value=NightlifePage.TIME_MAX,
            help_text="Sunday Opening Hours")

    short_desc = forms.CharField(max_length=NightlifePage.SHORT_DESC_MAX_LENGTH,
                help_text="Provide a short description")
    price_range = forms.IntegerField(min_value=0,max_value=100,
                    help_text="On a scale of 0-100 how pricey is this location")
    liscenced = forms.BooleanField(help_text="Is this location liscenced to sell alcohol")
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data

class LifestylePageForm(forms.ModelForm):

    name = forms.CharField(max_length=LifestylePage.NAME_MAX_LENGTH,
                            help_text="Name of the location.")
    business = forms.CharField(max_length=50,
                help_text="What kind of business is this location")
    url = forms.URLField(help_text="URL to the website")

    street_num = forms.IntegerField(min_value=0,max_value=LifetsylePage.STREET_NUM_MAX_LENGTH,
                    help_text="Street number of building")
    post_code = forms.StringField(max_length=LifestylePage.POSTCODE_MAX_LENGTH,
                help_text="Postcode")

    mon_open = forms.IntegerField(min_value=0, max_value=LifestylePage.TIME_MAX,
            help_text="Monday Opening Hours")
    tues_open = modls.IntegerField(min_value=0, max_value=LifestylePage.TIME_MAX,
            help_text="Tuesday Opening Hours")
    wed_open = models.IntegerField(min_value=0, max_value=LifestylePage.TIME_MAX,
            help_text="Wednesday Opening Hours")
    thur_open = models.IntegerField(min_value=0, max_value=LifestylePage.TIME_MAX,
            help_text="Thursday Opening Hours")
    fri_open = models.IntegerField(min_value=0, max_value=LifestylePage.TIME_MAX,
            help_text="Friday Opening Hours")
    sat_open = models.IntegerField(min_value=0, max_value=LifestylePage.TIME_MAX,
            help_text="Saturday Opening Hours")
    sun_open = models.IntegerField(min_value=0, max_value=LifestylePage.TIME_MAX,
            help_text="Sunday Opening Hours")

    short_desc = forms.CharField(max_length=LifestylePage.SHORT_DESC_MAX_LENGTH,
                help_text="Provide a short description")
    price_range = forms.IntegerField(min_value=0,max_value=100,
                    help_text="On a scale of 0-100 how pricey is this location")

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data

class FoodAndDrinkPageForm(forms.ModelForm):

    name = forms.CharField(max_length=FoodAndDrinkPage.NAME_MAX_LENGTH,
                            help_text="Name of the location.")

    url = forms.URLField(help_text="URL to the website")

    street_num = forms.IntegerField(min_value=0,max_value=FoodAndDrinkPage.STREET_NUM_MAX_LENGTH,
                    help_text="Street number of building")
    post_code = forms.StringField(max_length=FoodAndDrinkPage.POSTCODE_MAX_LENGTH,
                help_text="Postcode")

    mon_open = forms.IntegerField(min_value=0, max_value=FoodAndDrinkPage.TIME_MAX,
            help_text="Monday Opening Hours")
    tues_open = modls.IntegerField(min_value=0, max_value=FoodAndDrinkPage.TIME_MAX,
            help_text="Tuesday Opening Hours")
    wed_open = models.IntegerField(min_value=0, max_value=FoodAndDrinkPage.TIME_MAX,
            help_text="Wednesday Opening Hours")
    thur_open = models.IntegerField(min_value=0, max_value=FoodAndDrinkPage.TIME_MAX,
            help_text="Thursday Opening Hours")
    fri_open = models.IntegerField(min_value=0, max_value=FoodAndDrinkPage.TIME_MAX,
            help_text="Friday Opening Hours")
    sat_open = models.IntegerField(min_value=0, max_value=FoodAndDrinkPage.TIME_MAX,
            help_text="Saturday Opening Hours")
    sun_open = models.IntegerField(min_value=0, max_value=FoodAndDrinkPage.TIME_MAX,
            help_text="Sunday Opening Hours")

    short_desc = forms.CharField(max_length=FoodAndDrinkPage.SHORT_DESC_MAX_LENGTH,
                help_text="Provide a short description")
    price_range = forms.IntegerField(min_value=0,max_value=100,
                    help_text="On a scale of 0-100 how pricey is this location")
    vegan_option = form.BooleanField(help_text="Does this restaurant have vegan options")
    
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data
