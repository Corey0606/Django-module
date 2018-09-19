# forms组件
from django.shortcuts import render,HttpResponse,redirect
# from app01.models import login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.contrib.auth.models import User
# def add_login(request):
#     obj = login.objects.create(usename='cjj',password='123')
#     return HttpResponse('ok')
def login_path(request):
    print(2)
    if request.method == 'POST':
        print(1)
        use = request.POST.get('usename')
        # print(usename)

        pwd = request.POST.get('password')
        # print(password)
        user = auth.authenticate(username=use,password=pwd)

        print('user',user)
        if user :
            auth.login(request,user)
            return render(request,'login_win.html')

        # obj = login.objects.filter(usename=usename,password=password).first()
        # if obj:
        #     reponse = HttpResponse('登录成功')
        #     reponse.set_cookie('is_login',True)
        #     reponse.set_cookie('use', usename)
        #     return reponse
        # else:
        #     pass
    return render(request,'login_test.html')

#
# def index(request):
#     cookie = request.COOKIES.get('is_login')
#     use = request.COOKIES.get('use')
#     if cookie:
#         return render(request,'login_win.html',{'use':use})
#     else:
#         return redirect('/login/')
def layout_do(request):
    print('usename',request.user.username)
    auth.logout(request)
    return HttpResponse('退出')

@login_required
def index(request):
    return render(request,'login_win.html')

def index1(request):
    if request.user.is_authenticated:
        return render(request,'login_win.html')
    return redirect('/login/')
#
# def set_session(request):
#     if request.method == 'POST':
#         usename = request.POST.get('usename')
#         password = request.POST.get('password')
#         obj = login.objects.filter(usename=usename, password=password).first()
#         if obj:
#             request.session['is_login'] = True
#             request.session['usename']=usename
#             return HttpResponse('登录成功')
#     return render(request, 'login_test.html')
# #
# # def get_session(request):
# #     # get_data = request.session.get('is_login',default = None)
# #     # use = request.session.get('usename', default=None)
# #     get_data = request.session.get('is_login',default = None)
# #     use = request.session.get('usename',default = None)
#     if get_data:
#         return render(request,'login_win.html',{'use':use})
#     else:
#         return redirect('/set_session/')
#     # try:
#     #     back = request.session.exists('is_login')
#     #     # if back:
#     #     print(back)
#     #     return HttpResponse('okk')
#     #
#     #     # get_data = request.session['is_login']
#     #     #
#     #     # use = request.session['usename']
#     # except:
#     #     print(1111)
#     #     redirect('/set_session/')
#     # if get_data:
#     #     print (1)
#         # return HttpResponse('WDQO')
#     # return render(request,'login_win.html')
#     # else:
#     #     redirect('/set_session/')
#
# def del_session(request):
#     del request.session['is_login']
#     del request.session["usename"]
#     return HttpResponse('ok')



