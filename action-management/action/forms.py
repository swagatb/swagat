__author__ = 'root'

from datetime import datetime, timedelta

from django.forms import ModelForm, ValidationError
from django.contrib.admin import widgets
from django.contrib.auth.models import User

from action.models import ActionManagement


class ActionCreateForm(ModelForm):
    """

    """
    class Meta:
        model = ActionManagement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ActionCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['date'].widget = widgets.AdminDateWidget()
        self.fields['date'].widget.attrs['class'] = 'form-control datepicker'
        self.fields['assigned_user'].widget.attrs['class'] = 'form-control'
    
    def clean(self):
        super(ActionCreateForm, self).clean()
        if not self.cleaned_data.get('title') or\
           not self.cleaned_data.get('description') or\
           not self.cleaned_data.get('date') or\
           not self.cleaned_data.get('assigned_user'):
            raise ValidationError('Please avoid the empty spaces!')

        return self.cleaned_data
