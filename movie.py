class Movie():
    """ Class to define what each movie needs are
    Attributes:
        title (str): The original `title`.
        poster_image_url (str): The poster width: 185 height: 278.
        trailer_youtube_url (str): Youtube link to trailer. """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
