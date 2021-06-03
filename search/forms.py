from django.forms import Form, ChoiceField, CharField
from common.variables import CARS_LIST, ENGINE_TYPES, COLOR_CHOICES

class FilterForm(Form):
    search = CharField(required=False)
    filter_field_1 = ChoiceField(choices=CARS_LIST, required=False)
