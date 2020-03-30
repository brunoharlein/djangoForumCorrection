from django.db import models
from django.contrib.auth import get_user_model

class Topic(models.Model):
    """Class representing a Topic entity
        Classe représentant une entité de sujet"""
    title = models.CharField(max_length=200)
    problem = models.TextField()
    # one to many relation, if and author is deleted all his topics are deleted by cascade
    # relation un à plusieurs, si et l'auteur est supprimé tous ses sujets sont supprimés par cascade
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    opening_date = models.DateTimeField(auto_now=True)
    is_solved = models.BooleanField(default=False)

class Message(models.Model):
    """Class representing a Message entity
        Classe représentant une entité Message"""
    content = models.TextField()
    # one to many relation, if and author is deleted all his messages are deleted by cascade
    # relation un à plusieurs, si et l'auteur est supprimé tous ses messages sont supprimés par cascade
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    publishing_date = models.DateTimeField(auto_now=True)
    # one to many relation, if a topic is deleted all the related messages are deleted by cascade
    # relation un à plusieurs, si un sujet est supprimé tous les messages associés sont supprimés par cascade
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
