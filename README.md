# Forum d'entre-aide utilisateurs sous Django
Avant de lire ce README :
Après le clone il ne faut pas oublier de vérifier le venv, faire un pip freeze. Si Django n'est pas la ... installer le
Il faudra faire de meme pour la BDD, le migration et le superuser ;-) 

produire une application à l'aide du framework Python Django et se familiarisent ainsi avec ses fonctionnalités principales. L'application en question est un forum d'entre-aide et de questions techniques pour une entreprise sur le modèle de stackoverflow.

Au travers de cet exercice, les étudiants apprennent à :
- Démarrer une application Django
- Organiser une application Django
- Gérer le routing d'une application
- Utiliser l'ORM de Django
- Gérer un modèle en orienté objet
- Comprendre le protocole HTTP
- Renvoyer un template sous forme de réponse
- Utiliser un moteur de template
- Utiliser l'administration de Django

## Consignes

WorldTransit est un grand groupe international spécialisé dans les métiers de la logistique. Fort de plus de 2000 consultants à travers le monde, les domaines d'expertise du groupe sont très variés. Aujourd'hui cependant, un problème a été constaté par l'équipe de direction de WorldTransit France, très souvent lors de problèmes techniques interne il est nécessaire de faire appel à un prestataire extérieur ou de faire déplacer du personnel alors qu'avec l'aide appropriée le problème aurait pu être réglé sur place. La direction a donc demandé au service informatique de produire une plateforme d'entre-aide de type forum où les employés en difficulté pourront poser leurs questions à d'autres employés de l'entreprise qui pourront leur répondre et ainsi peut-être éviter des frais supplémentaires.

Développeur python dans ce service, la tâche de produire un tel forum vous a été assignée et afin de gagner du temps dans votre processus de développement, vous avez choisi d'utiliser le framework Django.

Spécifications fonctionnelles:
- Les utilisateurs ne peuvent accéder à l'application qu'après s'être identifiés avec leur compte personnel
- La page d'accueil affiche tous les sujets non-résolus d'un côté et quelques sujets résolus de l'autre
- Une page permet à l'utilisateur de voir ses sujets personnels non résolus
- L'utilisateur peut ouvrir un nouveau sujet s'il le désire
- Une page permet d'accéder au détail de chaque sujet
- Sur la page d'un sujet, il est possible de poster une réponse au sujet
- Un utilisateur peut choisir de supprimer un de ses sujets ou de le marquer comme résolu s'il estime qu'il a obtenu une réponse à son problème
- Une page archives liste les sujets résolus de l'utilisateur ainsi que les autres sujets résolus

Spécifications techniques:
- Python3
- Framework Django 3
- Template organisé avec triple héritage
- Framework CSS Bootstrap 4

## Pour aller plus loin

- Proposez un formulaire de recherche qui permet de recherche les mots tapés par l'utilisateur dans les titres et contenus de tous les sujets du site
- Implantez un système de pagination afin que l'utilisateur ne soit pas obligé de scroller à l'infini quand le forum comportera des centaines de sujets
- Utilisez les messages flash de django pour donner des indications claires à l'utilisateur sur le succès ou l'échec des actions qu'il entreprend.  
