import webbrowser


class Movie():
    """ Class for representing a movie """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """ Inits a Movie object
        Args:
        title = a string of the movie's title
        poster_image_url = a string containing a URL to a poster image
        trailer_youtube_url = a string containing a youtube
        URL of the movie's trailer
        """

        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens trailer in a web browser """
        webrowser.open(self.trailer_youtube_url)
