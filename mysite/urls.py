# mysite/urls.py

from django.contrib import admin
from django.urls import path, include  # <-- Make sure you have both of these imports.

urlpatterns = [
    path('', include('blogging.urls')),  # <-- this didn't seem to work
    path('polling/', include('polling.urls')),  # <-- Add this
    path('blogging/', include('blogging.urls')),  # <-- I added this too
    path('admin/', admin.site.urls),
]

