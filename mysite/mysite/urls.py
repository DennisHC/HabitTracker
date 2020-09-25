"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import include, path

# My Files
from . import views
from habits import views as habits_views
from users import views as user_views
from user_profiles import views as user_profiles_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.myhomepage, name='homepage'),
    path('habits/', include('habits.urls')),
    path('success', views.success, name='success'),
    path('about_us', views.about_us, name='about_us'),
    path('features', views.features, name='features'),

    path('create_account', user_views.create_account, name='create_account'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
    path('my_habits/', user_views.my_habits, name='my_habits'),

    path('api/', include('api.urls')),

    path('password_reset', user_views.password_reset, name='password_reset'),

    path('profile/', user_views.profile, name='profile'),
    # path('profile/', include('user_profiles.urls')),
]
