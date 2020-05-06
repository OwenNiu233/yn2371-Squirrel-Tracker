#Yipeng Niu yn2371
from django.db import models
from django.forms import ModelForm
from .models import Record


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
