from django.http import HttpResponse, HttpResponseNotFound
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
import logging
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from .models import *
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password
from .forms import *

logger = logging.getLogger('maizi_app.views')

# Create your views here.
# 分页代码
def getPage(request, shoppro_list):
    paginator = Paginator(shoppro_list, 8)
    try:
        page = int(request.GET.get('page', 1))
        shoppro_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        shoppro_list = paginator.page(1)
    return shoppro_list

# 注册
def reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                #注册
                user = shop_user.objects.create(username=reg_form.cleaned_data['username'],
                                                email=reg_form.cleaned_data['email'],
                                                password=make_password(reg_form.cleaned_data['password']),)
                user.save()

                # 登录
                user.backend = 'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
                login(request, user)
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason': reg_form.errors})
        else:
            reg_form = RegForm()

    except Exception as e:
        logger.error(e)
    return render(request, 'reg.html', locals())

#登录
def login(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 登录
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username, password=password)  #authenticate（）验证方法
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                    login(request, user)
                else:
                    # 登录信息错误，执行
                    return render(request, 'failure.html', {'reason': '登录验证失败'})
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason': login_form.errors})
        else:
            login_form = LoginForm()
    except Exception as e:
        logger.error(e)
    return render(request, 'login.html', locals())


def index(request):
    try:
        ad_list = Ad.objects.all()
        shopadmin_list = shop_admin.objects.all()
        shopuser_list = shop_user.objects.all()
        shopcat_list = shop_cat.objects.all()
        shoppro_list = shop_pro.objects.all()
        CarItem_list = CarItem.objects.all()
    except Exception as e:
        logger.error(e)
    return TemplateResponse(request, 'index.html', locals())

def products(request):
    try:
        shopadmin_list = shop_admin.objects.all()
        shopuser_list = shop_user.objects.all()
        shopcat_list = shop_cat.objects.all()
        shoppro_list = shop_pro.objects.all()
        CarItem_list = CarItem.objects.all()
    except Exception as e:
        logger.error(e)
    return TemplateResponse(request, 'products.html', locals())

def seachpro(request):
    try:
        shopadmin_list = shop_admin.objects.all()
        shopuser_list = shop_user.objects.all()
        shopcat_list = shop_cat.objects.all()
        shoppro_list = shop_pro.objects.all()
        shoppro_list = getPage(request, shoppro_list)
        CarItem_list = CarItem.objects.all()
    except Exception as e:
        logger.error(e)
    return TemplateResponse(request, 'seachpro.html', locals())

def shopcar(request):
    try:
        shopadmin_list = shop_admin.objects.all()
        shopuser_list = shop_user.objects.all()
        shopcat_list = shop_cat.objects.all()
        shoppro_list = shop_pro.objects.all()
        CarItem_list = CarItem.objects.all()
    except Exception as e:
        logger.error(e)
    return TemplateResponse(request, 'shopcar.html', locals())

