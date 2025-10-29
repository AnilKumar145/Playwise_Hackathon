from playlist.song import Song

class SongLookupMap:
    """
    Hash map for constant-time song lookup by id or title.
    Synchronizes with playlist operations for immediate update.
    """
    def __init__(self):
        # Maps song_id to Song object
        self.id_map = {}
        # Maps song title to Song object
        self.title_map = {}

    def add_song(self, song):
        """
        Add (or update) a song in both id and title maps.
        """
        if song.song_id is not None:
            self.id_map[song.song_id] = song
        # If multiple songs can have same title, use a list; here we assume unique
        self.title_map[song.title] = song

    def remove_song(self, song_id):
        """
        Remove song from both maps by song_id.
        Returns True if successful, False if not found.
        """
        song = self.id_map.pop(song_id, None)
        if song and song.title in self.title_map:
            del self.title_map[song.title]
            return True
        return False

    def lookup_song_by_id(self, song_id):
        """
        Return the Song with given song_id, or None if not found.
        """
        return self.id_map.get(song_id, None)

    def lookup_song_by_title(self, title):
        """
        Return the Song with given title, or None if not found.
        """
        return self.title_map.get(title, None)
