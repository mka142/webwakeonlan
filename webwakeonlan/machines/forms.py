from django import forms
from .models import Machine
from django.core.validators import validate_ipv46_address
import re


def validate_mac_address(value):
    if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", value.lower()):
        return None
    raise forms.ValidationError("Invalid MAC Address")


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ("name", "description", "mac_address", "ip_address")

    def clean_ip_address(self):
        if self.cleaned_data["ip_address"]:
            validate_ipv46_address(self.cleaned_data["ip_address"])
        return self.cleaned_data["ip_address"]

    def clean_mac_address(self):
        mac_address = self.cleaned_data["mac_address"]
        validate_mac_address(mac_address)
        return mac_address
