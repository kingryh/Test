#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.
'''
创建数据库模型
我们需要 3 个表格：文章（Post）、分类（Category）以及标签（Tag）
多对一和多对多两种关联关系 ForeignKey 和 ManyToManyField
'''
#python_2_unicode_compatible 装饰器用于兼容python2
@python_2_unicode_compatible
class Category(models.Model):
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name
@python_2_unicode_compatible
class Tag(models.Model):
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name
@python_2_unicode_compatible
class Post(models.Model):
	title =models.CharField(max_length=100)
	body=models.TextField()
	created_time=models.DateTimeField()
	modified_time=models.DateTimeField()
	excerpt=models.CharField(max_length=200,blank=True)
	category=models.ForeignKey(Category)
	tags=models.ManyToManyField(Tag,blank=True)
	author=models.ForeignKey(User)
	def __str__(self):
		return self.title
	#自定义get_absolute_url 方法
	#记得从 django.urls中导入reverse函数
	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})
	class Meta:
		ordering=['-created_time']

