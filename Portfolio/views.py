from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

from .models import Portfolio, Skills, Statistics, Services, Contact


# View metodida - 2xil usul bor


# 1) Agar html fayllar bittani ichida ishlailsa - index funksiya metodidan foydalaniladi

# 2) Agar html fayl ko'p bo'lsa - ListView klasslik metoddan foydalanamiz


# class PortfoliyomViews(ListView):
#     model = Portfolio
#     context_object_name = 'portfolio'
#     template_name = 'index.html'

def index(request):
    portfolio = Portfolio.objects.all()
    statistics = Statistics.objects.all()
    skills = Skills.objects.all()
    services = Services.objects.all()
    contact = Contact.objects.all()

    contex = {
        'portfolio':portfolio,
        'statistics':statistics,
        'Skills':skills,
        'Services':services,
        'Contact':contact,

        
    }
    return render(request, ['index.html'], contex)