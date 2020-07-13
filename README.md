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
I changed the list loop to generate a list of href with the titles available in entries folder. Seems to work, but - there is something strange with all links: it is needed to double click the link to the browser take you to the next page. 
Anywaysm the conclusion of 'Index page' was commited and pushed do GitHub. 

3. Search
Before start to work in Search, I corrected a mistake I made. I was modifying layout.html, but it wasn't the best idea - so i created title.html to inherit layout.html template and redirected title and text to title.html render the individual pages. The file layout.html now doesn't have strange lines. At last, I don't know if was this change - but that double click issue reported in 2. Index Page is not ocurring now. 
QUERY MATCHES TASK.
I had a really bat time trying to figure out how to solve this task. The first thing I tried was to use the wiki/<str:title> to receive back the POST data. But to configure this as a form, is expected that I provide a <str:title> value. So, I created another url, called just 'wiki', but to define a wiki function I not knew how to acess the data that came from form. 
After some days watching tutorial videos and reading documentation, I figured that request.POST gives the data sent by a form - and it is possible to print this data. I printed and saw that the request.POST is, in fact, a dictionary. In my investigation, was: <QueryDict: {'csrfmiddlewaretoken': ['4qSFfVCKnoDtKfQG5QQ47NH8rhTJrNok50dqpwFKWJMpYfaUh1m0r39Qg5PfOLcd'], 'q': ['CSS']}>
So, I reached the data I needed after these tests:
def wiki(request):
    print("the requested data is:", request.POST)
    post_dict = request.POST
    print("the inside data is:", post_dict['q'])
    post_data = post_dict['q']
And passed post_data as value to render the page. Probably I will only comment the excedent lines of code.  
QUERY DOESN'T MATCH TASK.
