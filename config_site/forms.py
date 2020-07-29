from django import forms


from .models import Config


OP_MODE_CHOICES = [
    ('0', 'Gateway'),
    ('1', 'Roteador'),
]

class ConfigForm(forms.Form):
    op_mode = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=OP_MODE_CHOICES,
