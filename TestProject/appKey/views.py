from django.shortcuts import render, redirect
from django.http import JsonResponse #--> отображать словарь для API
from django.views import View
from .models import Product, Category 

class HomeKey(View):
    def get(self, request):
        data = {
            'product': Product.objects.get(id=7)
        }
        return render(request, 'appKey/product/index.html', data)
    def post(self, request):
        if request.POST['method'] == 'addCategory':
            Category.objects.create(
                title=request.POST['text']
            )
            Category.objects.filter(id=7).update(            # - Обновление
                title=request.POST['text']
            )
            # print(request.POST['method'])
            # print(request.POST['text'])
            Category.objects.filter(id=4).delete(            # - Удаление
                title=request.POST['text']
            )
        return redirect('urlHomeKey')