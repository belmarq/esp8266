from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
class Home(View):
    def get(self, request):
        cdx = {
            'titulo':'Enlaces',
        }
        return render(request, 'index.html', cdx)