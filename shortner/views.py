from django.shortcuts import HttpResponse, render, redirect
# from django.core.validators import URLValidator
from .models import Url
from django.views import View
from . import urls
from .generator import shortUrl

def home(request):
    return render(request, 'home.html')

def generate(request):
    if request.method == "POST":
        url = request.POST['url']
        urlLength = request.POST['urlength']
        if urlLength != "":
            print(urlLength)
            urlLength = int(urlLength)
        else:
            urlLength = 6
        shorturl = shortUrl(n=urlLength)
        print(url,urlLength, shorturl)
        url_obj = Url(url=url, url_id=shorturl)
        

        # url_obj.url = url

        url_obj.save()
        print("Saved Sucessfully ")
        urls.addUrlsFromDb(url_obj)
        print( urls.addUrlsFromDb(url_obj))

        context = {
            "genratedUrl ": shorturl,
        }
        print(str(context))
        return render(request, 'view.html', {'genratedUrl': shorturl})
    else:
        context = {
            "genratedUrl ": " ",
        }
        # return render(request, 'view.html', context=context)
        return redirect('/')



class UrlView(View):
    url = ""
    def get(self, request):
        return render(request, 'url.html', {'url': self.url})