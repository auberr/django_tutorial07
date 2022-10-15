from django.shortcuts import render, redirect
from articles.models import Article
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            articles = Article.objects.all().order_by('-pk')
            context = {
                "articles" : articles
            }
            return render(request, 'index.html', context)
        elif request.user.is_anonymous:
            return redirect('user:login')
    
    else:
        return HttpResponse('오류')


def write(request):
    if request.method == 'GET':
        return render(request, 'write.html')

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content, user=request.user)
        return redirect("articles:index")

def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        "article": article
    }
    return render(request, "detail.html", context)


def edit(request, article_id):
    if request.method == 'GET':
        article = get_object_or_404(Article, id=article_id)
        context = {
            "article":article
        }
        return render(request, "write_edit.html", context)
    
    elif request.method =='POST':
        article = get_object_or_404(Article, id=article_id)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect("articles:detail", article_id)

def delete(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        article.delete()
    
    return redirect("articles:index")