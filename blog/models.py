from django.db import models
from django.urls import reverse


# 카테고리
class Category(models.Model):
    name = models.CharField(max_length=50, help_text='카테고리')

    def __str__(self):
        return self.name


# 블로그 글(제목, 작성일, 대표 이미지, 내용, 분류)
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models. TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, help_text='카테고리')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single', args=[str(self.id)])
