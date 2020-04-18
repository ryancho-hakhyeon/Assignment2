from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base

from song import Song


class SongManager:

    def __init__(self, audio_library_db):

        if audio_library_db is None or audio_library_db == "":
            raise ValueError(f"Audio Library database [{audio_library_db}] not found")

        engine = create_engine('sqlite:///' + audio_library_db)
        Base.metadata.bind = engine
        self._db_session = sessionmaker(bind=engine)

    def add_song(self, new_song: Song):

        session = self._db_session()
        session.add(new_song)

        session.commit()

        file_name = new_song.file_name
        session.close()

        return file_name

    def get_song(self, file_name):
        if file_name is None or type(file_name) != str:
            raise ValueError("Invalid Title")
        session = self._db_session()

        song = session.query(Song).filter(
            Song.file_name == file_name).first()
        session.close()
        return song

    def get_all_songs(self):
        session = self._db_session()
        all_songs = session.query(Song).all()
        session.close()

        return all_songs

    def delete_song(self, file_name):

        session = self._db_session()

        song = session.query(Song).filter(
                Song.file_name == file_name).first()
        if song is None:
            session.close()
            raise ValueError("Student does not exist")

        session.delete(song)
        session.commit()

        session.close()

    def delete_all_songs(self):
        """ Delete all students from the database """
        session = self._db_session()

        session.query(Song).delete()
        session.commit()

        session.close()