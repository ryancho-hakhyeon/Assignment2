from flask import Flask, request
from song_manager import SongManager
from song import Song
import json

app = Flask(__name__)

song_mgr = SongManager('audio_library_db.sqlite')


@app.route('/song', methods=['POST'])
def add_song():
    content = request.json

    try:
        song = Song(content['file_name'],
                    content['title'],
                    content['artist'],
                    content['runtime'],
                    content['album'],
                    content['genre'],
                    content['location'])
        song_mgr.add_song(song)
        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )

    return response

@app.route('/song/<string:file_name>', methods=['GET'])
def get_song(file_name):
    try:
        song = song_mgr.get_song(file_name)
        if song is None:
            raise ValueError(f"Song {file_name} does not exist")

        response = app.response_class(
            status=200,
            response=json.dumps(song.to_dict()),
            mimetype='application/json'
        )
        return response
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
        return response


@app.route('/song/titles', methods=['GET'])
def get_all_titles():
    """ Return a list of all student names    """
    titles = song_mgr.get_all_songs()

    response = app.response_class(
            status=200,
            response=json.dumps([s.to_dict() for s in titles]),
            mimetype='application/json'
    )

    return response


@app.route('/song/<string:file_name>', methods=['DELETE'])
def delete_student(file_name):
    try:
        song_mgr.delete_song(file_name)
        response = app.response_class(
                status=200
        )
    except ValueError as e:
        response = app.response_class(
                response=str(e),
                status=404
        )
    return response


@app.route('/song/all', methods=['DELETE'])
def delete_all_songs():
    try:
        song_mgr.delete_all_songs()
        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
    return response


if __name__ == "__main__":
    app.run(debug=True)