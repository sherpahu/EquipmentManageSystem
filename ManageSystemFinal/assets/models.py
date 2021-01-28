from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import datetime
# Create your models here.

time_now = timezone.now()

class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

def getID():
    return str(datetime.date.today()).replace('-', '') + "-" + str(uuid.uuid4())[:6]

class Asset(models.Model):
    """    设备数据表    """
    task_type_choices = (
        ('张三', '张三'),
        ('李四', '李四'),
        ('王五', '王五'),
    )
    name = models.CharField(max_length=64, verbose_name="设备名")     # 不可重复
    sn = models.CharField(max_length=128, unique=True, default=getID, verbose_name="设备ID号")  # 不可重复
    manufacturer = models.CharField(max_length=128, null=True,verbose_name='购置人')
    idc = models.CharField(max_length=128,  null=True,verbose_name='实验室名')
    purchase_day = models.DateField(null=True, blank=True, default=time_now, verbose_name="购置日期")

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = '设备列表'
        verbose_name_plural = "设备列表"
