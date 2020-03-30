from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.decorators.http import require_http_methods

from .forms import TopicForm, MessageForm

from .models import Topic


@login_required
def index(request):
    """Home view after login to display all unsolved and solved topics
        Vue d'accueil après la connexion pour afficher tous les sujets non résolus et résolus"""
    topics = Topic.objects.filter(is_solved=False)
    solved_topics = Topic.objects.filter(is_solved=True)
    return render(request, "index.html", {"topics": topics, "solved_topics": solved_topics})


@login_required
def single(request, topic_id):
    """View to display single topic information with messages, and allow users to answer Afficher pour afficher des
    informations sur un seul sujet avec des messages et permettre aux utilisateurs de répondre """
    # if this is a POST request we need to process the form data to register the message
    # s'il s'agit d'une demande POST, nous devons traiter les données du formulaire pour enregistrer le message
    if request.method == 'POST':
        # hydrate a form object with data from the request
        # hydrater un objet de formulaire avec les données de la demande
        form = MessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # get the message object from the form, add some info and save it in DB
            # récupérer l'objet message du formulaire, ajouter des informations et l'enregistrer dans DB
            message = form.save(commit=False)
            message.author = request.user
            message.topic = Topic.objects.get(id=topic_id)
            message.save()
    # Once the form is treated, we select the topic with all the related messages
    # Une fois le formulaire traité, nous sélectionnons le sujet avec tous les messages associés
    topic = Topic.objects.prefetch_related('message_set').get(id=topic_id)
    form = MessageForm()
    return render(request, "single.html", {"topic": topic, 'form': form})


@login_required
def user_questions(request):
    """View to diplay topics created by the logged user and allow topics creation
        Afficher pour afficher les sujets créés par l'utilisateur connecté et autoriser la création de sujets"""
    # if this is a POST request we need to process the form data to register the topic
    # s'il s'agit d'une demande POST, nous devons traiter les données du formulaire pour enregistrer le sujet
    if request.method == 'POST':
        # hydrate a form object with data from the request
        # hydrater un objet de formulaire avec les données de la demande
        form = TopicForm(request.POST)
        # check whether it's valid:
        # vérifier sa validité:
        if form.is_valid():
            # get the topic object from the form and persist it to DB
            # obtenir l'objet de rubrique du formulaire et le conserver dans la base de données
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
    # Create the form to be displayed in template and select the topics from the logged user
    # Créez le formulaire à afficher dans le modèle et sélectionnez les sujets de l'utilisateur connecté
    form = TopicForm()
    topics = Topic.objects.filter(author=request.user, is_solved=False)
    return render(request, "user_questions.html", {"topics": topics, 'form': form})


@require_http_methods(["POST"])
@login_required
def search(request):
    """View only accessible by post to search for a topic based on a string input
        Afficher uniquement accessible par un post pour rechercher un sujet basé sur une "entrée de chaîne" """
    # get back the data from the search form
    # récupérer les données du formulaire de recherche
    research = request.POST['search']
    # search for topics
    # Rechercher des sujets
    topics = Topic.objects.filter(Q(title__icontains=research) | Q(problem__icontains=research))
    return render(request, "search.html", {'research': research, 'topics': topics})


@login_required
def archives(request):
    """View to display all solved topics
        Afficher pour afficher tous les sujets résolus"""
    # get the topics from the logged user
    # obtenir les sujets de l'utilisateur connecté
    topics = Topic.objects.filter(author=request.user, is_solved=True)
    # get all the topics not from the logged user
    # obtenir tous les sujets ne provenant pas de l'utilisateur connecté
    other_topics = Topic.objects.filter(is_solved=True).exclude(author=request.user)
    return render(request, "archives.html", {"topics": topics, 'other_topics': other_topics})


@require_http_methods(["GET"])
@login_required
def delete_topic(request, topic_id):
    """View to delete a topic from DB
        Afficher pour supprimer un sujet de la base de données"""
    try:
        # make sur the id match a topic and the author is the user
        # assurez-vous que l'identifiant correspond à un sujet et que l'auteur est l'utilisateur
        topic = Topic.objects.get(id=topic_id)
        if request.user == topic.author:
            topic.delete()
    except Exception as e:
        pass
    return redirect('user_questions')


@require_http_methods(["GET"])
@login_required
def solve_topic(request, topic_id):
    """View to update a question as solved in DB
        Afficher pour mettre à jour une question telle que résolue dans DB"""
    try:
        # make sur the id match a topic and the author is the user
        # assurez-vous que l'identifiant correspond à un sujet et que l'auteur est l'utilisateur
        topic = Topic.objects.get(id=topic_id)
        if request.user == topic.author:
            # mark the topic as solved
            # marquer le sujet comme résolu
            topic.is_solved = 1
            topic.save()
    except Exception as e:
        pass
    return redirect('user_questions')
