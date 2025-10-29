from playlist.playlist import Playlist
from playlist.song import Song
from .playback_engine import PlaybackHistory


class PlaybackController:
    """
    Controls playback actions integrating Playlist and PlaybackHistory.

    Provides user-level operations: play_song, undo_last_play.
    """

    def __init__(self):
        self.playlist = Playlist()
        self.history = PlaybackHistory()

    def play_song(self, title, artist, duration):
        """
        Play a song: add to playlist and record in playback history.
        """
        song = Song(title, artist, duration)
        self.playlist.add_song(title, artist, duration)
        self.history.record_played_song(song)

    def undo_last_play(self):
        """
        Undo last played song: re-add last played song from history to playlist.
        Returns True if successful, False otherwise.
        """
        return self.history.undo_last_play(self.playlist)

    def get_playlist_songs(self):
        """
        Return current songs in the playlist.
        """
        return self.playlist.get_all_songs()
