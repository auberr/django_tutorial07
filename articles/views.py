from django.shortcuts import render, redirect
from articles.models import Article, Comment
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            articles = Article.objects.all().order_by('-pk')
            context = {
                "articles" : articles,
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
    likes = article.like_users.all().count()
    comments = list(article.comment_set.all().values())
    context = {
        "article": article,
        "comments": comments,
        "likes": likes
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

def comment(request, article_id):
    if request.method == 'GET':
        return HttpResponse('comment GET')
    
    elif request.method == 'POST':
        content = request.POST.get('content', None)
        article = Article.objects.get(pk=article_id)
        comment = Comment(user=request.user, content=content, article=article)
        comment.save()
        return redirect("articles:detail", article_id)

def comment_edit(request, article_id, comment_id):
    if request.method == 'GET':
        article = get_object_or_404(Article, id=article_id)
        comment = get_object_or_404(Comment, id=comment_id)
        context = {
            "article": article,
            "comment": comment
        }
        return render(request, "detail_comment_edit.html", context)

    if request.method == 'POST':
        content = request.POST.get('content', None)
        article = Article.objects.get(pk=article_id)
        comment = Comment(user=request.user, content=content, article=article)
        comment.save()
        return redirect("articles:detail", article_id)

def comment_delete(request, article_id, comment_id):
    if request.method == 'POST':
        article = Article.objects.get(pk=article_id)
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect("articles:detail", article_id)

def article_like(request, article_id):
    if request.method == 'GET':
        article = Article.objects.get(pk=article_id)
        return HttpResponse('like GET')

    if request.method == 'POST':
        article = Article.objects.get(pk=article_id)
        article.like_users.add(request.user)
        article.save()
        return redirect("articles:index")


