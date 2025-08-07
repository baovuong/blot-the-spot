class Track:

    def __init__(self, id='', name='', artists=[], album=None):
        self.id = id
        self.name = name
        self.artists = artists
        self.album = album

class Artist:
    def __init__(self, id='', name=''):
        self.id = id
        self.name = name  

class Album:
    
    def __init__(self, id='', name='', tracks=[], year=0):
        self.id = id
        self.name = name 
        self.tracks = tracks
        self.year = year 

class Playlist:
    
    def __init__(self, id='', name='', tracks=[]):
        self.id = id 
        self.name = name
        self.tracks = tracks