from django import forms
from .models import Project, Task
from accounts.models import User
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["project", "title", "description", "assigned_to", "status"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only users with role 'USER'
        self.fields['assigned_to'].queryset = User.objects.filter(role='USER')
