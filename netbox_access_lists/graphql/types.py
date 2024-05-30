from typing import Annotated
import strawberry
import strawberry_django
from netbox.graphql.types import NetBoxObjectType
from .. import models
from . import filters

@strawberry_django.type(
    models.AccessList,
    fields='__all__',
)
class AccessListType(NetBoxObjectType):
    id: int
    name: str
    default_action: str
    rules: list[Annotated["AccessListRuleType", strawberry.lazy('netbox_access_lists.graphql.types')]]
    comments: str

@strawberry_django.type(
    models.AccessListRule,
    fields='__all__',
    filters=filters.AccessListRuleFilter
)
class AccessListRuleType:
    id: int
    index: int
    access_list: Annotated["AccessListType", strawberry.lazy('netbox_access_lists.graphql.types')]
    protocol: str
    source_prefix: Annotated["PrefixType", strawberry.lazy('ipam.graphql.types')]
    source_ports: list[int]
    destination_prefix: Annotated["PrefixType", strawberry.lazy('ipam.graphql.types')]
    destination_ports: list[int]
    action: str
    description: str