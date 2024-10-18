import eyed3


import os

class Song:
    def __init__(self, artist, album, album_artist, title, track_num):
        """
        Initialize a Song object.

        Args:
            artist (str): The artist of the song.
            album (str): The album the song belongs to.
            album_artist (str): The artist of the album (may differ from song artist).
            title (str): The title of the song.
            track_num (int): The track number of the song in the album.
        """
        self.artist = artist
        self.album = album
        self.album_artist = album_artist
        self.title = title
        self.track_num = track_num

    def __str__(self):
        """
        Return a string representation of the Song.

        Returns:
            str: A formatted string containing the song's information.
        """
        return f"{self.track_num}. {self.title} by {self.artist} (Album: {self.album} by {self.album_artist})"

    def __repr__(self):
        """
        Return a string representation of the Song for debugging.

        Returns:
            str: A string representation of the Song object.
        """
        return f"Song(artist='{self.artist}', album='{self.album}', album_artist='{self.album_artist}', title='{self.title}', track_num={self.track_num})"

    def save(self, filename):
        """
        Save the Song object to a JSON file.

        Args:
            filename (str): The name of the file to save the song information to.

        Raises:
            IOError: If there's an error writing to the file.
        """
        data = {
            "artist": self.artist,
            "album": self.album,
            "album_artist": self.album_artist,
            "title": self.title,
            "track_num": self.track_num
        }
        pass

    @classmethod
    def load(cls, filename):
        """
        Load a Song object from a JSON file.

        Args:
            filename (str): The name of the file to load the song information from.

        Returns:
            Song: A new Song object with the loaded data.

        Raises:
            FileNotFoundError: If the specified file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file {filename} does not exist.")

        pass

def main():



    import eyed3

    audiofile = eyed3.load("song.mp3")
    audiofile.tag.artist = "Token Entry"
    audiofile.tag.album = "Free For All Comp LP"
    audiofile.tag.album_artist = "Various Artists"
    audiofile.tag.title = "The Edge"
    audiofile.tag.track_num = 3

    audiofile.tag.save()





if __name__ == '__main__':
    main()

