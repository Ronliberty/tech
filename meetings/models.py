# meetings/models.py
from django.db import models
from django.contrib.auth.models import User

class MeetingRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    request_date = models.DateTimeField(auto_now_add=True)
    feedback_url = models.URLField(blank=True, null=True)
    meeting_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, default="Pending")  # Options: Pending, Approved, etc.

    def __str__(self):
        return f"{self.subject} - {self.user.username}"
class Meeting(models.Model):
    meeting_request = models.OneToOneField(MeetingRequest, on_delete=models.CASCADE, related_name='meeting')
    feedback = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField()  # Date and time of the meeting

    def __str__(self):
        return f"Meeting for {self.meeting_request.subject} - {self.meeting_request.user.username}"