# wiki

1. Entry Page
First, I prepared the files views.py and urls.py. In views.py I defined the funcion 
title to take 'title' as argument and provide a strig as a response (Using HttpsResponse). In urls.py was cofigured the wiki/<str:title> to answer to 'title' insertions via GET. This worked to test purposes. 
Next, I defined a second version of this funcion that stores the .md text in a variable using the define function get_entry from until.py and also the title (that must be presented) - this function orders to render layout.html.
So, I went to layout.html and inserted with double curly bracers the text and the title in the proper locations. 
For the error when the page does not exist, I modified the until.py, that returned None, when not found to retur a string. 
Some issues that I faced was the comma (,), sometimes the runserver showed a sintax error because I forgot (now knew that it was needed) sometimes - also, I struggled, in view.py, to define function because I didn't knew if it was mandadory put a curlybracers or not sometimes.
The conclusion of 'Entry Page' was commited and pushed to GitHub. 

2. Index Page
I changed the list loop to generate a list of href with the titles available in entries folder. Seems to work, but