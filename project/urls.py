from django.urls import path
from .views import (
    ProjectListView, ProjectDetailView, ProjectCreateView,
    ProjectProgressUpdateView, FeedbackCreateView, ProjectHistoryView, ProjectOngoingView
)
app_name = 'project'
urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('ongoing/', ProjectOngoingView.as_view(), name='project_ongoing'),
    path('project/<int:pk>/progress/', ProjectProgressUpdateView.as_view(), name='project-progress-update'),
    path('project/<int:pk>/feedback/', FeedbackCreateView.as_view(), name='feedback-create'),
    path('project/history/', ProjectHistoryView.as_view(), name='project-history'),
]
