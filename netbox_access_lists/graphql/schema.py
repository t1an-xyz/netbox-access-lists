import strawberry
import strawberry_django
from typing import Annotated
from .. import models
from .types import AccessListType, AccessListRuleType

@strawberry.type
class Query:
    @strawberry.field
    def accesslist(self, id: int) -> AccessListType:
        return models.AccessList.objects.get(pk=id)
    accesslist_list: list[AccessListType] = strawberry_django.field()

    @strawberry.field
    def accesslistrule(self, id: int) -> AccessListRuleType:
        return models.AccessListRule.objects.get(pk=id)
    accesslistrule_list: list[AccessListRuleType] = strawberry_django.field()
    
schema = [
    Query
]