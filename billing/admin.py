from django.contrib import admin
from .models import Invoice, Receipt

# Invoice Model Admin
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'description', 'amount_due', 'due_date', 'payment_method', 'is_paid', 'created_at')
    list_filter = ('payment_method', 'is_paid', 'due_date', 'user')
    search_fields = ('user__username', 'description')
    list_editable = ('is_paid',)  # Allow editing the "is_paid" field directly from the list view
    ordering = ['-due_date']
    readonly_fields = ('created_at',)  # Set created_at as read-only

    # Optionally, you can customize the form layout for better usability
    fieldsets = (
        (None, {
            'fields': ('user', 'description', 'amount_due', 'due_date', 'payment_method', 'is_paid')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # Optional: collapsible section for timestamps
        }),
    )

# Receipt Model Admin
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'payment_date', 'payment_reference', 'amount_paid', 'created_at')
    list_filter = ('payment_date', 'invoice__user')
    search_fields = ('invoice__id', 'payment_reference')
    readonly_fields = ('created_at',)  # Set created_at as read-only

    # Optionally, you can customize the form layout for better usability
    fieldsets = (
        (None, {
            'fields': ('invoice', 'payment_date', 'payment_reference', 'amount_paid')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # Optional: collapsible section for timestamps
        }),
    )

# Register the models with their custom admin configurations
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Receipt, ReceiptAdmin)