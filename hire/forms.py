from django import forms
from .models import OurExperts, ExpertImage, ExpertRequest


class ExpertForm(forms.ModelForm):
    class Meta:
        model = OurExperts
        fields = ['names', 'portfolio', 'email', 'social_links', 'phone_number']

class ExpertImageForm(forms.ModelForm):
    class Meta:
        model = ExpertImage
        fields = ['image']

class ExpertRequestForm(forms.ModelForm):
    class Meta:
        model = ExpertRequest
        fields = ['expert', 'additional_details']
        widgets = {
            'expert': forms.Select(attrs={
                'class': 'form-select',
                'style': 'width:100%; padding:10px; border-radius:5px; margin-top: 15px; margin-bottom: 15px;'
            }),
            'additional_details': forms.Textarea(attrs={
                'placeholder': 'Provide additional details about your request',
                'class': 'form-textarea',
                'rows': 5,
                'style': 'width:100%; padding:10px; margin-top: 15px; margin-bottom: 15px; border-radius:5px; resize: vertical;'
            }),
        }