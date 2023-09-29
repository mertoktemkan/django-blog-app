from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.conf import settings
# Create your views here.

#Anasayfa
def index(request):
    return render(request,"index.html")

#Hakkında
def about(request):
    return render(request,"about.html")

#Makaleler
def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request, "articles.html", {"articles":articles})
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles":articles})

#Dashboard
@login_required(login_url="article:hata")
def dashboard(request):
        articles = Article.objects.filter(author = request.user)
        return render(request,"dashboard.html",{"articles":articles})

#Makale Ekleme
@login_required(login_url="article:hata")
def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarılı bir şekilde eklendi.")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})

#Makale Detay Sayfası
def detail(request,id):
    article = get_object_or_404(Article, id=id)
    
    comments = article.comments.all()
    return render(request,"detail.html",{"article":article, "comments":comments})

# Makale Güncelle
@login_required(login_url="article:hata")
def updatearticle(request,id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if article.author == request.user:
        if form.is_valid():
            form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Makale başarılı bir şekilde güncellendi.")
            return redirect("article:dashboard")
        return render(request, "updatearticle.html", {"form":form})
    else:
        messages.error(request, "Yetkisiz İşlem")
        return redirect("article:dashboard")

#Makale Silme
@login_required(login_url="article:hata")
def deletearticle(request,id):
    article = get_object_or_404(Article, id=id)
    if article.author == request.user:
        article.delete()
        messages.success(request, "Makale başarılı bir şekilde silindi.")
        return redirect("article:dashboard")
    else:
        messages.error(request, "Yetkisiz İşlem")
        return redirect("article:dashboard")

def hata(request):
    messages.error(request, "Yetkisiz İşlem!")
    return redirect("index")

def articleComment(request,id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.article = article
        newComment.save()

    return redirect(reverse("article:detail",kwargs={"id":id}))
    
 