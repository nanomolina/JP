"""odontology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from core import views

handler404 = views.error404

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('landing.urls', namespace='landing')),
    url(r'^core/', include('core.urls', namespace='core')),
    url(r'^persons/', include('person.urls', namespace='person')),
    url(r'^register/', include('register.urls', namespace='register')),
    url(r'^accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
