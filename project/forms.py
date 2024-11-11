from django import forms
from .models import Project, ProjectProgress, Feedback
from django.contrib.auth.models import User, Group

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'assigned_to', 'start_date', 'end_date', 'status', 'documentation']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        client_group = Group.objects.get(name='default')
        self.fields['assigned_to'].queryset = User.objects.filter(groups=client_group)
class ProjectProgressForm(forms.ModelForm):
    class Meta:
        model = ProjectProgress
        fields = ['status_update', 'progress_percentage', 'description']

        def clean_progress_percentage(self):
            progress_percentage = self.cleaned_data.get('progress_percentage')
            if not (0 <= progress_percentage <= 100):
                raise forms.ValidationError("Progress percentage must be between 0 and 100.")
            return progress_percentage

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']
