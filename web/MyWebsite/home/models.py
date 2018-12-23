from django.db import models

# Create your models here.


#留言表
class LeaveMessage(models.Model):
    user_id = models.CharField(max_length=100)
    message = models.TextField(max_length=256)
    create_date = models.DateTimeField(auto_now_add=True)

#用户表
class User(models.Model):
    gender = (('1','男'),('2','女'))
    account = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    sex = models.CharField(max_length=25,choices=gender,default='')
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=55)
    creDate = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(auto_now=True)
    enable = models.IntegerField(default=1)

    class Meta:
        db_table = 'User'
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.name