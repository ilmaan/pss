from django.shortcuts import render
from .models import Homelem

# Create your views here.

def home(request):

    homes = Homelem.objects.all()


    return render(request, "home.html", {'homes':homes})