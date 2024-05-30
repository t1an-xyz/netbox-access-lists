import django_filters
from netbox.filtersets import NetBoxModelFilterSet
from .models import AccessListRule, AccessList
from django.db.models import Q, Count

class AccessListRuleFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = AccessListRule
        fields = ('id', 'access_list', 'index', 'protocol', 'action')
    
    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)

class AccessListFilterSet(NetBoxModelFilterSet):
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact')
    default_action = django_filters.CharFilter(field_name='default_action', lookup_expr='exact')
    rule_count = django_filters.RangeFilter(method='filter_rule_count')

    class Meta:
        model = AccessList
        fields = ('id', 'default_action', 'rule_count')
    
    def filter_rule_count(self, queryset, name, value):
        queryset = queryset.annotate(rule_count=Count('rules'))
        if value.start is not None:
            queryset = queryset.filter(rule_count__gte=value.start)
        if value.stop is not None:
            queryset.filter(rule_count__lte=value.stop)
        return queryset
    
    def search(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(comments__icontains=value))
        