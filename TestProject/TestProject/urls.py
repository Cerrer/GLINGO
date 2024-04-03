from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appKey.urls')),
    path('api/', include('appApi.urls')),
    path('auth/', include('appAuth.urls')),
    path('shop/', include('appShop.urls')),
    path('method_auth/', include('appMethodAuth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('render/', include('appRenderHtml.urls')),
]
print(path('render/', include('appRenderHtml.urls')))
print(include('appRenderHtml.urls'))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)