from django.conf.urls import url

from django.contrib.auth.views import (
    login,logout,password_reset_complete,password_reset_done,
    password_reset_confirm,password_reset
)
from .views import register,profile,profile_edit,change_password
#add urls for all apps
urlpatterns = [

    url(r'^login/$', login,{'template_name':"accounts/login.html"},name='login'),
    url(r'^logout/$', logout,{'template_name':"accounts/logout.html"},name='logout'),
    url(r'^register/$', register,name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^profile/(?P<pk>\d+)/$', profile, name='view_profile_with_pk'),
    url(r'^profile/edit/$', profile_edit, name='profile_edit'),
    url(r'^change-password/$', change_password, name='change_password'),
    url(r'^reset-password/$',password_reset,{'template_name':
        "accounts/reset_password.html","post_reset_redirect":"accounts:password_reset_done",
                                             'email_template_name':"accounts/reset_password_email.html"},
        name='reset_password'),

    url(r'^reset-password/done/$', password_reset_done,{'template_name':'accounts/reset_password_done.html'}
        ,name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'template_name':"accounts/reset_password_confirm.html",
         'post_reset_redirect':'accounts:password_reset_complete'},name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete,{'template_name':
        "accounts/reset_password_complete.html",} ,name='password_reset_complete')
]
