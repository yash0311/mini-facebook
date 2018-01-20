from django.conf.urls import url
from home.views import HomeView,change_friend,message_to_friend
urlpatterns = [
    url(r'^$',HomeView.as_view(),name='home'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$',change_friend, name='change_friend'),
    url(r'^message/$', message_to_friend, name='message_to_friend')
    ]
