from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from books import views
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.defaults import *
#from django.views.generic.simple  import direct_to_template

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xuyuan.views.home', name='home'),
    # url(r'^xuyuan/', include('xuyuan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^hello/', views.hello),
     url(r'^ua_display/', views.ua_display),
#     url(r'^search-form/$',views.search_form),
#     url(r'^search/$',views.search),
     url(r'^contact/$',views.contact),
#     url(r'^about/$',direct_to_template,{'template':'about.html'}),
     #url(r'about/(\w+)/$',about_pages),
     url(r'^polls/',include('polls.urls')),
)
