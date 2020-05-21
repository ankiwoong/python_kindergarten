from django.contrib import admin
from blog.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']           # 제목으로 검색
    list_per_page = 5                   # 한 페이지에 보이는 갯수
    list_display = ('id', 'title', 'content', 'createDate',
                    'updateDate')       # 페이지에 보이는 내용
    list_filter = ('category', )        # 필터링 작업

    # 레이아웃
    fieldsets = [
        ('기본 정보', {'fields': (('title', 'content',))}),
        ('카테고리', {'fields': ['category']}),
        ('날짜', {'fields': ['createDate']}),
    ]


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
