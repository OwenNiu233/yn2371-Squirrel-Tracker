#Yipeng Niu yn2371
from django.db imoport models
from django.forms import DodelForm
from .models import Record


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
