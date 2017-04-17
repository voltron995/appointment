from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from appointments_manager.views import AppointmentList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', AppointmentList.as_view(), name='appointments'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^appointmnent/', include('appointments_manager.urls'))

]
