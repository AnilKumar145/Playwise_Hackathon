from .stack import Stack
from playlist.song import Song  # Reuse Song class from Problem 1's playlist module


class PlaybackHistory:
    """
    Manages playback history using a stack.

    Time Complexity:
    - record_played_song: O(1)
    - undo_last_play: O(1) + playlist add_song complexity
    Space Complexity: O(N) for N recorded songs
    """

    def __init__(self):
        self.history_stack = Stack()

    def record_played_song(self, song: Song):
        """
        Record a song as recently played by pushing it onto the history stack.
        """
        self.history_stack.push(song)

    def undo_last_play(self, playlist):
        """
        Undo the last played song by popping from history stack
        and re-adding it to the given playlist.

        Args:
            playlist (Playlist): Playlist instance to re-add song.

        Returns:
            bool: True if undo succeeded, False if no songs to undo.
        """
        last_song = self.history_stack.pop()
        if last_song is None:
            return False
        playlist.add_song(last_song.title, last_song.artist, last_song.duration)
        return True
