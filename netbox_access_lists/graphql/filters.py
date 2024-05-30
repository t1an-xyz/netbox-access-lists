import strawberry
import strawberry_django
from .. import filtersets, models
from netbox.graphql.filter_mixins import autotype_decorator, BaseFilterMixin

__all__ = (
    'AccessListRuleFilter'
)

@strawberry_django.filter(models.AccessListRule, lookups=True)
@autotype_decorator(filtersets.AccessListRuleFilterSet)
class AccessListRuleFilter(BaseFilterMixin):
    pass