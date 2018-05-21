print("Content-type:text/html \n")
import webbrowser
import os
import re

main_page_start = '''<html>
<head>
    <title>Movie Trailers</title>
</head>
<body>

    <script src="https://code.jquery.com/jquery-1.12.3.min.js" integrity="sha256-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ="
        crossorigin="anonymous"></script>
        <link href="https://fonts.googleapis.com/css?family=Courgette" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script>
        $(document).ready(function () {
            $("#myVideo").on("hidden.bs.modal", function () {
                $("#myframeY").attr("src", "#");
            })
        })
        function changeVideo(vId) {
            var iframe = document.getElementById("myframeY");
            iframe.src = "https://www.youtube.com/embed/" + vId;
            $("#myVideo").modal("show");
        }
    </script>
    <style>
        .container {
            flex-wrap: wrap;
            display: flex;
            flex: 10%;
            justify-content: center;
            
        }

        body {
            margin: 0;
        }

        header {
            color: lightseagreen;
            background-color: rgb(35, 72, 142);
            height: 1.5cm;
            margin: 0px, 0px, 0px, 0px;
            text-align: center;
            font-size: 40px;
            font-family: 'comic sans ms', cursive;
        }

        img {
            height: 400px;
            width: 400px;
        }
        .one:hover,
        .two:hover,
        .three:hover,
        .four:hover
        {
            background-color: rgb(30, 128, 255);
            visibility: visible;
            cursor: pointer;
            border-radius:5%;
        }

        .one {

            padding-top: 15px;
            padding-left: 40px;
            padding-bottom: 30px;
            padding-right: 40px;
            background-color: white;
        }
        .two {
            padding-top: 15px;
            padding-left: 40px;
            padding-bottom: 30px;
            padding-right: 40px;
            background-color: white;
        }
        .three {
            padding-top: 15px;
            padding-left: 40px;
            padding-bottom: 30px;
            padding-right: 40px;
            background-color: white;
        }
        .four {
            padding-top: 15px;
            padding-left: 40px;
            padding-bottom: 30px;
            padding-right: 40px;
            background-color: white;
        }
    </style>
    <title>Movie Trailers</title>
    <header><i class="fa fa-film"></i>  Movie Trailers  <i class="fa fa-film"></i></header>
    <main>
        <div class="container">
'''
main_page_remain='''
     
        </div>       
        <div class="modal fade" id="myVideo" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-body">
                        <iframe id="myframeY" width="550" height="350" src="" frameborder="0" allowfullscreen></iframe>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>

</html>
'''
movie_title_content='''<div class="one" onclick="changeVideo('{trailer_youtube_url}')">
                <img  src="{poster_image_url}">
                <figcaption style="text-align: center; color: white;">
                    <b>{title}</b>
                </figcaption>
            </div>
'''
def create_movie(mylist):
    content = ''
    for movie in mylist:
        content +=movie_title_content.format(
            title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_url=movie.trailer_youtube_url
        )
    return content

def  open_movies_page(mylist):
    output_file = open('fresh_tomatoes.html','w')

    rendered_content = create_movie(mylist)

    output_file.write(main_page_start + rendered_content+main_page_remain)
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
