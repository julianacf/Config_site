from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from macaddress.fields import MACAddressField


class Config_device(models.Model):
    Connect_Choices = (
        ('0', 'IP Estático'),
        ('1', 'IP Dinâmico'),
    )
    connect_choice = models.CharField(max_length=1, choices=Connect_Choices)

    Op_Mode_Choices = (
    ("0", "Gateway"),
    ("1", "Roteador"),
    )
    op_mode = models.CharField(max_length=1, choices=Op_Mode_Choices)

    #op_mode_gateway = models.BooleanField(default=True)
    #op_mode_router = models.BooleanField(default=False)

    ip_adress = models.GenericIPAddressField()
    mask_adress = models.GenericIPAddressField()
    gateway_adress = models.GenericIPAddressField()

    def get_absolute_url(self):
        return f"/status/{self.id}/"

class Status_device(models.Model):
    mac_adress = MACAddressField(null=True, blank=True)
    firmware_ver = models.CharField(max_length=20)
    hardware_ver = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)
