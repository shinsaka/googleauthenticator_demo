from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('common.urls')),
    url(r'^signup/', include('signup.urls')),
    url(r'^admin/', admin.site.urls),
]
