from django import forms

from .models import Topic

class Topicform(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}