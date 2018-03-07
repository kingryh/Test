from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Comment(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=255)
	url=models.URLField(blank=True)
	text=models.TextField()
	#为DateTimeField传递一个auto_now_add=True的参数值，当评论数据保存到数据库时，自动把created_time的值指定为当前时间
	created_time=models.DateTimeField(auto_now_add=True)
	post=models.ForeignKey('blog.Post',on_delete=models.CASCADE)
	def __str__(self):
		return self.text[:20]