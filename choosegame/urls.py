
from django.conf.urls import url
from django.contrib import admin

from core.views import HomeView, LoginView, LogoutView, LikeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^like/', LikeView.as_view(), name='like'),
]
