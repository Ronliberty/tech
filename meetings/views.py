from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MeetingRequest, Meeting
from .forms import MeetingRequestForm, MeetingFeedbackForm

# View for creating a meeting request
class MeetingRequestCreateView(LoginRequiredMixin, CreateView):
    model = MeetingRequest
    form_class = MeetingRequestForm
    template_name = 'meetings/request_meeting.html'
    success_url = reverse_lazy('meetings:meeting-request-success')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user to the logged-in user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Example of accessing meetings related to the user
        context['user_meetings'] = Meeting.objects.filter(meeting_request__user=self.request.user)
        return context
class MeetingRequestSuccessView(TemplateView):
    template_name = 'meetings/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Your meeting request has been successfully submitted!'
        return context

class MeetingRequestListView(LoginRequiredMixin, ListView):
    model = MeetingRequest
    template_name = 'meetings/meeting_requests_list.html'
    context_object_name = 'meeting_requests'


class MeetingFeedbackUpdateView(LoginRequiredMixin, UpdateView):
    model = MeetingRequest
    form_class = MeetingFeedbackForm
    template_name = 'meetings/provide_feedback.html'
    success_url = reverse_lazy('meetings:meeting_requests_list')

    def form_valid(self, form):
        form.instance.status = "Approved"
        return super().form_valid(form)

class MeetingFeedbackDetailView(LoginRequiredMixin, DetailView):
    model = MeetingRequest
    template_name = 'meetings/meeting_feedback_detail.html'
    context_object_name = 'meeting'

    def test_func(self):
        # Allow access if the logged-in user is the one who made the request or if the user is an admin
        meeting = self.get_object()
        return self.request.user == meeting.user or self.request.user.is_staff