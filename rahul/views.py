from email import message
from django.http import HttpResponse
from multiprocessing import context
import profile
from unicodedata import category, name
from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portofolio
from django.core.mail import send_mail

def index(request):


    # Home
    home = Home.objects.latest('updated')

    # about
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    #Skill
    categories = Category.objects.all()

    #Portofolio
    portofolios = Portofolio.objects.all()

    context = {
        'home' : home,
        'about' : about,
        'profiles' : profiles,
        'categories' : categories,
        'portofolios' : portofolios

    }

    return render(request, 'index.html', context)
