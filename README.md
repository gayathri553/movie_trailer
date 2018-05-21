# movie_trailer
A simple movie trailer Project for Udacity's fullstack nano degree program.It simply explains about the movie object class in python to display a static web page.By using this website we can view our movie trailers and play the videos within that window.
In this folder we create three python files(entertainment_center.py,fresh_tomatoes.py,media.py)
Movie class in present in media.py module which creates data structure to store our favourite movies,which includes movie name,movie poster url,movie trailer video url.
In entertainment_center.py module we import media,fresh_tomatoes which are not inbuilt libraries and also we create multiple instances of the Movie class,we store them in the form of lists.
In python module fresh_tomatoes.py we import os,webbrowser,re and it contains open_movies_page method which contains one argument to be passed (ie,list that we have already created in entertainment_center.py) this method  creates a new html page(ie,fresh_tomatoes.html).  
Running the program:
 -save the three python modules 
 -Then run the entertainment_center.py then it creates the html page named fresh_tomatoes.html and which is opened in the browser directly.
 -python entertainment_center.py
Download Git bash 
Project files need to be uploaded in Git 
Open Git bash 
   Then run commands in this respository in the path that your project files are present
   git init(.git folder is created(not a sharable folder))
   git clone(to upload this file we use the clone link)
   git status (It gives the present status)
   git add --all
   git commit -m "adding files"
   git push origin master
We use Python for buliding this project 

   
   
   
