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

def detail():
    pass

