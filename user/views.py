from django.shortcuts import render,redirect
from .forms import RegisterForm
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.

#Kullancı Kaydı
def register(request):
    """<<<2.YOL>>>"""
    form = RegisterForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarılı bir şekilde kayıt olundu.")
        return redirect("index")
   
    return render(request,"register.html",context)


    """ <<<1.YOL>>>
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            return redirect("index")
        else:
            context = {
                "form":form
            }
            return render(request,"register.html",context)

    else:
        form = RegisterForm()
        context = {
            "form":form
        }
        return render(request,"register.html",context)"""
    
#Kullanıcı Girişi
def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request,"Kullanıcı Adı ve/veya Şifre Hatalı")
            return render(request,"login.html",context)
        
        login(request,user)
        messages.success(request,"Başarılı bir şekilde giriş yapıldı.")
        return redirect("index")
        
    return render(request,"login.html",context)

#Kullanıcı Çıkışı
def logoutUser(request):
    logout(request)
    messages.info(request,"Başarılı bir şekilde çıkış yaptınız.")
    return redirect("index")
