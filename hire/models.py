from django.db import models
from django.contrib.auth.models import User


class OurExperts(models.Model):
    names = models.CharField(max_length=255, blank=True, null=True)
    portfolio = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.names or "No name provided"

class ExpertImage(models.Model):
    expert = models.ForeignKey(OurExperts, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='expert_images/')

    def __str__(self):
        return f"Image for {self.expert.names}"


class ExpertRequest(models.Model):
    expert = models.ForeignKey(OurExperts, on_delete=models.CASCADE, related_name='requests')
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Expert_requests')
    additional_details = models.TextField(blank=True, null=True, verbose_name="Description")
    requested_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Request for {self.expert.title} by {self.requested_by.username}"