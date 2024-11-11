from django.shortcuts import render
from .forms import ExpertForm, ExpertImageForm, ExpertRequestForm
from django.http import JsonResponse
from .models import OurExperts, ExpertImage, ExpertRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, TemplateView
from django.forms import modelformset_factory
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
class ExpertsCreateView(LoginRequiredMixin, CreateView):
    model = OurExperts
    form_class = ExpertForm
    template_name = 'hire/create_expert.html'
    success_url = reverse_lazy('hire:expert-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        ImageFormset = modelformset_factory(ExpertImage, form=ExpertImageForm, extra=3)
        if self.request.POST:
            data['image_formset'] = modelformset_factory(ExpertImage, form=ExpertImageForm, extra=3)(self.request.POST, self.request.FILES, queryset=ExpertImage.objects.none())
        else:
            data['image_formset'] = modelformset_factory(ExpertImage, form=ExpertImageForm, extra=3)(queryset=ExpertImage.objects.none())
        return data

    def form_valid(self, form):
        # Set the created_by user to the currently logged-in user
        form.instance.created_by = self.request.user
        self.object = form.save()

        context = self.get_context_data()
        image_formset = context['image_formset']

        if image_formset.is_valid():
            for image_form in image_formset:
                if image_form.cleaned_data:
                    image_instance = image_form.save(commit=False)
                    image_instance.expert = self.object
                    image_instance.save()
        else:
            return self.form_invalid(form)

        return redirect(self.success_url)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

class ExpertListView(LoginRequiredMixin, ListView):
    model = OurExperts
    template_name = 'hire/expert_list.html'
    context_object_name = 'expert'

    # Remove AJAX logic for now to focus on normal rendering
    def get(self, request, *args, **kwargs):
        # Just render the normal page
        return super().get(request, *args, **kwargs)

class ExpertRequestCreateView(LoginRequiredMixin, CreateView):
    model = ExpertRequest
    form_class = ExpertRequestForm
    template_name = 'hire/request_expert.html'
    success_url = reverse_lazy('hire:expert-request-success')  # Redirect after successful submission

    def form_valid(self, form):
        form.instance.requested_by = self.request.user

        return super().form_valid(form)

    def form_invalid(self, form):

        return super().form_invalid(form)

class ExpertRequestSuccessView(TemplateView):
    template_name = 'hire/request_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Your service request has been successfully submitted!'
        return context

class ExperteRequestListView(TemplateView):
    template_name = 'hire/request.html'

    def get_context_data(self, **kwargs):
        expert_request = ExpertRequest.objects.all()

        context = super().get_context_data(**kwargs)
        context['expert_requests'] = expert_request
        return context


