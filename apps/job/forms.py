from django import forms

from apps.job.models import Job


class AddJobForm(forms.ModelForm):
    class meta:
        model = Job
        fields = ['title', 'short_description', 'long_description']
