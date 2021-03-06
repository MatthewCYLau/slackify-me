from django import forms
from .models import InputMessage


CHANNEL_CHOICES= [
    ('DE2QP24U8', 'Matt Lau Slackbot'),
    ('GK08B28MQ', 'SlackifyMe Team Channel'),
    ]


class InputMessageForm(forms.ModelForm):

    name = forms.CharField(label='Your name', widget=forms.TextInput(attrs={"placeholder": "Enter name here"}))
    body = forms.CharField(label='Your message', widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Enter slack message body here"}))
    channel = forms.CharField(label='Slack channel', widget=forms.Select(choices=CHANNEL_CHOICES))

    class Meta:
        model = InputMessage
        fields = [

            'name',
            'body',
            'channel'
        ]
