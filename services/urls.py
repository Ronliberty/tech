from django.urls import path
from .views import ServiceCreateView, ServiceListView, ServiceRequestCreateView, ServiceRequestSuccessView

app_name = 'services'
urlpatterns = [
    path('service/create/', ServiceCreateView.as_view(), name='service-create'),
    path('service-list/', ServiceListView.as_view(), name='service-list'),
    path('request-service/', ServiceRequestCreateView.as_view(), name='request-service'),
    path('service-request-success/', ServiceRequestSuccessView.as_view(), name='service-request-success'),
]
