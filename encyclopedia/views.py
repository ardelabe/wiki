from django.shortcuts import render
#HttpResponse imported for test purposes
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#function to render layout
def title(request, title):
    return render(request, "encyclopedia/layout.html")