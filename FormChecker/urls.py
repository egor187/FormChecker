from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

import debug_toolbar

from .views import FormTemplateAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('get_form/', FormTemplateAPIView.as_view(), name="form")
]