from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Invoice, Receipt
from django.contrib.auth.mixins import LoginRequiredMixin


# User Dashboard View
class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'billing/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Get all invoices and receipts for the logged-in user
        context['invoices'] = Invoice.objects.filter(user=user)
        context['receipts'] = Receipt.objects.filter(invoice__user=user)
        return context


# User Invoices List View
class UserInvoicesView(LoginRequiredMixin, ListView):
    model = Invoice
    template_name = 'billing/invoices_list.html'
    context_object_name = 'invoices'

    def get_queryset(self):
        # Only show invoices belonging to the logged-in user
        return Invoice.objects.filter(user=self.request.user)


# User Receipts List View
class UserReceiptsView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = 'billing/receipts_list.html'
    context_object_name = 'receipts'

    def get_queryset(self):
        # Only show receipts related to the invoices of the logged-in user
        return Receipt.objects.filter(invoice__user=self.request.user)