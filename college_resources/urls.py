# college_resources/urls.py
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from resources.views import home_view  # Adjust 'your_app' to the actual app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Define a URL pattern for the home view
    path('resources/', include('resources.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

