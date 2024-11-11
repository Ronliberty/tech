from django import forms
from .models import Service, ServiceImage, ServiceRequest

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'sample_website']

class ServiceImageForm(forms.ModelForm):
    class Meta:
        model = ServiceImage
        fields = ['image']


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service', 'additional_details']
        widgets = {
            'service': forms.Select(attrs={
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