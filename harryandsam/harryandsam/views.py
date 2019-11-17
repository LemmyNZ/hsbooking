from django.http import HttpResponse
from django.shortcuts import render
from accounts.models import Accounts


def home_page(request):
    accounts = Accounts.objects.all()
    template_name = 'home.html'
    return render(request, template_name)