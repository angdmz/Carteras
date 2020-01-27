"""Carteras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include  # This needs to be added
from rest_framework import permissions, routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest.views import ClientViewSet, PortfoliosViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Portfolios API",
      default_version='v1',
      description="Portfolios administration",
      contact=openapi.Contact(email="agustindorda@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'portfolios', PortfoliosViewSet)

urlpatterns = [
    url(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
