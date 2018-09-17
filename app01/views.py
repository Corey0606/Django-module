# forms组件
from django.shortcuts import render
from django import forms
from django.forms import widgets

wid_01=widgets.TextInput(attrs={"class":"form-control"})
wid_02=widgets.PasswordInput(attrs={"class":"form-control"})

from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    name = forms.CharField(max_length=32,
                         widget=wid_01
                         )
    pwd=forms.CharField(max_length=32,widget=wid_02)
    r_pwd=forms.CharField(max_length=32,widget=wid_02)
    email=forms.EmailField(widget=wid_01)
    tel=forms.CharField(max_length=32,widget=wid_01)
    # 局部钩子
    def clean_name(self):
        print('clean_name')
        val=self.cleaned_data.get("name")
        print('val',val)
        if not val.isdigit():
            print('digit')
            return val
        else:
            print('error')
            raise ValidationError("用户名不能是纯数字!")

    # 全局钩子

    def clean(self):
        print('clean')
        pwd=self.cleaned_data.get("pwd")
        print('pwd' ,pwd)
        r_pwd=self.cleaned_data.get("r_pwd")
        print('r_pwd',r_pwd)

        if pwd==r_pwd:

            print('self.cleaned_data',self.cleaned_data)
            return self.cleaned_data
        else:
            print('clean_error')
            raise ValidationError('两次密码不一致!')


def register(request):

    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            print('form.cleaned_data',form.cleaned_data)       # 所有干净的字段以及对应的值
        else:
            clean_error=form.errors.get("__all__")
            print('clean_error',clean_error)

        return render(request,"form_test.html",locals())
    form=UserForm()
    return render(request,"form_test.html",locals())