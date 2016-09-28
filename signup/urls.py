from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.signup, name='signup-index'),
    url(r'^confirm$', views.confirm_token, name='confirm_token'),
    url(r'^success$', views.success, name='signup_success'),
]
