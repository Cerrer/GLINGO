from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import ContentBanner, AboutMe, Documents

class HomePage(View):
    def get(self, request):
        # print(AboutMe.objects.first())   # вытягивает первый объект
        # print(AboutMe.objects.all()[1])    # вытягивает 2 объект
        data = {
            'banner':ContentBanner.objects.order_by("number"),
            'about_me':AboutMe.objects.first(),
            'documents':Documents.objects.all()
        }
        return render(request, 'appSites_2/home/index.html', data)
