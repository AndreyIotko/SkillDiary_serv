"""SkillDiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from task_app.views import TaskList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users_app.urls', namespace='users')),
    path('', include('courseapp.urls', namespace='course')),
    path('api/', include('api_app.urls')),
    path('course/<int:pk>/', include('task_app.urls', namespace='tasks')),
    path('task_daily/', TaskList.as_view(), name='task_daily' ),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


