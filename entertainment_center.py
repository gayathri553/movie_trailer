import media
import fresh_tomatoes
"""
declare favorite movies, with 4 args each:
title (movie's title)
poster_image_url (url to poster image)
trailer_youtube_url (url to youtube trailer)
"""

print("Content-type:text/html \n")

TP = media.Movie("Tarezameen Par", "http: // www.bollylocations.com /
                 clix_images/201701040601560.Taare % 20Zameen % 20Par.jpg",
                 "tn_2Ie_jtX8")
TI = media.Movie("Three idiots", "http: // st1.bollywoodlife.com/wp-content/,
                 uploads/photos/3-idiots-movie-poster-201601-657872.jpg",
                 "xvszmNXdM4w")
SB = media.Movie("Sathamanam Bhavathi",
                 "https://i.ytimg.com/vi/paD2oJXdZEE/maxresdefault.jpg",
                 "LG_qGiHqmIY")
MB = media.Movie("Mayabazar",
                 "http://www.idlebrain.com/images4/wp-27mayabazaarcthumb.jpg",
                 "Q9M6QW0MH6E")
# assign individual movies to mylist
mylist = [TP, TI, SB, MB]
# call movie trailer page method and pass mylist  and sorting option
fresh_tomatoes.open_movies_page(mylist)
