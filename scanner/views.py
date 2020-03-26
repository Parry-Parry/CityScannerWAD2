from django.shortcuts import render
from scanner.forms import NightlifePageForm
from scanner.models import NightlifePage

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
