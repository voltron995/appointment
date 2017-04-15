from django.conf.urls import url, include
from appointments_manager import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  url(r'^appointments', views.AppointmentList.as_view(), name='appointments'),
  url(r'^appointment/(?P<pk>\d+)/appointments', views.AppointmentList.as_view(), name='appointments'),
  url(r'^appointment/(?P<pk>\d+)/$', views.AppointmentDetail.as_view(), name='appointment_details'),
  url(r'^appointment_new/$', views.AppointentCreate.as_view(), name='appointment_new'),
  url(r'^appointment_edit/(?P<pk>\d+)/$', views.AppointmentUpdate.as_view(), name='appointment_edit'),
  url(r'^appointment_delete/(?P<pk>\d+)/$', views.AppointmentDelete.as_view(), name='appointment_delete'),
  url(r'^appointment/(?P<pk>\d+)/visitor_new$', views.VisitorCreate.as_view(), name='visitor_new'),
  # url(r'^appointment/(?P<pk1>\d+)/visitor_details/(?P<pk2>\d+)$', views.VisitortDetail.as_view(), name='visitor_details'),
  url(r'^timerange_new$', views.TimeRangesCreate.as_view(), name='timerange_new'),
  url(r'^api/$', views.AppList.as_view()),
  url(r'^api/(?P<pk>[0-9]+)/$', views.AppDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)