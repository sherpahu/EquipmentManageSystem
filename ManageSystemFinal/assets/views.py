from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import get_object_or_404
from . import models
from . import forms
def index(request):
    assets = models.Asset.objects.all()
    return render(request, 'assets/index.html', locals())


def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['user_name'] = user.name
                    return redirect('/assets/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'assets/login.html', {"message": message})
    return render(request, 'assets/login.html')

def add(request):
    register_form = forms.RegisterForm(request.POST)
    if request.method == 'POST':
        # register_form = forms.RegisterForm(request.POST)
        message = '请检查填写内容'
        if register_form.is_valid():
            name = register_form.cleaned_data['name']
            sn = register_form.cleaned_data['sn']
            manufacturer = register_form.cleaned_data['manufacturer']
            idc = register_form.cleaned_data['idc']
            purchase_day = register_form.cleaned_data['purchase_day']

            same_sn = models.Asset.objects.filter(sn=sn)
            if same_sn:
                message = "该设备已存在"
                return render(request, 'assets/add.html', locals())

            new_equipment = models.Asset()
            new_equipment.name = name
            new_equipment.sn = sn
            new_equipment.manufacturer = manufacturer
            new_equipment.idc = idc
            new_equipment.purchase_day = purchase_day
            new_equipment.save()
            message = '添加成功'

            return redirect('/assets/index/')
    else:
        register_form = forms.RegisterForm()
    # register_form = forms.RegisterForm()
    return render(request,'assets/add.html',locals())

# 删除设备
def del_equipment(request,asset_id):
    models.Asset.objects.get(id=asset_id).delete()
    return redirect('/assets/index/')