from .playlist_engine import DoublyLinkedList
from .song import Song

class Playlist:
    """
    Interface for playlist operations using doubly linked list.
    """
    def __init__(self):
        self.playlist = DoublyLinkedList()

    def add_song(self, title, artist, duration):
        song = Song(title, artist, duration)
        self.playlist.add_song(song)

    def delete_song(self, index):
        self.playlist.delete_song(index)

    def move_song(self, from_index, to_index):
        self.playlist.move_song(from_index, to_index)

    def reverse_playlist(self):
        self.playlist.reverse_playlist()

    def get_all_songs(self):
        songs = []
        current = self.playlist.head
        while current:
            songs.append(current.song)
            current = current.next
        return songs
