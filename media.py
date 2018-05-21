import webbrowser

 
class Movie():
    def __init__(ob,movie_title,poster_image,trailer_youtube):
        ob.title = movie_title
        ob.poster_image_url= poster_image
        ob.trailer_youtube_url= trailer_youtube

    def  show_trailer(ob):
        webrowser.open(ob.trailer_youtube_url)
