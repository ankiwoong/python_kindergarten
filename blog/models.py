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
    createDate = models.DateTimeField('date published')
    updateDate = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, help_text='카테고리')

    def __str__(self):
        return '제목 : %s | 본문 : %s' % (self.title, self.content)

    # 1번 글 -> post/1
    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

    # 300자가 넘을경우
    def is_content_more300(self):
        return len(self.content) > 300

    # 300자가 안넘을경우
    def get_content_under300(self):
        return self.content[:300]
