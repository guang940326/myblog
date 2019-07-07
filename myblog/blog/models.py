from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

# Create your models here.


class Category(models.Model):   #创建首页分类
    name = models.CharField(max_length=100)


class Tag(models.Model):       #标签
    name = models.CharField(max_length=100)

class Post(models.Model):      #文章
    title = models.CharField(max_length=70)  #文章标题
    content = models.TextField()      #文章内容

    created_time = models.DateTimeField()   #创建时间
    modified_time = models.DateTimeField()  #最后修改时间

    excerpt = models.CharField(max_length=200, blank=True)    #文章摘要

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)   #关联分类和标签

    author = models.ForeignKey(User)     #文章作者

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:               #meta类排序
        ordering = ['-created_time']