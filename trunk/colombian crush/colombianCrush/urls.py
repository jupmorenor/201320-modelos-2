from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('colombianCrush.views',
    # Examples:
    # url(r'^$', 'prueba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'inicio'),
    url(r'^game/$', 'juego'),
    url(r'^fin/$', 'fin'),
)