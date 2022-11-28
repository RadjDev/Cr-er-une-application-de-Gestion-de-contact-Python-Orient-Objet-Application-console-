import sqlite3
from random import randint
'''
une application qui permet de:
Se connecter sur la base de données SQlite
Ajouter un contact
Modifier un contact
Supprimer un contact
Afficher la liste de tous les contacts
Rechercher un contact par son numéro de téléphone'''

class Contact:
    def __init__(self):
        self.Nom_Prenom ="Ferrari"
    def Connexion(self):
        connecter_bd = sqlite3.connect("basededonneesContact.db")
        curseur = connecter_bd.cursor()
        print("Connexion réussie à la base de données Contact ")
        curseur.execute('''CREATE TABLE IF NOT EXISTS contact(
                        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        NomPrenom TEXT  NOT NULL,
                        Email  TEXT,
                        NumeroTelephone TEXT NOT NULL,
                        Adresse TEXT
                        )''')
        connecter_bd.commit() 
        connecter_bd.close()
    #Ajouter un contact    
    def Ajouter_contact(self):
        global entrer1 , entrer2, entrer3, entrer4, liste_contact
        liste_contact=[]
        entrer1 ="0"
        while( entrer1 != "q" ):
            liste_contact=[]
            entrer1= input("Saisir Nom et Prénom \n")        
            if (entrer1)!= "":
                liste_contact.append(entrer1)
                entrer2=input("Saisir E-mail \n")
                if (entrer2)!= "":
                    liste_contact.append(entrer2)
                    entrer3=input("Saisir Numéro de Téléphone \n")
                    if (    entrer3)!= "":
                        liste_contact.append(entrer3)
                        entrer4=input("Saisir Adress \n")
                        if (entrer4)!= "":
                            liste_contact.append(entrer4)
            liste_contact=  [(entrer1,entrer2,entrer3,entrer4)] 
            break       
        connecter_bd = sqlite3.connect("basededonneesContact.db")
        curseur = connecter_bd.cursor()
        for donnee in liste_contact:
            curseur.execute('''INSERT INTO contact (NomPrenom, Email, NumeroTelephone, Adresse) VALUES (?, ?, ?, ?)''', donnee)
        connecter_bd.commit() 
        connecter_bd.close()
        
    def Afficher(self): 
        connecter_bd = sqlite3.connect("basededonneesContact.db")
        curseur = connecter_bd.cursor()
        curseur.execute('''select * from contact ''')
        result = curseur.fetchall()
        for resultat in result:
           print(resultat)
        connecter_bd.commit() 
        connecter_bd.close()   
    #Modifier un contact    
    def Modifier(self):
        global entrerId,modifierNomPrenom,modifierEmail,modifierNumeroTelephone,modifierAdress,rechercherCont,entrer1
        entrer1 ="o"
        while( entrer1 == "o" ):
            entrerId=[]
            modifierNomPrenom=[]
            modifierEmail=[]
            modifierNumeroTelephone=[]
            modifierAdress=[]
            entrerNumero=[]
            rechercherCont=[]
            #print("Vous pouvez quitter à t
            modifierContact= input(" Saisir 1 pour modifier Nom et Prénom \n Saisir 2 pour modifier E-mail \n Saisir 3 pour modifier Numéro de Téléphone \n Saisir 4 pour modifier Adress \n Saisir 5 pour Supprimé Contact \n Saisir 6 pour Rechercher un Contact par son son numéro de téléphone \n")
            try:
                if  int(modifierContact)==1:
                    entrerId = input(" Veillez saisir votre Id \n")
                    if  entrerId != 0:
                        modifierNomPrenom= input(" Entrer nouveau Nom et Prénom \n")
                        connecter_bd = sqlite3.connect("basededonneesContact.db")
                        curseur = connecter_bd.cursor()
                        curseur.execute("UPDATE contact SET NomPrenom=? WHERE id=? ",([modifierNomPrenom,entrerId]))
                        connecter_bd.commit()
                        self.Afficher
                        connecter_bd.close() 
                    
                    
                elif int(modifierContact)==2:
                    entrerId = input(" Veillez saisir votre Id \n")
                    if  entrerId != 0:    
                        modifierEmail= input(" Entrer nouveau E-mail \n")
                        connecter_bd = sqlite3.connect("basededonneesContact.db")
                        curseur = connecter_bd.cursor()
                        curseur.execute("UPDATE contact SET Email=? WHERE id=? ",([modifierEmail,entrerId]))
                        connecter_bd.commit()
                        self.Afficher 
                        connecter_bd.close()
                    
                elif int(modifierContact)==3:
                    entrerId = input(" Veillez saisir votre Id \n")
                    if  entrerId != 0:    
                        modifierNumeroTelephone= input(" Entrer nouveau Numéro de Téléphone \n")
                        connecter_bd = sqlite3.connect("basededonneesContact.db")
                        curseur = connecter_bd.cursor()
                        curseur.execute("UPDATE contact SET NumeroTelephone=? WHERE id=? ",([modifierNumeroTelephone,entrerId]))
                        connecter_bd.commit()
                        self.Afficher 
                        connecter_bd.close()        
                    
                elif int(modifierContact)==4:
                    entrerId = input(" Veillez saisir votre Id \n")
                    if  entrerId != 0:    
                        modifierAdress= input(" Entrer nouveau Adress \n")
                        connecter_bd = sqlite3.connect("basededonneesContact.db")
                        curseur = connecter_bd.cursor()
                        curseur.execute("UPDATE contact SET Adresse=? WHERE id=? ",([modifierAdress,entrerId]))
                        connecter_bd.commit()
                        self.Afficher
                        connecter_bd.close()        
            #supprim Contact        
                elif int(modifierContact)==5:
                    entrerNumero = input(" Veillez saisir votre Numéros \n")
                    if  entrerNumero != 0:    
                    #supprimContact= input(" Voulez vous vraiment supprim \n")
                        connecter_bd = sqlite3.connect("basededonneesContact.db")
                        curseur = connecter_bd.cursor()
                        curseur.execute("DELETE from contact WHERE NumeroTelephone=?",([entrerNumero]))
                        connecter_bd.commit()
                        self.Afficher
                        connecter_bd.close()   
                    
                elif int(modifierContact)==6:
                    rechercherCont = input(" Veillez saisir votre Numéros \n")
                    if  int(rechercherCont) != 0:    
                    #supprimContact= input(" Voulez vous vraiment supprim \n")
                        connecter_bd = sqlite3.connect("basededonneesContact.db")
                        curseur = connecter_bd.cursor()
                        curseur.execute("SELECT * FROM contact WHERE NumeroTelephone LIKE '%"+rechercherCont+"%'",)
                        result = curseur.fetchall()
                        for resultat in result:
                                   print(resultat)
                        connecter_bd.commit()
                        connecter_bd.close()                                
                else :
                    print("Veillez choisir une option existente.")
                #print(affichmenue)
                #break
            except:
                
                if str(entrer1).lower()== "q":
                    break
                else :                  
                    print("Vous n'avez ni entré une option existente  ni appuyé sur la touche Quittez.")
                        
            entrer1 = input("Voulez-vous recommencer ? o/n \n").lower() 
        print("Vous avez quitté le jeu")                                               
conactact1= Contact() 
#print(conactact1.Nom_Prenom)
#conactact1.Afficher()
#conactact1.Connexion()
#conactact1.Ajouter_contact() 
conactact1.Modifier() 
conactact1.Afficher()  


        
               
        
        
  