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

#search function that comports partially macthing string
def wiki(request):
    partmatch = []

    # print("the requested data is:", request.POST) # test
    post_dict = request.POST
    # print("the data inside 'q' is:", post_dict['q']) # test
    post_data = post_dict['q']

    for entry in util.list_entries():
        # print(entry) # test

        # testa e retorna para caso de .capitalize()
        if post_data.capitalize() == entry:
            # print(post_data.capitalize(), "is equal to", entry.lower()) #test
            post_data = post_data.capitalize()
            return render(request, "encyclopedia/title.html", {
                "text": util.get_entry(post_data),
                "title": post_data,
            })
        # teste e retorna para o caso de .upper()
        elif post_data.upper() == entry:
            post_data = post_data.upper()
            return render(request, "encyclopedia/title.html", {
                "text": util.get_entry(post_data),
                "title": post_data,
            })
        elif post_data.lower() in entry.lower():
            # print(entry) #test
            partmatch.append(entry)
    # print(partmatch)     
    return render(request, "encyclopedia/results.html", {
        "entries": partmatch,
        })

def create(request):
    if request.method == "POST":
        print('REQUESTED DATA:', request.POST) # test
        post_dict = request.POST
        print("the data inside 'createtitle' is", post_dict.get('createtitle'))
        print("the data inside 'content' is", post_dict.get('content')) # test
        # print("title is", postdict['createtitle'], "and content is", postdict['content']) #test
        title = post_dict.get('createtitle')
        content = post_dict.get('content')
        print(title)
        print(content)
        util.save_entry(title, content) 
    return render(request, "encyclopedia/create.html")