from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_car  = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    # search_feild = Car.objects.values('model', 'city', 'year', 'body_style')
    model_search = Car.objects.values_list('model',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    

    data = {
        'teams':teams,
        'featured_cars':featured_car,
        'all_cars':all_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search
    }
    return render(request, 'Pages/home.html', data)



def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams

    }
    return render(request, 'Pages/about.html', data)


def cars(request):
    return render(request, 'Pages/cars.html')

def contact(request):
    return render(request, 'Pages/contact.html')

def service(request):
    return render(request, 'Pages/service.html')