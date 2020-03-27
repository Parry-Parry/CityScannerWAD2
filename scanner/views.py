from django.shortcuts import render
from scanner.forms import NightlifePageForm, LifestylePageForm, FoodAndDrinkPageForm
from scanner.models import NightlifePage, LifestylePage, FoodAndDrinkPage

# Create your views here.
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
