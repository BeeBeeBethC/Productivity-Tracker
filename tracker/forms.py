from django import forms
from .models import custom_user, ToDo

class userForm(forms.ModelForm):
    class Meta:
        model = custom_user
        fields = ['username', 'lastname', 'firstname', 'email', 'password']

class todoForm(forms.ModelForm):
    class Meta:
        model = tracker
        fields['username','task','task_completed']
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)