from django.shortcuts import render, reverse, redirect
from scanner.forms import NightlifePageForm, LifestylePageForm, FoodAndDrinkPageForm, UserForm, UserProfileForm
from scanner.models import NightlifePage, LifestylePage, FoodAndDrinkPage, UserProfile, Culture
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse



# Create your views here.
def homepage(request):

    return render(request, 'scanner/homepage.html')
def search(request):
    return render(request, 'scanner/search.html')

def choose_type(request,culture_name_slug):
    context_dict={}
    try:
        culture = Culture.objects.get(slug=culture_name_slug)
        context_dict['culture']= culture
    except Culture.DoesNotExist:
        context_dict['culture'] = None
    
    return render(request, 'scanner/choose_type.html', context=context_dict)

def show_nightlife(request,culture_name_slug):
    context_dict={}

    try:
        culture = Culture.objects.get(slug=culture_name_slug)
        pages = NightlifePage.objects.filter(culture=culture)
        context_dict['pages'] = pages
        context_dict['culture']  = culture

    except Culture.DoesNotExist:
        context_dict['culture'] = None
        context_dict['pages'] = None

    return render(request, 'scanner/results.html', context=context_dict)
def show_lifestyle(request,culture_name_slug):
    context_dict={}

    try:
        culture = Culture.objects.get(slug=culture_name_slug)
        pages = LifestylePage.objects.filter(culture=culture)
        context_dict['pages'] = pages
        context_dict['culture']  = culture

    except Culture.DoesNotExist:
        context_dict['culture'] = None
        context_dict['pages'] = None

    return render(request, 'scanner/results.html', context=context_dict)

def show_foodanddrink(request,culture_name_slug):
    context_dict={}

    try:
        culture = Culture.objects.get(slug=culture_name_slug)
        pages = FoodAndDrinkPage.objects.filter(culture=culture)
        context_dict['pages'] = pages
        context_dict['culture']  = culture

    except Culture.DoesNotExist:
        context_dict['culture'] = None
        context_dict['pages'] = None

    return render(request, 'scanner/results.html', context=context_dict)

@login_required
def add_nightlife_page(request):
    form = NightlifePageForm()

    if request.method == 'POST':
        form = NightLifePageForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/admin/')
        else:
            print(form.errors)

    return render(request, 'scanner/add_nightlife_page.html', {'form':form})

@login_required
def add_lifestyle_page(request):
    form = LifestylePageForm()

    if request.method == 'POST':
        form = LifestylePageForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/admin/')
        else:
            print(form.errors)
    return render(request, 'scanner/add_lifestyle_page.html', {'form':form})

@login_required
def add_foodanddrink_page(request):
    form = FoodAndDrinkPageForm()

    if request.method == 'POST':
        form = FoodAndDrinkPageForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/admin/')
        else:
            print(form.errors)
    return render(request, 'scanner/add_foodanddrink_page.html', {'form':form})

def register(request):
    registered=False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile= profile_form.save(commit=False)
            profile.user =user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                    'scanner/register.html',
                    context = {'user_form': user_form,
                                'profile_form': profile_form,
                                'registered': registered})

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('scanner:profile'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'scanner/login.html')

@login_required
def show_profile(request):
    context_dict={'user': request.user}
    return render(request, 'scanner/show_profile.html', context_dict)

def user_logout(request):
    logout(request)
    return redirect(reverse('home'))
