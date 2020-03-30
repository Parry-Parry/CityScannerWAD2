from django.shortcuts import render, reverse, redirect
from scanner.forms import NightlifePageForm, LifestylePageForm, FoodAndDrinkPageForm, UserForm, UserProfileForm
from scanner.models import NightlifePage, LifestylePage, FoodAndDrinkPage, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse



# Create your views here.
def homepage(request):
    return render(request, 'scanner/homepage.html')

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
            login(request, user)
            return redirect(reverse('home'))
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'scanner/login.html')
