from django import forms
from order.models import Oder
class OderForm(forms.ModelForm):
  class Meta:
    model = Oder
    fields = "__all__"
