# CityScannerWAD2
Group Project

Pre-requisite: anaconda installed

From the main project directory run the following commands :

`conda create -n scanner python=3.7.2`

`conda activate scanner`

`pip install django==2.2.3`

`pip install pillow`

`python manage.py makemigrations scanner`

`python manage.py migrate`

`python population_script.py`

`python manage.py runserver`

------------------------------

The server should now be up and running and populated with some data!
From the homepage you can add locations, search locations or login/register
The site has been populated with three different cultures/nationalities:

-Spanish

-Chinese

-Greek

Spanish:

        Nightlife - Mango Tropical
        
        Lifestyle - N/A
        
        FoodAndDrink - Iberica Glasgow, The Spanish Butcher
        
Chinese:
       
        Nightlife - N/A
        
        Lifestyle - Lims
        
        FoodAndDrink - Lychee Oriental

Greek:

        Nightlife - N/A

        Lifestyle - Style City, Greek Orthodox Cathedral of St. Luke

        FoodAndDrink - Halloumi
