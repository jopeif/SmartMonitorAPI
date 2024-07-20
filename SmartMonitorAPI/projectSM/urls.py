from django.contrib import admin
from django.urls import path

from appSM import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authentication import TokenAuthentication

schema_view = get_schema_view(
   openapi.Info(
      title="Smart Monitor API",    
      default_version='',
      description="",
      terms_of_service="",
      contact=openapi.Contact(""),
      license=openapi.License(""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(permissions.TokenAuthentication,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', views.helloword),

    path('token/', obtain_auth_token, name='token'),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
