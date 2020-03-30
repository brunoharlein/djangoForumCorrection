from django.db import models
from django import forms
from django.forms import ModelForm

from .models import Topic, Message

class TopicForm(ModelForm):
    """Form representing a topic entity for registration
        Formulaire représentant une entité pour l'inscription"""
    class Meta:
        model = Topic
        # we have only those fields since the other are not filled by the user
        # nous n'avons que ces champs puisque les autres ne sont pas renseignés par l'utilisateur
        fields = ['title', 'problem']

    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        # add class and translate labels for the different fields
        self.fields['title'].widget.attrs.update({'class': 'form-control',})
        self.fields['title'].label = "Votre question"
        self.fields['problem'].widget.attrs.update({'class': 'form-control',})
        self.fields['problem'].label = "Explication du problème"

class MessageForm(ModelForm):
    """Form representing a message entity for registration
        Formulaire représentant une entité de message pour l'enregistrement"""
    class Meta:
        model = Message
        # we have only those fields since the other are not filled by the user
        # nous n'avons que ces champs puisque les autres ne sont pas renseignés par l'utilisateur
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        # add class and translate labels for the different fields
        # ajouter une classe et traduire des étiquettes pour les différents champs
        self.fields['content'].widget.attrs.update({'class': 'form-control',})
        self.fields['content'].label = "Votre message"
