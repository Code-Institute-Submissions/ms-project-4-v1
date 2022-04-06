from django.shortcuts import render
from .models import MenuOption


# Create your views here.

def all_food(request):
    """ A view to show all menu options, including sorting """

    menuoption = MenuOption.objects.all()

    context = {
        'menuoption': menuoption,
    }

    return render(request, 'menuoptions/all_food.html', context)
