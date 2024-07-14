from django.contrib import admin
from .models import *

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'owner', 'client', 'dev', 'type', 'date', 'amount_in_uzs', 'amount_in_usd', 'amount_out_uzs', 'amount_out_usd')
    list_filter = ('date', 'owner', 'dev', 'client')
    date_hierarchy = 'date'
    search_fields = ('comment',)

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
            total_amount_in_uzs = qs.aggregate(total=models.Sum('amount_in_uzs'))['total'] or 0
            total_amount_out_uzs = qs.aggregate(total=models.Sum('amount_out_uzs'))['total'] or 0
            total_amount_in_usd = qs.aggregate(total=models.Sum('amount_in_usd'))['total'] or 0
            total_amount_out_usd = qs.aggregate(total=models.Sum('amount_out_usd'))['total'] or 0
            response.context_data['summary'] = {
                'total_amount_in_uzs': total_amount_in_uzs,
                'total_amount_out_uzs': total_amount_out_uzs,
                'total_amount_in_usd': total_amount_in_usd,
                'total_amount_out_usd': total_amount_out_usd,
            }
        except (AttributeError, KeyError):
            pass

        return response

    def get_changelist_instance(self, request):
        self.change_list_template = 'change_list_summary.html'
        return super().get_changelist_instance(request)
