from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PlayView.as_view(), name='play'),
    url(r'^api/', views.APIView.as_view(), name='api'),
]