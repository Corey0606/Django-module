from django.db import models

# Create your models here.
# from django.db import models
# Create your models here.
from django import forms
from django.forms import widgets

wid_01=widgets.TextInput(attrs={"class":"form-control"})
wid_02=widgets.PasswordInput(attrs={"class":"form-control"})

from django.core.exceptions import ValidationError
class UserForm(forms.Form):
    name=forms.CharField(max_length=32,
                         widget=wid_01
                         )
    pwd=forms.CharField(max_length=32,widget=wid_02)
    r_pwd=forms.CharField(max_length=32,widget=wid_02)
    email=forms.EmailField(widget=wid_01)
    tel=forms.CharField(max_length=32,widget=wid_01)


    # 局部钩子
    def clean_name(self):
        val=self.cleaned_data.get("name")
        if not val.isdigit():
            return val
        else:
            raise ValidationError("用户名不能是纯数字!")

    # 全局钩子

    def clean(self):
        pwd=self.cleaned_data.get("pwd")
        r_pwd=self.cleaned_data.get("r_pwd")

        if pwd==r_pwd:
            return self.cleaned_data
        else:
            raise ValidationError('两次密码不一致!')







