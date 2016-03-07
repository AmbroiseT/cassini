import math

class Echelle:
	carte = None
	#Facteur multiplicatif pour faire une projection des coords
	mult = 40000/360
	#Facteur correctif pour la longitude(a calculer en fonction de la latitude)
	corr = 1
	
	maxX = 500
	maxY = 500
	
	facteurKmPx = 1

	largeurKm = 0
	hauteurKm = 0


	def __init__(self, carte, maxX=500):
		self.maxX = maxX
		self.carte = carte
		self.corr = math.cos(self.carte.maxlat)
		self.largeurKm = self.convertLatitudeToKm(self.carte.maxlat - self.carte.minlat)
		self.hauteurKm = self.convertLongitudeToKm(self.carte.maxlon -self.carte.minlon)
		self.facteurKmPx = self.maxX/self.largeurKm
		self.maxY = self.convertKmToPx(self.hauteurKm)
	
	def convertLatitudeToKm(self, latitude):
		return latitude*self.mult
	def convertLongitudeToKm(self, longitude):
		return longitude*self.mult*self.corr
	def convertKmToPx(self, km):
		return self.facteurKmPx * km
	def describe(self):
		print("Echelle de la carte")
		print("Facteur multiplicatif = {}".format(self.mult))
		print("Facteur correctif = {}".format(self.corr))
		print("Largeur Km = {}, hauteur Km = {}".format(self.largeurKm, self.hauteurKm))
		print("MaxX = {}, maxY={}".format(self.maxX, self.maxY))
		print("Facteur Km to Px : {}".format(self.facteurKmPx))
