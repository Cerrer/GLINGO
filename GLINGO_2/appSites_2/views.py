from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import News

class HomePage(View):
    def get(self, request):
        data = {
            'block_css':'home',
        }
        return render(request, 'appSites_2/home/index.html', data)
class NewsPage(View):
    def get(self, request):

        data = {
            'block_css':'news',
            'list_news': News.objects.order_by('-date')
                            }
        return render(request, 'appSites_2/news/index.html', data)
class ProposalPage(View):
    def get(self, request):
        data = {
            'header':{
                'block_css':'proposal',
            }
        }
        return render(request, 'appSites_2/proposal/index.html', data)
class ContactsPage(View):
    def get(self, request):
        data = {
            'block_css':'contacts',
        }
        return render(request, 'appSites_2/contacts/index.html', data)

