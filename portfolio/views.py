from django.shortcuts import render
from .models import Projects,Profile

# Create your views here.
def home_view(request):
    context = {
        'projects': Projects.objects.all(),
        'profiles': Profile.objects.all()

    }
    return render(request,'portfolio/home.html',context)
