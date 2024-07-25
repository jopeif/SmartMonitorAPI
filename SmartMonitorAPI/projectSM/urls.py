from appSM.views import *
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token



schema_view = get_schema_view(
    openapi.Info(
        title="Smart Monitor API",
        default_version='',
        description="",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloWord.as_view()),
    path('statistic/', Statis_Analys.as_view()),
    path('RandomForest/', Pred_RandomForest.as_view()),

    path('token/', obtain_auth_token, name='api_token_auth'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('poste/',Exemplo.as_view())
]
