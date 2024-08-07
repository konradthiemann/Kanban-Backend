"""
URL configuration for kanbanBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from todo.views import TodoViewSet, CategoryViewSet, UserViewSet, search_tasks, RegisterUserView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # POST JSON with "username" & "password"
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # POST JSON with "refresh":"refreshToken"
    path('tasks/search/', search_tasks, name='search_tasks'), # GET with query string "q" /tasks/search/?q=searchString
    path('', include(router.urls)),
    path('register/', RegisterUserView.as_view(), name='register'),
    # path('api/auth/', include('rest_framework.urls')), # For login/logout views
]
