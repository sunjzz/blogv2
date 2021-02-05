from django.db import models

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=64, unique=True, verbose_name="用户名")
    email = models.EmailField(verbose_name="邮箱")
    password = models.CharField(max_length=128, verbose_name="用户密码")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="注册日期")
    signature = models.CharField(max_length=128, blank=True, null=True, verbose_name="签名")
    avatar = models.ImageField(upload_to='static/image/', default='static/image/default.jpg',
                               verbose_name="用户图像")


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="文章标题")
    content = models.TextField(blank=True, null=True, verbose_name="博客正文")
    account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='art')
    tags = models.ManyToManyField('Tag', null=True, verbose_name="博客标签")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="发表时间")
    read_count = models.IntegerField(verbose_name="阅读量", null=True)
    like = models.IntegerField(verbose_name="点赞量", null=True)


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='标签名称')
    date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


