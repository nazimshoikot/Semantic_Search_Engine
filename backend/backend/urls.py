"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework import routers                   
from docs import views as docsView 
# import ..docs.views as docView              
# from emails import views as emailsView                       

router = routers.DefaultRouter()                     
router.register(r'docs', docsView.docsView, 'doc')     
# router.register(r'new', docsView.new, 'new')     

# router.register(r'emails', emailsView.emailsView, 'email')     

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)), 
    path('api/docs/', docsView.docsView.as_view()), 
    # path('new/', docsView.runModel), 
    # path('new/', docsView.new)  
    # url(r'/path/to/API/', include((router.urls, 'my_app_name'), namespace='widget-api'),
]
