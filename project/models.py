from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_projects', default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    status_choices = [
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('ON_HOLD', 'On Hold'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='IN_PROGRESS')
    documentation = models.FileField(upload_to='documents/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProjectProgress(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='progress_entries')
    status_update = models.TextField()
    progress_percentage = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User making the update
    update_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-update_date']  # Orders progress entries by most recent first.

    def __str__(self):
        return f"{self.project.title} - {self.progress_percentage}%"

    def clean(self):
        """ Ensure progress_percentage is between 0 and 100. """
        if not (0 <= self.progress_percentage <= 100):
            raise ValidationError('Progress percentage must be between 0 and 100.')

class Feedback(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='feedback_entries')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User providing feedback
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback on {self.project.title} by {self.user.username}"
