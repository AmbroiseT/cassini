def createMagicMap():
	voie = 3.5/1000
	magic = {}
	magic['motorway']=voie*4
	magic['trunk'] = voie*4
	magic['primary'] = voie*3
	magic['secondary']=voie*2
	magic['tertiary']=voie*2
	magic['unclassified']=voie*1
	magic['residential']=voie*1
	magic['service']=voie*1
	magic['pedestrian']=voie*1
	magic['footway']=voie*0.5
	return magic
