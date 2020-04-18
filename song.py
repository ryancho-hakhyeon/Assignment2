from sqlalchemy import Column, TEXT, String
from base import Base


class Song(Base):

    __tablename__ = "songs_tb"
    file_name = Column(String, primary_key=True)
    title = Column(String, nullable=True )
    artist = Column(String, nullable=True)
    runtime = Column(String, nullable=True)
    album = Column(String, nullable=True)
    genre = Column(String, nullable=True)
    location = Column(String, nullable=False)

    def __init__(self, file_name: str, title: str, artist: str, runtime: str, album: str,
                 genre: str, location: str):
        self.file_name = file_name
        self.title = title
        self.artist = artist
        self.runtime = runtime
        self.album = album
        self.genre = genre
        self.location = location

    def to_dict(self):
        output = dict()
        output["file_name"] = self.file_name
        output["title"] = self.title
        output["artist"] = self.artist
        output["runtime"] = self.runtime
        output["album"] = self.album
        output["genre"] = self.genre
        output["location"] = self.location


        return output

    @staticmethod
    def from_dict(d):
        for val in ('file_name','title', 'artist', 'runtime', 'album', 'location', 'genre'):
            if val not in d.keys():
                raise ValueError("Invalid dict")

        instance = Song(file_name=d["file_name"],
                        title=d["title"],
                        artist=d["artist"],
                        runtime=d["runtime"],
                        album=d["album"],
                        genre=d["genre"],
                        location=d["location"],
                        )
        return instance

    def __str__(self):
        return f"<Song: {self.file_name}, {self.title}, {self.artist}, {self.runtime}, {self.album}" \
               f"{self.genre}, {self.location}>"