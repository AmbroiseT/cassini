def createMagicMap():
    way = 3.5 / 1000
    return {'motorway': way * 4, 'trunk': way * 4, 'primary': way * 3, 'secondary': way * 2, 'tertiary': way * 2,
             'unclassified': way * 1, 'residential': way * 1, 'service': way * 1, 'pedestrian': way * 1,
             'footway': way * 0.5}