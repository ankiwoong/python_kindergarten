from django.db import models
from django.urls import reverse

# Create your models here.
# 글의 분류(일상, 유머, 정보)


class Category(models.Model):
    # 분류 : 최대길이 50자
    name = models.CharField(max_length=50, help_text="분류를 입력하세요.")

    def __str__(self):
        return self.name

# 블로그 글(제목, 작성일, 대표이미지, 내용, 분류)


class Post(models.Model):
    # 글 제목 : 최대길이 200자
    title = models.CharField(max_length=200)
    # 대표 이미지 : 비어있어도 됨
    title_image = models.ImageField(blank=True)
    # 글 내용 : 내용의 글자수는 정해지지 않으므로 TextField
    content = models.TextField()
    # 작성일 : 사용자가 입력하지 않고 현재 날짜를 받아옴
    createDate = models.DateTimeField(auto_now_add=True)
    # 수정일 : 사용자가 입력하지 않고 현재 날짜를 받아옴
    updateDate = models.DateTimeField(auto_now_add=True)
    # 분류 : 다대다 관계정의
    category = models.ManyToManyField(category, help_text='분류를 입력하세요.')

    def __str__(self):
        return self.title

    # 1번 글의 경우 -> single/1

    def get_absolute_url(self):
        return reverse('single'. args=[str(self.id)])
