from django.http import HttpResponse
from articles.models import Article
from django.shortcuts import render

def home_view(request):
    articles_obj = Article.objects.all()

    context = {
        'object': articles_obj,
    }
    return render(request, "home-view.html", context=context)

