from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.
class User(models.Model):
    PLAN_CHOICES = (
        ('simple','simple'),
        ('premium', 'premium'),
        ('nobless', 'nobless'),
    )
    email = models.EmailField(max_length=128,verbose_name='사용자이메일', unique=True)
    name = models.CharField(max_length=30,verbose_name="사용자 이름")
    plan = models.CharField(max_length= 20, choices=PLAN_CHOICES,verbose_name="사용자 구독 플랜")
    password = models.CharField(max_length=30,verbose_name="비밀번호")
    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=200, null=False,verbose_name="기부단체 이름")
    thumbnail = models.ImageField(upload_to="%Y/%m/%d",blank=False,verbose_name="썸네일")
    link = models.CharField(max_length=200,verbose_name="단체 링크")
    context = models.TextField(verbose_name="간단한 설명")
    def __str__(self):
        return self.name


class User_Choiced(models.Model):
    # pk : django 자동으로 제공하는 id 값으로 할거임
    user = models.ForeignKey(User,on_delete=CASCADE,verbose_name="유저")
    coin = models.IntegerField(null=False,verbose_name="코인")
    orga = models.ForeignKey(Organization,on_delete=CASCADE,verbose_name="기부단체")
    date = models.DateTimeField()
    def __str__(self):
        return self.user.name+" "+self.orga.name

