from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import ContentBanner

class HomePage(View):
    def get(self, request):
        data = {
            'obj':ContentBanner.objects.order_by("number"),
        }
        return render(request, 'appSites_2/home/index.html', data)
