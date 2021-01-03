from django.urls import include, path
from rest_framework import routers
from .supplier import views as supplier_views
from .auth import views as auth_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Green Mile Api",
        default_version='v1',
        terms_of_service="#",
        contact=openapi.Contact(email="me@iamafasha.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("auth/login", auth_views.LoginView.as_view(), name="user-login"),
    path('sandbox/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('suppliers', supplier_views.SupplierViewSet.as_view({'post':'create'}), name="create-supplier" ),
]