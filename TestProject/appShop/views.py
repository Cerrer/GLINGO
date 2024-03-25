from django.shortcuts import render
from django.views import View
from .models import ProductShop
from django.http import JsonResponse, HttpResponse

class HomePage(View):
    def get(self, request):
        obj_products = ProductShop.objects.values('id', 'count','title', 'price')
        return render(request, 'appShop/home.html', {
            'products': obj_products
        })
    def post(self, request):
        product_id = request.POST['id']
        server_type = request.POST['type']
        key_backed = request.session.get('backed')
        if server_type == 'add':
            if key_backed == None:
                request.session['backed'] = [product_id]
            else:
                request.session['backed'] = list(key_backed) + [product_id]
        elif server_type == 'remove':
            index = 0
            for item in key_backed:
                if item == product_id:
                    key_backed.pop(index)
                    request.session['backed'] = key_backed
                    break
                index += 1
        print(request.session['backed'])
        return JsonResponse({})
    

class MethodDjangoPost(View):
    def post(self, request):
        title = request.POST['janr']
        print(title)
        return HttpResponse(f"<h2>Форма сработала!</h2> {title}")
    
class MethodAjaxPost(View):
    def post(self, request):
        print(request.POST['texteria'])
        return JsonResponse({
            'status': 'ok'
        })
