__author__ = 'Administrator'
from django.db import models

# Create your models here.
class Item (models.Model):
	content = models.CharField("��������", max_length=200)
	is_done = models.BooleanField("����״̬", default=False)
	pub_date = models.DateTimeField("����ʱ��", auto_now_add=True)

	class Meta():
		verbose_name = "��������"
		verbose_name_plural = verbose_name

    def __str__(self):
        return self.content