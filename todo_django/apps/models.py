# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Item( models.Model ):
	content = models.CharField("待办内容", max_length=200)
	is_done = models.BooleanField("事项状态", default=False)
	pub_date = models.DateTimeField("发布时间", auto_now_add=True)

	class Meta():
		verbose_name = "待办事项"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.content