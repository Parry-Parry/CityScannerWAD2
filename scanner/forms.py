from django import forms
from scanner.models import Culture, NightlifePage, LifestylePage, FoodAndDrinkPage
from django.contrib.auth.models import User
from scanner.models import UserProfile

class NightlifePageForm(forms.ModelForm):
    class Meta:
        model = NightlifePage
        fields = '__all__'

    name = forms.CharField(max_length=NightlifePage.NAME_MAX_LENGTH,
                            help_text="Name of the location.")
    culture = forms.ModelChoiceField(queryset=Culture.objects.all(),help_text="Culture")
    business = forms.CharField(max_length=50,
                help_text="What kind of business is this location")
    url = forms.URLField(help_text="URL to the website")

    street_num = forms.IntegerField(min_value=0,max_value=NightlifePage.STREET_NUM_MAX_LENGTH,
                    help_text="Street number of building")
    post_code = forms.CharField(max_length=NightlifePage.POSTCODE_MAX_LENGTH,
                help_text="Postcode")


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
    culture = forms.ModelChoiceField(queryset=Culture.objects.all(),help_text="Culture")

    business = forms.CharField(max_length=50,
                help_text="What kind of business is this location")
    url = forms.URLField(help_text="URL to the website")

    street_num = forms.IntegerField(min_value=0,max_value=LifestylePage.STREET_NUM_MAX_LENGTH,
                    help_text="Street number of building")
    post_code = forms.CharField(max_length=LifestylePage.POSTCODE_MAX_LENGTH,
                help_text="Postcode")


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

    class Meta:
        model = LifestylePage
        fields='__all__'

class FoodAndDrinkPageForm(forms.ModelForm):

    culture = forms.ModelChoiceField(queryset=Culture.objects.all(),help_text="Culture")


    name = forms.CharField(max_length=FoodAndDrinkPage.NAME_MAX_LENGTH,
                            help_text="Name of the location.")

    url = forms.URLField(help_text="URL to the website")

    street_num = forms.IntegerField(min_value=0,max_value=FoodAndDrinkPage.STREET_NUM_MAX_LENGTH,
                    help_text="Street number of building")
    post_code = forms.CharField(max_length=FoodAndDrinkPage.POSTCODE_MAX_LENGTH,
                help_text="Postcode")

    short_desc = forms.CharField(max_length=FoodAndDrinkPage.SHORT_DESC_MAX_LENGTH,
                help_text="Provide a short description")
    price_range = forms.IntegerField(min_value=0,max_value=100,
                    help_text="On a scale of 0-100 how pricey is this location")
    vegan_option = forms.BooleanField(help_text="Does this restaurant have vegan options")

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data

    class Meta:
        model = FoodAndDrinkPage
        fields='__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields=('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
