"""URL_SHORTNER URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from testapp import views
from testapp.API.views import Generate_Short_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.URL_SHORTNER_VIEW,name ='home'),
    path('results/', views.URL_SHORTNER_VIEW,name ='result'),
    path('about/', views.About_us,name ='about'),
    path('apidoc/', views.API,name ='api'),
    path('api/', Generate_Short_URL.as_view()),
    path('<hidden_url>/', views.Redirect,name ='redirect'),
]
