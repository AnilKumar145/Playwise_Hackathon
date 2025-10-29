class Song:
    """
    Represents a Song entity in the playlist.
    Attributes:
        song_id (int/str, optional): Unique song identifier. Defaults to None.
        title (str): Song title.
        artist (str): Artist name.
        duration (int): Duration in seconds.
    """
    def __init__(self, title: str, artist: str, duration: int, song_id=None):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration
