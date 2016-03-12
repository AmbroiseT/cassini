#Juste des fonctions pour generer la map couleur<->tag pour dessiner

def paletteStandard():
	'''
	Returns standard colors for drawing
	'''
	palette = {}
	palette["building"] = 'white'
	palette["highway"] = 'grey'
	palette["waterway"] = "blue"
	palette["landuse"] = 'green'
	return palette
