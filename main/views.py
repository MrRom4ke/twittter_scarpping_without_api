from django.shortcuts import render
from django.http import HttpRequest
from .forms import MainForm
from .services import *


def index(request):
    if request.method == "POST":
        urls = request.POST.get("urls")
        names = get_username(urls)
        mydict = get_main_info(names)
        return render(request, "index.html", context=mydict)
    else:
        get_urls = MainForm()
        return render(request, "index.html", {"urls_form": get_urls})


def show_tweets(request):
    url = HttpRequest.get_full_path(request)
    name = get_username(url)
    tweets = get_tweets(name[0])
    return render(request, "index.html", {"df_tweets": tweets})
