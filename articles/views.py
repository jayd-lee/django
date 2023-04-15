from django.shortcuts import render

from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
# Create your views here.

def articles_details_view(request, id=None):    
    articles_obj = None
    if id is not None:
        articles_obj = Article.objects.get(id=id)
    context ={
        'object': articles_obj
    }
    return render(request, 'articles/details.html', context=context)


def articles_search_view(request):
    try:
        query = request.GET.get('q')
    except:
        query = None

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)

    context ={
        'object': article_obj
    }

    return render(request, 'articles/details.html', context)

@login_required
def articles_post_view(request):
    
    form = ArticleForm(request.POST or None)
    context={
        'form': form
        }
    
    if form.is_valid():
        articles_obj = form.save()
        context = {'form': ArticleForm()}

    return render(request, 'articles/create.html', context)