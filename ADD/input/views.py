from django.shortcuts import render

from .models import *
# Create your views here.

def index(request):

    if request.method == "GET":
        return render(request, "input/index.html", {
            "Foods": Food.objects.all()
        })
    
    # Add new meals to the Database 
    else:
        breakfast = request.POST['Breakfast']
        lunch = request.POST['Lunch']
        dinner = request.POST['Dinner']

        new_meal = Food(Breakfast = breakfast, Lunch = lunch, Dinner = dinner)
        new_meal.save()

        return render(request, "input/index.html", {
            "Foods": Food.objects.all()
        })