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
from django.contrib.auth import views as auth_views
from django.conf.urls import handler400, handler403, handler404, handler500


# http://localhost:8000/ => http://localhost:8000/blog
urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls")),
    path("", RedirectView.as_view(url="/blog/", permanent=True)),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),
         name='logout', kwargs={'next_page': '/'}),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)     # staic 정적 파일 처리
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)     # media 정적 파일 처리

handler400 = 'blog.views.error400'
handler403 = 'blog.views.error403'
handler404 = 'blog.views.error404'
handler500 = 'blog.views.error500'
