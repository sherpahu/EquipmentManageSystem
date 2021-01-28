from django import forms
from . import models
import uuid
import datetime
class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['name', 'password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, *kwargs)
        self.fields['name'].label = '用户名'
        self.fields['password'].label = '密码'

def getID():
    return str(datetime.date.today()).replace('-', '') + "-" + str(uuid.uuid4())[:6]

class RegisterForm(forms.Form):
    task_type_choices = (
        ('张三', '张三'),
        ('李四', '李四'),
        ('王五', '王五'),
    )
    name = forms.CharField(label='设备名',max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    #sn = forms.CharField(label='设备ID号', initial=uuid.uuid1,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    #sn = forms.CharField(label='设备ID号', initial=uuid.uuid1, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    sn = forms.CharField(label='设备ID号', initial=getID, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    #manufacturer = forms.CharField(label='购置人', max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    manufacturer = forms.ChoiceField(label='购置人', widget=forms.Select(), choices=task_type_choices,initial=task_type_choices[0])
    idc = forms.CharField(label='实验室名', max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    purchase_day = forms.DateField(initial=datetime.date.today, label='购置时间',  widget=forms.TextInput(attrs={'class': 'form-control'}))

