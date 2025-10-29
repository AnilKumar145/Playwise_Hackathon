"""
Integrated main.py demonstrating combined features of PlayWise backend engine:
- Problem 1: Playlist Engine (Doubly Linked List)
- Problem 2: Playback History (Stack with undo functionality)
This centralized script serves as an end-to-end example running core functionalities.
"""

from playlist.playlist import Playlist
from playlist.song import Song
from playback_history.playback_controller import PlaybackController
from song_rating_tree.song_rating_engine import SongRatingEngine
from song_lookup_map.lookup_map import SongLookupMap

def demonstrate_problem_1():
    """
    Demonstrates Problem 1 features: creating playlist,
    adding, moving, reversing, deleting songs, and printing results.
    """
    print("=== Problem 1: Playlist Engine ===")

    playlist = Playlist()
    playlist.add_song("Imagine", "John Lennon", 183)
    playlist.add_song("Bohemian Rhapsody", "Queen", 354)
    playlist.add_song("Hey Jude", "The Beatles", 431)

    print("\nInitial Playlist:")
    for song in playlist.get_all_songs():
        print(f"- {song.title} by {song.artist} [{song.duration}s]")

    # Move first song to last position
    playlist.move_song(0, 2)
    print("\nPlaylist after moving the first song to last:")
    for song in playlist.get_all_songs():
        print(f"- {song.title} by {song.artist} [{song.duration}s]")

    # Reverse the playlist
    playlist.reverse_playlist()
    print("\nPlaylist after reversing:")
    for song in playlist.get_all_songs():
        print(f"- {song.title} by {song.artist} [{song.duration}s]")

    # Delete song at index 1
    playlist.delete_song(1)
    print("\nPlaylist after deleting the second song:")
    for song in playlist.get_all_songs():
        print(f"- {song.title} by {song.artist} [{song.duration}s]")

def demonstrate_problem_2():
    """
    Demonstrates Problem 2 features: playing songs (adding to playlist and history),
    undoing last played song, and printing playlist state after actions.
    """
    print("\n=== Problem 2: Playback History ===")

    controller = PlaybackController()

    # Play songs through controller (adds playlist + records history)
    controller.play_song("Shape of You", "Ed Sheeran", 240)
    controller.play_song("Blinding Lights", "The Weeknd", 200)
    controller.play_song("Levitating", "Dua Lipa", 210)

    print("\nPlaylist after playing songs:")
    for song in controller.get_playlist_songs():
        print(f"- {song.title} by {song.artist} [{song.duration}s]")

    # Undo last played song (re-add it back to playlist)
    if controller.undo_last_play():
        print("\nUndo last play succeeded.")
    else:
        print("\nNo song to undo.")

    print("\nPlaylist after undoing last played song:")
    for song in controller.get_playlist_songs():
        print(f"- {song.title} by {song.artist} [{song.duration}s]")


def demonstrate_problem_3():
    """
    Demonstrates Problem 3 features: using a BST to index songs by ratings,
    showing fast insertion, search, and deletion in rating buckets.
    """
    print("\n=== Problem 3: Song Rating Tree (BST) ===")

    engine = SongRatingEngine()

    # Create Song objects (reuse Song class from playlist module!)
    song1 = Song(song_id=1, title="Imagine", artist="John Lennon", duration=183)
    song2 = Song(song_id=2, title="Bohemian Rhapsody", artist="Queen", duration=354)
    song3 = Song(song_id=3, title="Hey Jude", artist="The Beatles", duration=431)
    song4 = Song(song_id=4, title="Shape of You", artist="Ed Sheeran", duration=240)

    # Insert songs with different ratings
    engine.insert_song(song1, rating=5)
    engine.insert_song(song2, rating=4)
    engine.insert_song(song3, rating=5)
    engine.insert_song(song4, rating=3)

    print("\nSongs with rating 5:")
    songs_5 = engine.search_by_rating(5)
    for s in songs_5:
        print(f"- {s.song_id}: {s.title} by {s.artist} [{s.duration}s]")

    print("\nSongs with rating 4:")
    songs_4 = engine.search_by_rating(4)
    for s in songs_4:
        print(f"- {s.song_id}: {s.title} by {s.artist} [{s.duration}s]")

    # Delete a song from rating tree and show updated bucket
    engine.delete_song(3)  # Deletes "Hey Jude"
    print("\nSongs with rating 5 after deleting song_id 3 ('Hey Jude'):")
    songs_5_updated = engine.search_by_rating(5)
    for s in songs_5_updated:
        print(f"- {s.song_id}: {s.title} by {s.artist} [{s.duration}s]")


def demonstrate_problem_4():
    print("\n=== Problem 4: Instant Song Lookup (HashMap) ===")
    lookup = SongLookupMap()
    
    # Create and add songs to the map
    song1 = Song(song_id=1, title="Imagine", artist="John Lennon", duration=183)
    song2 = Song(song_id=2, title="Bohemian Rhapsody", artist="Queen", duration=354)
    song3 = Song(song_id=3, title="Hey Jude", artist="The Beatles", duration=431)
    song4 = Song(song_id=4, title="Shape of You", artist="Ed Sheeran", duration=240)

    # Add songs to the lookup structure
    lookup.add_song(song1)
    lookup.add_song(song2)
    lookup.add_song(song3)
    lookup.add_song(song4)

    # Instant lookup by song_id
    print("\nLookup by song ID (song_id=2):")
    result = lookup.lookup_song_by_id(2)
    if result:
        print(f"Found: {result.song_id}: {result.title} by {result.artist} [{result.duration}s]")
    else:
        print("Song not found.")

    # Instant lookup by song title
    print("\nLookup by song title ('Hey Jude'):")
    result = lookup.lookup_song_by_title("Hey Jude")
    if result:
        print(f"Found: {result.song_id}: {result.title} by {result.artist} [{result.duration}s]")
    else:
        print("Song not found.")

    # Remove a song and show that lookup fails
    lookup.remove_song(3)
    print("\nLookup by song ID (song_id=3) after removal:")
    result = lookup.lookup_song_by_id(3)
    print("Found." if result else "Song not found.")


def main():
    """
    Main driver executing demonstrations of all problem features sequentially.
    """
    demonstrate_problem_1()
    demonstrate_problem_2()
    demonstrate_problem_3()
    demonstrate_problem_4()

if __name__ == "__main__":
    main()
