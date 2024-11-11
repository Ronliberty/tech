# meetings/urls.py
from django.urls import path
from .views import MeetingRequestCreateView, MeetingRequestListView, MeetingFeedbackUpdateView, MeetingRequestSuccessView, MeetingFeedbackDetailView

app_name = 'meetings'
urlpatterns = [
    path('request/', MeetingRequestCreateView.as_view(), name='request_meeting'),
    path('requests/', MeetingRequestListView.as_view(), name='meeting_requests_list'),
    path('provide-feedback/<int:pk>/', MeetingFeedbackUpdateView.as_view(), name='provide_feedback'),
    path('meeting-request-success/', MeetingRequestSuccessView.as_view(), name='meeting-request-success'),
    path('feedback/<int:pk>/', MeetingFeedbackDetailView.as_view(), name='meeting_feedback_detail'),
]
