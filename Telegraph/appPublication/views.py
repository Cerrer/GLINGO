from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import PubNews
import uuid


class PublicationPage(View):
    def get(self, request):
        return render(request, 'appPublication/views-edit.html')
    def post(self, request):
        print(request.POST)
        name_url = str(uuid.uuid4())[:5]
        get_pub, created = PubNews.objects.get_or_create(
            name_url=name_url,
            defaults={
                "content":request.POST['content']
            }
        )
        if created:
            # get_pub.content = request.POST['content'],
            # get_pub.save()
            return JsonResponse({
                "status": "ok",
                "url": get_pub.name_url
            })
        return JsonResponse({
            "status": "Erorr",
        })