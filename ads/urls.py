from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from rest_framework.authtoken import views
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from ads.views import LocationViewSet, CategoryViewSet, AdViewSet, index, UserViewSet, SelectionViewSet
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register(r'location', LocationViewSet)
router.register(r'cat', CategoryViewSet)
router.register(r'user', UserViewSet)
router.register(r'ad', AdViewSet)
router.register(r'selection', SelectionViewSet)


urlpatterns = [
    path("", index),

    path('login/', views.obtain_auth_token),
    # path('logout/', Logout.as_view()),
    path("", include(router.urls)),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
