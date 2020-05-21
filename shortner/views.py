from django.shortcuts import HttpResponse, render
from .models import Url
from django.views import View
from . import urls

def home(request):
    return render(request, 'home.html')


def generate(request):
    if request.method == "POST":
        url = request.POST['url']
        url_obj = Url()
        url_obj.url = url
        url_obj.save()

        print("Saved Sucessfully ")
        urls.addUrlsFromDb(url_obj)
        print( urls.addUrlsFromDb(url_obj))
        context = {
            "genratedUrl ": url_obj.url_id
        }
        print(str(context))
        return render(request, 'view.html', context=context)
    else:
        context = {
            "genratedUrl ": ""
        }
        return render(request, 'view.html', context=context)


class UrlView(View):
    url = ""
    def get(self, request):
        return render(request, 'url.html', {'url': self.url})