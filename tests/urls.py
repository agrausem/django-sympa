try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^users.sympa$', 'sympa.views.users', name='sympa-users')
)
