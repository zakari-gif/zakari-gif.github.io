#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 01:33:19 2021

@author: abdoumahamadouzakariyaou
"""


import data1 as PiscinePatinoireCampus 
import data2 as PoisyParcDesGlaisins
import networkx
import matplotlib.pyplot as plt

class ArretBUS():
    def __init__(self,NomArret,direction1,direction2,Numeroligne,Arretsuivant=[],Arretprecedent=[],Horairesligne=[]):
        self.NomArret=NomArret
        self.direction1=direction1
        self.direction2=direction2
        self.Numeroligne=Numeroligne
        self.Arretsuivant=Arretsuivant
        self.Arretprecedent=Arretprecedent
        self.Horairesligne=Horairesligne
    def getNomArret(self):
        return self.NomArret
    def getdirection1(self):
        return self.direction1
    def getdirection2(self):
        return self.direction2
    def getArretsuivant(self):
        listearretsuivant=[]
        listearret1=self.direction1.regular_path.split(" N ")
        listearret2=self.direction2.regular_path.split(" N ")
        if self.NomArret=='CAMPUS' or self.NomArret=='PARC_DES_GLAISINS':
            return "C'est le 'TERMINUS"
        elif self.NomArret=='PISCINE-PATINOIRE' or self.NomArret=='LYCÉE_DE_POISY + POISY_COLLÈGE':
            return "C'est le premier arret"
        for arret in listearret1:
            if self.NomArret==arret:
                indice=listearret1.index(arret)
                listearretsuivant.append(listearret1[indice+1])
        for arret in listearret2:
            if self.NomArret==arret:
                indice=listearret2.index(arret)
                listearretsuivant.append(listearret1[indice+1])
        return listearretsuivant
    def getArretprecedent(self):
        listearretprecedent=[]
        listearret1=self.direction1.regular_path.split(" N ")
        listearret2=self.direction2.regular_path.split(" N ")
        for arret in listearret1:
            if self.NomArret==arret:
                indice=listearret1.index(arret)
                listearretprecedent.append(listearret1[indice-1])
        for arret in listearret2:
            if self.NomArret==arret:
                indice=listearret2.index(arret)
                listearretprecedent.append(listearret1[indice-1])
        return listearretprecedent
    def getNumeroligne(self):
        return self.Numeroligne
    def getHorairesligne(self):
        dichorgo1=self.direction1.regular_date_go1
        dichorbac1=self.direction1.regular_date_back1
        dichorgo2=self.direction2.regular_date_go1
        dichorbac2=self.direction2.regular_date_back1
        listehoraireligne1direction1=[]
        listehoraireligne2direction1=[]
        listehoraireligne1direction2=[]
        listehoraireligne2direction2=[]
        if self.Numeroligne==1:
            for key in dichorgo1:
                if self.NomArret==key:
                    listehoraireligne1direction1=[self.NomArret]
                    listehoraireligne1direction1.append(dichorgo1[key])
            for key in dichorgo2:
                if self.NomArret==key:
                    listehoraireligne1direction2=[self.NomArret]
                    listehoraireligne1direction2.append(dichorgo2[key])
        elif self.Numeroligne==2:
            for key in dichorbac1:
                if self.NomArret==key:
                    listehoraireligne2direction1=[self.NomArret]
                    listehoraireligne2direction1.append(dichorbac1[key])
            for key in dichorbac2:
                if self.NomArret==key:
                    listehoraireligne2direction2=[self.NomArret]
                    listehoraireligne2direction2.append(dichorbac2[key])
        
        resultat=[listehoraireligne1direction1,listehoraireligne2direction1,listehoraireligne1direction2,listehoraireligne2direction2]
        return resultat
#----------------------------------------------------------------------------------------------------
                                                #WEEKEND
#----------------------------------------------------------------------------------------------------
    def getArretsuivantWeekend(self):
        listearretsuivant=[]
        listearret1=self.direction1.we_holidays_path1.split(" N ")
        listearret2=self.direction2.we_holidays_path1.split(" N ")
        if self.NomArret=='CAMPUS' or self.NomArret=='PARC_DES_GLAISINS':
            return "C'est le 'TERMINUS"
        elif self.NomArret=='PISCINE-PATINOIRE' or self.NomArret=='LYCÉE_DE_POISY + POISY_COLLÈGE':
            return "C'est le premier arret"
        for arret in listearret1:
            if self.NomArret==arret:
                indice=listearret1.index(arret)
                listearretsuivant.append(listearret1[indice+1])
        for arret in listearret2:
            if self.NomArret==arret:
                indice=listearret2.index(arret)
                listearretsuivant.append(listearret1[indice+1])
        return listearretsuivant
    def getArretprecedentWeekend(self):
        listearretprecedent=[]
        listearret1=self.direction1.we_holidays_path1.split(" N ")
        listearret2=self.direction2.we_holidays_path1.split(" N ")
        for arret in listearret1:
            if self.NomArret==arret:
                indice=listearret1.index(arret)
                listearretprecedent.append(listearret1[indice-1])
        for arret in listearret2:
            if self.NomArret==arret:
                indice=listearret2.index(arret)
                listearretprecedent.append(listearret1[indice-1])
        return listearretprecedent


    def getHorairesligneWeekend(self):
        dichorgo1=self.direction1.we_holidays_date_go1
        dichorbac1=self.direction1.we_holidays_date_back1
        dichorgo2=self.direction2.we_holidays_date_go1
        dichorbac2=self.direction2.we_holidays_date_back1
        listehoraireligne1direction1=[]
        listehoraireligne2direction1=[]
        listehoraireligne1direction2=[]
        listehoraireligne2direction2=[]
        if self.Numeroligne==1:
            for key in dichorgo1:
                if self.NomArret==key:
                    listehoraireligne1direction1=[self.NomArret]
                    listehoraireligne1direction1.append(dichorgo1[key])
        elif self.Numeroligne==2:
            for key in dichorbac1:
                if self.NomArret==key:
                    listehoraireligne2direction1=[self.NomArret]
                    listehoraireligne2direction1.append(dichorbac1[key])
        elif self.Numeroligne==1:
            for key in dichorgo2:
                if self.NomArret==key:
                    listehoraireligne1direction2=[self.NomArret]
                    listehoraireligne1direction2.append(dichorgo2[key])
        elif self.Numeroligne==2:
            for key in dichorbac2:
                if self.NomArret==key:
                    listehoraireligne2direction2=[self.NomArret]
                    listehoraireligne2direction2.append(dichorbac2[key])
        resultat=[listehoraireligne1direction1,listehoraireligne2direction1,listehoraireligne1direction2,listehoraireligne2direction2]
        return resultat
    
#-----------------------------------------------------------------------------------------------------   
    def setNomArret(NomArret):
        self.NomArret=NomArret
    def setdirection1(direction):
        self.direction1=direction
    def setdirection2(direction):
        self.direction2=direction
    def setArretsuivant(Arretsuivant):
        self.Arretsuivant=Arretsuivant
    def setArretprecedent(Arretprecedent):
        self.Arretprecedent=Arretprecedent
    def setHorairesligne(Horairesligne):
        self.Horairesligne=Horairesligne
        
"""
print("-----------testclassArretBus---------")
d=ArretBUS("GARE",PiscinePatinoireCampus,PoisyParcDesGlaisins,1,[],[],[])
e=d.getArretsuivant()
#print(e)
f=d.getArretprecedent()
#print(f)
g=d.getHorairesligne()
#print(g)
h=d.getArretsuivantWeekend()
#print(h)
i=d.getArretprecedentWeekend()
#print(i)
j=d.getHorairesligneWeekend()
#print(j)
print("-----------testclassArretBus---------")
"""