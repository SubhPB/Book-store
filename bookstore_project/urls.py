# Byimaan 

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# static_url_patterns = static(
#     settings.STATIC_URL,
#     document_root=settings.STATIC_ROOT
# )

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')),

    # Local apps
    # path('accounts/', include('users.urls')),
    path('', include('pages.urls')),
]  