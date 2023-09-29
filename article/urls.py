from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('', views.articles, name = "articles"),
    path('dashboard/',views.dashboard, name = "dashboard"),
    path('addarticle/',views.addarticle, name="addarticle"),
    path('article/<int:id>',views.detail, name="detail"),
    path('update/<int:id>',views.updatearticle, name="updatearticle"),
    path('delete/<int:id>',views.deletearticle, name="deletearticle"),
    path('error/',views.hata, name="hata"),
    path('article/comment/<int:id>',views.articleComment, name="articlecomment"),
]