'''from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']


from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date < date.today():
            raise ValidationError("Due date cannot be in the past!")
        return due_date
'''

'''from django import forms
from datetime import datetime
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        
        # Ensure that due_date is a datetime object, if it's a date object
        if isinstance(due_date, datetime.date):
            due_date = datetime.combine(due_date, datetime.min.time())
        
        # Add your custom validation here, e.g., checking if the due date is in the future
        if due_date < datetime.now():
            raise forms.ValidationError("The due date cannot be in the past.")
        
        return due_date
'''

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea'}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-input'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
