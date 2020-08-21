import os
import json
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ConfigForm
from .models import Config_device
from django.conf import settings


# Create your views here.
def read_file():
    with open(os.path.join(settings.BASE_DIR, 'status_file.txt')) as json_file:
        info = json.load(json_file)
    return(info)


@login_required
def Config_device_View(request):
    info = read_file()
    form = ConfigForm()

    if request.method == "POST":
        form = ConfigForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            total_info = dict(form.cleaned_data, **info)
            with open("status_file.txt", "w") as outfile:
                json.dump(total_info, outfile, ensure_ascii=False)
        else:
            print(form.errors)

    context = {"form": form}

    return render(request, 'config_site/config.html', context)


@login_required
def Status_device_View(request, id):
    obj = Config_device.objects.get(id=id)#id=id
    obj = get_object_or_404(Config_device, id=id)#id=id

    info = read_file()
    mac_status = info["MAC"]
    hardware_status = info["hardware"]
    firmware_status = info["firmware"]
    serial_status = info["serial"]

    context = {"object": obj, "mac": mac_status, "hw": hardware_status, "fw": firmware_status, "sr": serial_status}

    return render(request, 'config_site/status.html', context)


@login_required
def Status_View(request):
    info = read_file()
    print(info)

    if "connect_choice" in info:
        connect_status = info["connect_choice"]
        if info["connect_choice"] == "0":
            connect_status = "IP Estático"
        else:
            connect_status = "IP Dinâmico"
    else:
        connect_status = "Valor não informado"

    if "op_mode" in info:
        opmode_status = info["op_mode"]
        if info["op_mode"] == "0":
            opmode_status = "Gateway"
        else:
            opmode_status = "Roteador"
    else:
        opmode_status = "Valor não informado"

    if "ip_adress" in info:
        ipadress_status = info["ip_adress"]
    else:
        ipadress_status = "Valor não informado"

    if "mask_adress" in info:
        maskadress_status = info["mask_adress"]
    else:
        maskadress_status = "Valor não informado"

    if "gateway_adress" in info:
        gatewayadress_status = info["gateway_adress"]
    else:
        gatewayadress_status = "Valor não informado"

    mac_status = info["MAC"]
    hardware_status = info["hardware"]
    firmware_status = info["firmware"]
    serial_status = info["serial"]

    context = {
    "connect": connect_status,
    "mode": opmode_status,
    "ip": ipadress_status,
    "mask": maskadress_status,
    "gateway": gatewayadress_status,
    "mac": mac_status,
    "hw": hardware_status,
    "fw": firmware_status,
    "sr": serial_status,
    }

    return render(request, 'config_site/status.html', context)
