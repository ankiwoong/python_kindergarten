"""anjia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # 주소창에 blog를 입력시 blog.urls가 처리
    path('blog/', include('blog.urls')),
    # 기본주소로 처리시 blog로 넘겨준다.
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)     # 정적 파일 처리
