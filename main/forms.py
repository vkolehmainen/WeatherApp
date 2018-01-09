from django import forms
from main.models import Observation

class ObservationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ObservationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    temperature = forms.FloatField(min_value=0.0)

    class Meta:
        model = Observation
        fields = ('city', 'temperature', 'time')
        labels = {
            'city': 'City',
            'temperature': 'Temperature',
            'time': 'Time'
        }
