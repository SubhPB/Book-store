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

    # books app
    path('books/', include('books.urls')),

    # ordes app
    path('orders/', include('orders.urls')),
] 

if settings.DEBUG:
    import debug_toolbar

    static_urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    debug_urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ]

    urlpatterns = urlpatterns + static_urlpatterns + debug_urlpatterns