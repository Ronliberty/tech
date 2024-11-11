# meetings/forms.py
from django import forms
from .models import MeetingRequest

class MeetingRequestForm(forms.ModelForm):
    class Meta:
        model = MeetingRequest
        fields = ['subject', 'description']
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; padding: 10px; margin-top: 20px; margin-bottom: 20px; border-radius: 5px;',
                'placeholder': 'Enter subject of the meeting'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 150px; padding: 10px; margin-top: 20px; margin-bottom: 20px; border-radius: 5px;',
                'placeholder': 'Provide a description of the meeting'
            })
        }


class MeetingFeedbackForm(forms.ModelForm):
    class Meta:
        model = MeetingRequest
        fields = ['feedback_url', 'meeting_time']
        widgets = {
            'feedback_url': forms.URLInput(attrs={'placeholder': 'Enter feedback URL'}),
            'meeting_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }