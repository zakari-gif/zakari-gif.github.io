#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 01:36:28 2021

@author: abdoumahamadouzakariyaou
"""
import data1 as PiscinePatinoireCampus 
import data2 as PoisyParcDesGlaisins
from StructureArc import Graphe
from StructureNoeud import ArretBUS
import networkx
import matplotlib.pyplot as plt

"-----------------------------Le Graphe Regular-----------------------------------------------"

G = networkx.Graph()     
name1 = PiscinePatinoireCampus.regular_path.split(" N ")
name2= PoisyParcDesGlaisins.regular_path.split(" N ")
def Creationgraphe():
    for i in range(len(name1)-1):
        G.add_edge(name1[i], name1[i+1],poids = 1)
        for i in range(len(name2)-1):
            G.add_edge(name2[i], name2[i+1], poids = 1)
    return G
"----------------------------Graphe Weekend--------------------------------------------------"
def CreationgrapheWeekend():
    for i in range(len(name1)-1):
        G.add_edge(name1[i], name1[i+1],poids = 1)
        for i in range(len(name2)-1):
            G.add_edge(name2[i], name2[i+1], poids = 1)
    return G


"-----------------Convertion de temps en seconde-------------------------------------"
def Horraire_Seconde(Nomarret,Numeroligne,Weekend=False): #donne la liste des horaires en seconde
    d=ArretBUS(Nomarret,PiscinePatinoireCampus,PoisyParcDesGlaisins,Numeroligne,[],[],[])
    g=d.getHorairesligne()
    if Weekend==True:
        g=d.getHorairesligneWeekend()
    listehorairEnseconde=[]
    for i in g:
        if len(i)!=0:
            if i[0]==Nomarret:
                times=i[1]
                for time in times:
                    if time!='-':
                        h_splited = time.split(":")
                        heures = int(h_splited[0])*60*60       
                        minutes = int(h_splited[1])*60
                        temps = heures + minutes
                        listehorairEnseconde.append(temps)
                return listehorairEnseconde
            else:
                return "ON A RIEN TROUVE"
#print(Horraire_Seconde("Mandallaz",1,Weekend=False))
"-----------------------conversion de seconde en format h:mn -----------------"

def Horraire_Seconde_format(heureEnseconde): #donne l'heure sous format h:mn
    heure=heureEnseconde//3600
    minute=heureEnseconde//60-heure*60
    return(str(heure)+':'+str(minute))

"--------------------convertir le format h:mn en seconde----------------------"
def convertir_En_seconde(heure):
    h_splited = heure.split(":")
    heures = int(h_splited[0])*60*60       
    minutes = int(h_splited[1])*60
    temps = heures + minutes
    return temps

"-----------------------trouvé le prochain bus qui passe a un arret donné------"

def prochainBUS(Numeroligne,Nomarret,lheur,Weekend): #Donne une liste des arrets qui suivent l'arret en argument meme si c'est pas la meme ligne
    h_splited = lheur.split(":")
    heuresENs = int(h_splited[0])*60*60       
    minutesENs = int(h_splited[1])*60
    tempsenseconde = heuresENs + minutesENs
    listedesHoraires=Horraire_Seconde(Nomarret,Numeroligne,Weekend)
    if type(listedesHoraires)==list and len(listedesHoraires)!=0: #au cas ou Horraire_seconde renvoie "ON A RIEN TROUVE" ou liste vide
        for temps in listedesHoraires:
            if type(temps)==int:
                if temps>=tempsenseconde:
                    tempsenseconde=temps
                    return(Horraire_Seconde_format(tempsenseconde))
    else:
        return "NOUS N'AVONS PAS DE TRAGET POUR VOUS"
    
"------------------test-----------------------------------"    
"""k=Horraire_Seconde("Impérial",1,False)
print(k)
l=prochainBUS(2,"VIGNIÈRES","9:20",False)
print(l)
"""

"-----------------------Shortest(calcule le chemin le plus court en nombre d'arcs)-----------"

def shortest(depart,arrive,weekend):
    Graphe=Creationgraphe()
    GrapheWeekend=CreationgrapheWeekend()
    if weekend==True:
        chemin=networkx.shortest_path(GrapheWeekend,depart,arrive)
    chemin=networkx.shortest_path(Graphe,depart,arrive)
    return chemin
#test
#a=shortest("Impérial","CAMPUS",False)
#print(a)


"----------------------fastest(Fonction calculant le trajet qui prend le moins de temps de transport)------"

"----------------Creation de graphe manuellemnet----------------------------------------"
g = {
        'LYCÉE_DE_POISY' : ['POISY_COLLÈGE'],
        'POISY_COLLÈGE' : ['LYCÉE_DE_POISY','Vernod'],
        'Vernod' : ['POISY_COLLÈGE', 'Meythet_Le_Rabelais'],
        'Meythet_Le_Rabelais' : ['Vernod', 'Chorus'],
        'Chorus' : ['Meythet_Le_Rabelais', 'Mandallaz'],
        'Mandallaz' : ['GARE', 'Chorus'],
        'GARE' : ['Mandallaz', 'France_Barattes', 'Bonlieu','Courier'],
        'France_Barattes' : ['C.E.S._Barattes','GARE'],
        'C.E.S._Barattes' : ['France_Barattes','VIGNIÈRES'],
        'VIGNIÈRES' : ['Ponchy','C.E.S._Barattes','CAMPUS','Pommaries'],
        'Ponchy' : ['VIGNIÈRES','PARC_DES_GLAISINS'],
        'PARC_DES_GLAISINS' : ['Ponchy','PISCINE-PATINOIRE'],
        'PISCINE-PATINOIRE' : ['PARC_DES_GLAISINS','Arcadium'],
        'Arcadium' : ['PISCINE-PATINOIRE','Parc_des_Sports'],
        'Parc_des_Sports' : ['Place_des_Romains','Arcadium'],
        'Place_des_Romains' : ['Parc_des_Sports','Courier'],
        'Courier' : ['Place_des_Romains','GARE'],
        'Bonlieu' : ['GARE','Préfecture_Pâquier'],
        'Préfecture_Pâquier' : ['Bonlieu','Impérial'],
        'Impérial' : ['Préfecture_Pâquier','Pommaries'],
        'Pommaries' : ['Impérial','VIGNIÈRES'],
        'CAMPUS' : ['VIGNIÈRES'],
    }   
graphe = Graphe(g)

def fastest(start_node, end_node, time,weekend,ligne): #Elle marche bien mais elle me renvoie un resultat douteux
    toti=convertir_En_seconde(time)
    paths = graphe.find_all_paths(start_node, end_node)
    ListeTemps = []
    tpstot = 0
    listehoraire=Horraire_Seconde(start_node,ligne,weekend)
    heuredepartleplusproche=0
    j=0
    for i in range (0,len(listehoraire)):
        if heuredepartleplusproche<toti:
            heuredepartleplusproche=listehoraire[i]
            j=j+1
    indice=listehoraire.index(heuredepartleplusproche)
    for path in paths:
        tpstot=0
        for i in range (1,len(path)):
            listeHoraire1=Horraire_Seconde(path[i],1,Weekend=False)
            listeHoraire2=Horraire_Seconde(path[i-1],1,Weekend=False)
            listeHoraire3=Horraire_Seconde(path[i],2,Weekend=False)
            listeHoraire4=Horraire_Seconde(path[i-1],2,Weekend=False)
            if ligne==1:
                a=listeHoraire1[indice]-listeHoraire2[indice]
                j=0
                while (a<0 or a>900) and len(listeHoraire1)<=indice+1:
                    j=j+1
                    a=listeHoraire1[indice+j]-listeHoraire2[indice]
            else:
                a=listeHoraire3[indice]-listeHoraire4[indice]
                i=0
                while (a<0 or a>900) and len(listeHoraire3)<=indice+1:
                    i=i+1
                    a=listeHoraire3[indice+i]-listeHoraire4[indice]
            tpstot = tpstot + a
        ListeTemps.append(tpstot)
    print("FASTEST \n Chemin effectué " , paths[ListeTemps.index(min(ListeTemps))])
    H=Horraire_Seconde_format(toti+min(ListeTemps))
    print("Votre heure d'arrivé est:"+H)
    print("Temps de trajet minimal " , Horraire_Seconde_format(min(ListeTemps)))
    
#print(fastest("Vernod","CAMPUS","10:10",False,1))


"----------------------foremost(Fonction calculant le trajet qui arrive au plus tôt)--------------------"


def foremost(ligne,weekend,heure,Arretdepart,Arretarrive,chemin=[]):
    #chemin.append(Arretdepart)
    Graphe=Creationgraphe()
    GrapheWeekend=CreationgrapheWeekend()
    d=ArretBUS(Arretdepart,PiscinePatinoireCampus,PoisyParcDesGlaisins,ligne,[],[],[])
    LesArretsquisuivent=d.getArretsuivant()
    nextime=prochainBUS(ligne,Arretdepart,heure,weekend)
    if ligne==2:
        LesArretsquisuivent=d.getArretprecedent() # ca ne marche pas toujours pa si il s'agit du terminus,je ne pas pu debugger
    h_splited =nextime.split(":")
    heures = int(h_splited[0])*60*60       
    minutes = int(h_splited[1])*60
    temps = heures + minutes
    heuredepartleplusproche=0
    ArretAajouterdanschemin=""
    horaireArretprecedent=0
    if type(LesArretsquisuivent)==list:
        for arret in LesArretsquisuivent:
            if arret!=Arretarrive:
                listehoraire=Horraire_Seconde(arret,ligne,weekend)
                i=0
                while horaireArretprecedent>=heuredepartleplusproche:
                    while i<len(listehoraire) and heuredepartleplusproche< temps:
                        heuredepartleplusproche=listehoraire[i]
                        i=i+1
                    ArretAajouterdanschemin=arret
            else:
                listehoraire=Horraire_Seconde(arret,ligne,weekend)
                i=0
                while i<len(listehoraire) and heuredepartleplusproche< temps:
                    heuredepartleplusproche=listehoraire[i]
                    i=i+1
                ArretAajouterdanschemin=arret
            break
        chemin.append(ArretAajouterdanschemin)
        heuredepartleplusproche=Horraire_Seconde_format(heuredepartleplusproche)
        if ArretAajouterdanschemin==Arretarrive:
            return (chemin,heuredepartleplusproche)
        else:
            return foremost(ligne,weekend,heuredepartleplusproche,ArretAajouterdanschemin,Arretarrive,chemin)

#x=foremost(1,True,'9:43',"Impérial","CAMPUS",[])
#print(x)
print("-----Bienvenu Dans l'application Sibra------------")
def SIBRA():
    Graphe=Creationgraphe()
    GrapheWeekend=CreationgrapheWeekend()
    x=input("Vous voulez voyagez? OUI/NON:")
    while x=="n":
        print("Aurevoir à bientot")
        break
    while x=="o":
        ligne = int(input("Sur Quelle ligne?")) # C'est le sens....il faut obligatoirement saisir le bon sens
        heure = input("Quelle heure est-il?")
        Arretdepart = input("A quel arrêt vous trouvez vous?")
        Arretarrive = input("A quel arrêt vous voulez allez ?")
        weekend = bool(input("weekend ? True/False :"))
        if weekend=="f":
            weekend=bool(False)
        elif weekend=="t":
            weekend=bool(True)
        relence=True
        while relence==True:
            option=input("Vous optez pour quelle option (shortest,formost,fastest):")
            if option=="s":
                print("le plus court chemin en nombre d'arret est:",shortest(Arretdepart,Arretarrive,weekend))
                relence=False
            elif option=="F":
                print("le chemin est l'heure d'arriver sont:",foremost(ligne,weekend,heure,Arretdepart,Arretarrive,chemin=[Arretdepart]))
                relence=False
            elif option=="f":
                print(fastest(Arretdepart,Arretarrive,heure,weekend,ligne))
                relence=False
            else:
                print("Desolé veuillez corriger votre choix")
                relence=True
#test General
test=SIBRA()