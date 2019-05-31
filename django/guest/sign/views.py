from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get("username",'')
        password = request.POST.get("password",'')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            #添加浏览器cookie：
            #第一个参数表示写入浏览器的cookie；
            #第二个参数username是由用户在登录页上输入的用户名；
            #第三个参数用户设置Cookie信息在浏览器中的保持时间，默认单位为秒
            # response.set_cookie('user',username,3600)

            response.session['user'] = username #将session信息记录到浏览器
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

#发布会管理
def event_manage(request):
    # username = request.COOKIES.get('user','')#读取浏览器cookie
    username = request.session.get('user','')#读取浏览器session
    return render(request,"event_manage.html",{"user":username})