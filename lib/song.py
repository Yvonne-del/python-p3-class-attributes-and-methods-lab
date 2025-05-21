class Song:
    count = 0
    artists = []
    genres = []
    genre_count ={}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, song):
        cls.genres.append(song)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

            
song1 = Song('333', 'Iniko', 'pop')  
song2 = Song('black swan', 'BTS', 'kpop')
song3 = Song('jericho', 'Iniko', 'pop')
song4 = Song('permission to dance', 'BTS', 'kpop')
song5 = Song('anxiiety', 'Chris Brown', 'hip-hop')
song6 = Song('ps5', 'Yeongjun', 'kpop') 
song7 = Song('pinochio', 'Iniko', 'pop') 
song8 = Song('leave the door open', 'Bruno Mars', 'jazz') 

print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)