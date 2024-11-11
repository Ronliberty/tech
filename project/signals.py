from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Project, ProjectProgress

@receiver(post_save, sender=Project)
def create_initial_project_progress(sender, instance, created, **kwargs):
    if created:
        ProjectProgress.objects.create(
            project=instance,
            status_update="Project started",
            progress_percentage=0,
            user=instance.user  # Assuming the creator is the user
        )
