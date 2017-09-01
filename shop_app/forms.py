#！/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2017/8/22
@author: sumin
"""
from django import forms
from django.conf import settings
from django.db.models import Q
from .models import shop_user
import re

class LoginForm(forms.Form):
    '''
    登录Form
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "用户名", "required": "required",}),
                              max_length=50,error_messages={"required": "用户名不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "密码", "required": "required",}),
                              max_length=20,error_messages={"required": "密码不能为空",})

class RegForm(forms.Form):
    '''
    注册表单
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "用户名", "required": "required",}),
                              max_length=50,error_messages={"required": "用户名不能为空",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "邮箱,地址格式类似于：1111111111@qq.com", "required": "required",}),
                              max_length=50,error_messages={"required": "邮箱不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "密码(6位数字)", "required": "required",}),
                              max_length=20,error_messages={"required": "密码不能为空",})

