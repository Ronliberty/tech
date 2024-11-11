from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from .models import Project, ProjectProgress, Feedback
from .forms import ProjectForm, ProjectProgressForm, FeedbackForm
from django.urls import reverse
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        manager_group = Group.objects.get(name='Manager')

        return Project.objects.filter(
            assigned_to=self.request.user,
            user__groups=manager_group
        ).select_related('user')

    def render_to_response(self, context, **kwargs):
        # Check if the request is AJAX by inspecting the 'X-Requested-With' header
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            html = render_to_string(
                'project/project_list.html', context, request=self.request)
            return JsonResponse({'html': html})
        return super().render_to_response(context, **kwargs)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project:project-detail', kwargs={'pk': self.object.pk})

class ProjectOngoingView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project/ongoing_projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        # Show all projects associated with the user (e.g., if the user is the creator of the project)
        return Project.objects.filter(user=self.request.user)

class ProjectProgressUpdateView(LoginRequiredMixin, UpdateView):
    model = ProjectProgress
    form_class = ProjectProgressForm
    template_name = 'project/progress_form.html'

    def get_queryset(self):
        return ProjectProgress.objects.filter(project__user=self.request.user)

    def get_success_url(self):
        # Redirect to the project detail page after updating progress
        return reverse_lazy('project:project-detail', kwargs={'pk': self.object.project.id})





class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'project/feedback_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = get_object_or_404(Project, id=self.kwargs['pk'])
        return super().form_valid(form)

class ProjectHistoryView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project/project_history.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Loop over the projects to fetch progress entries
        for project in context['projects']:
            project.progress_entries_list = project.progress_entries.all()  # Use a new attribute to store the entries

        return context
