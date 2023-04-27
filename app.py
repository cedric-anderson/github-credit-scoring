## importation des librairies
from pycaret.clustering import *
import streamlit as st
import pandas as pd
from PIL import Image 
import joblib 
import numpy as np

## Chargement du Kfold model
model = joblib.load(filename = 'predict_model.joblib')

## Definition de la fonction
def run():
    
    
    ## ajouter le titre de l'application streamlit
    st.title("Application de Machine Learning pour la detection de Fraud par carte de credit")
    
    
    ## Contact du concepteur de l'application
    st.sidebar.write('Auteur : Cedric Anderson')
    ## Image dans la sidebar
    st.sidebar.success("Contact :" 'https://www.pycaret.org')
    
    
     ## ajouter des informations sur le fonctionnement de l'application à la barre latérale
    st.sidebar.markdown(
        "**Cette application est crée pour detecter les fraudes sur carte de crédit**: \n"
        "1. Entrez les informations que vous souhaitez predire \n"
        "4. Cliquez sur le bouton **Predict** pour voir la prediction \n"
    )
      
    
    ## Image dans la sidebar
    st.sidebar.image('https://tse1.mm.bing.net/th?id=OIP.2G3whoG9_NcACTRObwyLrgHaHa&pid=Api&P=0')

        
   
           
    ## Zone de saisie numérique pour obtenir la valeur d'âge
    age = st.number_input('age', min_value=20, max_value=94, value=24)
    
    ## Zone de saisie categoriel pour obtenir la valeur salaire_annuelle
    salaire_annuelle = st.number_input("alaire_annuelle", min_value=4000.0, max_value=140004.0, value=54000.0)
            
    ## Zone de saisie categoriel pour obtenir la valeur duree_emploi
    duree_emploi = st.number_input("duree_emploi", min_value=0.0, max_value=80.0, value=7.0)
        
    ## Zone de saisie numérique pour obtenir la valeur de  montant_pret
    montant_pret = st.number_input('montant_pret', min_value=500.0, max_value=35000.0, value=800.0)
    
    ## Zone de saisie categoriel pour obtenir la valeur aux_interet
    taux_interet = st.number_input("taux_interet", min_value=5.42, max_value=23.22, value=10.99)
    
    ## Zone de saisie numérique pour obtenir la valeur de ratio_dette_revenu
    ratio_dette_revenu = st.number_input('ratio_dette_revenu', min_value=0.01 , max_value=0.83, value=0.15)
    
    ## Zone de saisie categoriel pour obtenir la valeur duree_credit_ant
    duree_credit_ant = st.number_input("duree_credit_ant",  min_value=2.0 , max_value=30.0, value=4.0)
       
    ## Zone de saisie categoriel pour obtenir la valeur statut
    statut = st.number_input("statut",  min_value=0 , max_value=3, value=2)
    
    ## Zone de saisie categoriel pour obtenir la valeur motif_credit
    motif_credit = st.number_input("motif_credit",  min_value=0 , max_value=3, value=2)
    
    ## Zone de saisie categoriel pour obtenir la valeur class_solvabilite
    class_solvabilite = st.number_input("class_solvabilite",  min_value=0 , max_value=6, value=2)
    
    ## Zone de saisie categoriel pour obtenir la valeur credit_rembourse
    credit_rembourse = st.number_input("credit_rembourse",  min_value=0 , max_value=1, value=0)
    
    
    # Definir la fonction d'inference
    def inference(age,	salaire_annuelle,	duree_emploi,	montant_pret,	taux_interet,	ratio_dette_revenu,	duree_credit_ant,	statut,	motif_credit,	class_solvabilite,	credit_rembourse):
        new_data = np.array([age,	salaire_annuelle,	duree_emploi,	
                             montant_pret,	taux_interet,	ratio_dette_revenu,	
                             duree_credit_ant,	statut,	motif_credit,	
                             class_solvabilite,	credit_rembourse
                             ])
        
        pred = model.predict(new_data.reshape(1, -1))
        return pred
    
    # Création du boutton de prediction
    if st.button('Predict'):
        prediction = inference(age,	salaire_annuelle,	duree_emploi,
                               montant_pret,	taux_interet,	ratio_dette_revenu,	
                               duree_credit_ant,	statut,	motif_credit,	
                               class_solvabilite,	credit_rembourse
                               )
        if st.success(prediction[0]) == 1:
            st.markdown("Cet individu **n'est pas un Fraudeur**")
        else:
            st.markdown('Cet individu **est un Fraudeur !**')
            
            

## calling the main function
if __name__ == '__main__':
    run()