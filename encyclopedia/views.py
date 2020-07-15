from django.shortcuts import render
#HttpResponse imported for test purposes
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.contrib import messages
import random
from markdown2 import Markdown

from . import util

markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    text = util.get_entry(title)
    text = markdowner.convert(text)
    return render(request, "encyclopedia/title.html", {
        "text": text,
        "title": title,
    })

def wiki(request):
    partmatch = []

    # print("the requested data is:", request.POST) # test
    post_dict = request.POST
    # print("the data inside 'q' is:", post_dict['q']) # test
    post_data = post_dict['q']
    text = util.get_entry(post_data)
    text = markdowner.convert(text)
    for entry in util.list_entries():
        # print(entry) # test

        # testa e retorna para caso de .capitalize()
        if post_data.capitalize() == entry:
            # print(post_data.capitalize(), "is equal to", entry.lower()) #test
            post_data = post_data.capitalize()
            return render(request, "encyclopedia/title.html", {
                "text": text,
                "title": post_data,
            })
        # teste e retorna para o caso de .upper()
        elif post_data.upper() == entry:
            post_data = post_data.upper()
            return render(request, "encyclopedia/title.html", {
                "text": text,
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
        repetcounter = 0
        # print('REQUESTED DATA:', request.POST) # test
        post_dict = request.POST
        # print("the data inside 'createtitle' is", post_dict.get('createtitle'))
        # print("the data inside 'content' is", post_dict.get('content')) # test
        # print("title is", postdict['createtitle'], "and content is", postdict['content']) #test
        title = post_dict.get('createtitle')
        content = post_dict.get('content')
        # print(title)
        # print(content)
        for entry in util.list_entries():
            if title == entry:
                repetcounter += 1
        if repetcounter == 0:
            content = markdowner.convert(content)
            util.save_entry(title, content)
            return render(request, "encyclopedia/title.html", {
                "text": content,
                "title": title,
                })
        else:
            # print('error: the page exists - use edit instead') # test
            # present error message
            messages.error(request,"error: a page with the given title already exists - use 'Edit Page' instead")
            return render(request, "encyclopedia/create.html")
    return render(request, "encyclopedia/create.html")

def edit(request, title):
    if request.method == "POST":
        # print(request.POST) # test
        # print(request.GET) # test
        post_dict = request.POST
        util.save_entry(post_dict.get("title"), post_dict.get("content"))
        return render(request, "encyclopedia/title.html", {
            "text": post_dict.get("content"),
            "title": title,
            })
    return render(request, "encyclopedia/edit.html", {
        "text": util.get_entry(title),
        "title": title,
        })

def alea(request):
    # print(request.POST) # test
    # print(request.GET) # test
    title_list = util.list_entries()
    # print(title_list) # test
    title = random.choice(title_list)
    text = util.get_entry(title)
    text = markdowner.convert(text)
    return render(request, "encyclopedia/title.html", {
        "text": text,
        "title": title,
    })