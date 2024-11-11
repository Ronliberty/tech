from django.urls import path
from .views import ExpertsCreateView, ExpertListView, ExpertRequestCreateView, ExpertRequestSuccessView, ExperteRequestListView

app_name = 'hire'
urlpatterns = [
    path('experts/create/', ExpertsCreateView.as_view(), name='experts-create'),
    path('expert-list/', ExpertListView.as_view(), name='expert-list'),
    path('request-expert/', ExpertRequestCreateView.as_view(), name='request-expert'),
    path('expert-request-success/', ExpertRequestSuccessView.as_view(), name='expert-request-success'),
    path('expert-request-list/', ExperteRequestListView.as_view(), name='expert-request-list'),
]
