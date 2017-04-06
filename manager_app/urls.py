from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from appointments_manager.views import AppointmentList, AppointmentDelete, AppointmentDetail, AppointentCreate, AppointmentUpdate, VisitorCreate, TimeRangesCreate

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', AppointmentList.as_view(), name='appointments'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),
    url(r'^appointments', AppointmentList.as_view(), name='appointments'),
    url(r'^appointment/(?P<pk>\d+)/$', AppointmentDetail.as_view(), name='appointment_details'),
    url(r'^appointment_new$', AppointentCreate.as_view(), name='appointment_new'),
    url(r'^appointment_edit/(?P<pk>\d+)/$', AppointmentUpdate.as_view(), name='appointment_edit'),
    url(r'^appointment_delete/(?P<pk>\d+)/$', AppointmentDelete.as_view(), name='appointment_delete'),
    url(r'^visitor_new$', VisitorCreate.as_view(), name='visitor_new'),
    url(r'^timerange_new$', TimeRangesCreate.as_view(), name='timerange_new'),

]
