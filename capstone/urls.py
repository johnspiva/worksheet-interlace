from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Pastebin API')
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('ws_interlace.urls')),
    url('^schema/$', schema_view),
]
