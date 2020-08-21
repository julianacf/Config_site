from django import forms
from .models import Config_device
from django.utils.translation import ugettext_lazy as _


class ConfigForm(forms.ModelForm):
    class Meta:
        model = Config_device
        fields = [
        "connect_choice",
        "op_mode",
        "ip_adress",
        "mask_adress",
        "gateway_adress",
        ]
        labels = {
        "connect_choice":_("Tipo de Conexão"),
        "op_mode":_("Modo de Operação"),
        "ip_adress":_("Endereço IP"),
        "mask_adress":_("Máscara de sub-rede"),
        "gateway_adress":_("Gateway"),
        }
