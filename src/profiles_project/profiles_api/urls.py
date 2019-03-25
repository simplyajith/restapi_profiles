from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^hello-view/',views.HelloApiView.as_view())

]


