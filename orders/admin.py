from django.contrib import admin

from .models import Order, OrderItem,SaleSummary
from django.db.models import Count,Sum,Min,Max
from django.db.models.functions import Trunc
from django.db.models import DateTimeField



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

def get_next_in_date_hierarchy(request, date_hierarchy):
    if date_hierarchy + '__day' in request.GET:
        return 'hour'
    if date_hierarchy + '__month' in request.GET:
        return 'day'
    if date_hierarchy + '__year' in request.GET:
        return 'month'
    return 'month'

admin.site.register(Order, OrderAdmin)

# @admin.register(SaleSummary)
class SaleSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'orders/admin/sale_summary_change_list.html'
    date_hierarchy = 'order_id__created'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        print(list(qs.values('order_id__paid')))
        if list(qs.values_list('order_id__paid'))[0][0]:
            print(123)
        metrics = {
        'total': Count('id'),
        'total_sales': Sum('price'),
        }
        response.context_data['summary_total'] = dict(qs.aggregate(**metrics))

        response.context_data['summary'] = list(
            qs
                .values('product_id__category_id__name')
        .annotate(**metrics)
            .order_by('-total_sales')
        )
        print(response.context_data['summary'])
        print(response.context_data['summary_total'])
        period = get_next_in_date_hierarchy(
            request,
            self.date_hierarchy,
        )
        response.context_data['period'] = period
        summary_over_time = qs.annotate(
            period=Trunc(
                'order_id__created',
                period,
                output_field=DateTimeField(),
            ),
        ).values('period').annotate(total=Count('price')).order_by('period')

        print(summary_over_time,"ee")
        summary_range = summary_over_time.aggregate(
            sum=Sum('total'),

        )
        print(summary_range,"hj")
        sum = summary_range.get('sum', 0)

        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'pct': \
                ((x['total'] or 0) ) / sum * 100
        } for x in summary_over_time]
        print( response.context_data['summary_over_time'],"ggg")
        return response


admin.site.register(SaleSummary, SaleSummaryAdmin)