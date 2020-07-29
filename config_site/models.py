from django.db import models
from django.conf import settings
from django.utils import timezone

class Login(models.Model):
    user = models.EmailField(max_length=100)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.user


class Connection(models.Model):
    connect_choices = (
        ('0', 'IP Estático'),
        ('1', 'IP Dinâmico'),
    )
    connect_choice = models.CharField(max_length=1, choices=connect_choices)

    def __str__(self):
        return self.connect_choice


class Config(models.Model):
    op_mode = models.BooleanField()

    def __str__(self):
        return self.op_mode
