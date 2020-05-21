# pip install django-model-utils
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from model_utils.models import TimeStampedModel
from django.conf import settings
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
    # createDate = models.DateTimeField('date published')           # 강제 수정날짜
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, help_text='카테고리')

    def __str__(self):
        return '제목 : %s | 본문 : %s' % (self.title, self.content)

    # 1번 글 -> post/1
    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

    # 300자가 넘을경우
    # def is_content_more300(self):
    #     return len(self.content) > 300

    # 300자가 안넘을경우
    # def get_content_under300(self):
    #     return self.content[:300]


class AuditEntry(models.Model):
    action = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    username = models.CharField(max_length=256, null=True)

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_logged_in',
                              ip=ip, username=user.username)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_logged_out',
                              ip=ip, username=user.username)


@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    AuditEntry.objects.create(
        action='user_login_failed', username=credentials.get('username', None))
