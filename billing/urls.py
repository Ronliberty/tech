from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    # URL for user dashboard
    path('dashboard/', views.UserDashboardView.as_view(), name='dashboard'),

    # URL to view all invoices
    path('invoices/', views.UserInvoicesView.as_view(), name='invoices'),

    # URL to view all receipts
    path('receipts/', views.UserReceiptsView.as_view(), name='receipts'),
]