# forms组件
from django.shortcuts import render,HttpResponse,redirect
from app01.models import login


def login_path(request):
    print(2)
    if request.method == 'POST':
        print(1)
        usename = request.POST.get('usename')
        password = request.POST.get('password')
        obj = login.objects.filter(usename=usename,password=password).first()
        if obj:
            reponse = HttpResponse('登录成功')
            reponse.set_cookie('is_login',True)
            reponse.set_cookie('use', usename)
            return reponse
        else:
            pass
    return render(request,'login_test.html')


def index(request):
    cookie = request.COOKIES.get('is_login')
    use = request.COOKIES.get('use')
    if cookie:
        return render(request,'login_win.html',{'use':use})
    else:
        return redirect('/login/')
