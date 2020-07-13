from django.shortcuts import render
#HttpResponse imported for test purposes
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#function to get the correct .md to render
#still has some capitalization issues
def title(request, title):
    return render(request, "encyclopedia/title.html", {
        "text": util.get_entry(title),
        "title": title,
    })

#WORKING CODE
def wiki(request):
    print("the requested data is:", request.POST)
    post_dict = request.POST
    print("the inside data is:", post_dict['q'])
    post_data = post_dict['q']
    return render(request, "encyclopedia/title.html", {
        "text": util.get_entry(post_data),
        "title": post_data,
    })