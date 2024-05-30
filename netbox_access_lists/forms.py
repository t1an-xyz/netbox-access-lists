from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from .models import AccessList, AccessListRule, ActionChoices, ProtocolChoices
from utilities.forms.fields import CommentField, DynamicModelChoiceField, TagFilterField
from utilities.forms.rendering import FieldSet, InlineFields

class AccessListForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = AccessList
        fields = ('name', 'default_action', 'comments', 'tags')

class AccessListRuleForm(NetBoxModelForm):
    access_list = DynamicModelChoiceField(
        queryset=AccessList.objects.all()
    )
    source_prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all(),
        required=False
    )
    destination_prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all(),
        required=False
    )

    class Meta:
        model = AccessListRule
        fields = (
            'access_list', 'index', 'description', 'source_prefix', 'source_ports', 'destination_prefix',
            'destination_ports', 'protocol', 'action', 'tags',
        )

class AccessListRuleFilterForm(NetBoxModelFilterSetForm):
    model = AccessListRule

    access_list = forms.ModelMultipleChoiceField(
        queryset=AccessList.objects.all(),
        required=False
    )
    index = forms.IntegerField(required=False)
    protocol = forms.MultipleChoiceField(
        choices = ProtocolChoices,
        required=False
    )
    action = forms.MultipleChoiceField(
        choices = ActionChoices,
        required=False
    )

class AccessListFilterForm(NetBoxModelFilterSetForm):
    model = AccessList

    tag = TagFilterField(model)
    default_action = forms.MultipleChoiceField(
        choices = ActionChoices,
        required=False
    )
    rule_count_min = forms.IntegerField(
        label='Min',
        required=False
    )
    rule_count_max = forms.IntegerField(
        label='Max',
        required=False
    )
    fieldsets = (
        FieldSet('filter_id', 'q'),
        FieldSet('default_action', InlineFields('rule_count_min', 'rule_count_max', label='Rule Count')),
    )