# Credit-Scoring
Lorsqu'une banque prête de l'argent a quelqu'un, elle prend le risque que cette dernière ne remborse pas cet argent dans le délais convenu. Ce risque est appelé **RISQUE DE CREDIT**. Alors avant d'octryer un crédit, les banques verifient si le client(e) qui demande un prêt sera capable de le rembouser. Cette verification se fait grâce à l'analyse de plusieurs parametres tels que: Les revenus, les depenses actuelles du client, etc. Cette analyse est encore effectuée manuellement par plusieurs banques. Ainsi, elle est très consommatrice en temps et en ressources financières.

Grâce au **MACHINE LEARNING**, il est possible d'automatiser cette tâche et de pouvoir prédire avec plus de précision, les clients qui seront en defaut de paiement.

Dans ce projet, nous allons construire un algorythme capable de prédire si une personne est en défaut de paiement ou pas(1 : défaut, 0 : non -défaut). Il s'agit donc d'un problème de classification car nous voulons prédire une variable discrète ( binaire pour être précis). Ensuite nous allons déployer notre algorythme dans une application web


En ce qui concerne les données, il s'agit des informations collectées sur d'anciens clients ayant contracté des prêts qui sont utilisées pour prédire le comportement des nouveaux clients.

Deux (2) types de données peuvent être utilisés pour modéliser la probabilité de défaut de paiement:

* Données liées à la demande de crédit:
* Données comportementales decrivant le bénéficiare du prêt.

Dans la pratique, les banques utilisent un mélange de ses deux types de données pour construire leur modèl de scoring appliqué a la gestion du risque de crédit.


Voici l'image de l'application web pour le Credit_Scoring:

Conditions préalables :

pandas==2.0.1

Sklearn==3.0.2

streamlit==1.21.0


Pour exécuter l’application web localement sur votre ordinateur, téléchargez les fichiers à partir du dossier. Modifiez le chemin d’accès du Dataset à l’emplacement correspondant sur votre machine. Sur le terminal, exécuter la commande **(streamlit run app.py)**.
Entrez les references de votre prediction et cliquez sur **Predict** :)

