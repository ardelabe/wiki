# wiki

INTRODUCTION
This is a report of my issues trying to solve the problem set 01 from the cs50w - Edx/Harvard course. The description of what the web-app must do can be found at https://cs50.harvard.edu/web/2020/projects/1/wiki/. 

1. ENTRY PAGE
First, I prepared the files views.py and urls.py. In views.py I defined the funcion 
title to take 'title' as argument and provide a strig as a response (Using HttpsResponse). In urls.py was cofigured the wiki/<str:title> to answer to 'title' insertions via GET. This worked to test purposes. 
Next, I defined a second version of this funcion that stores the .md text in a variable using the define function get_entry from until.py and also the title (that must be presented) - this function orders to render layout.html.
So, I went to layout.html and inserted with double curly bracers the text and the title in the proper locations. 
For the error when the page does not exist, I modified the until.py, that returned None, when not found to retur a string. 
Some issues that I faced was the comma (,), sometimes the runserver showed a sintax error because I forgot (now knew that it was needed) sometimes - also, I struggled, in view.py, to define function because I didn't knew if it was mandadory put a curlybracers or not sometimes.
The conclusion of 'Entry Page' was commited and pushed to GitHub. 

2. INDEX PAGE
I changed the list loop to generate a list of href with the titles available in entries folder. Seems to work, but - there is something strange with all links: it is needed to double click the link to the browser take you to the next page. 
Anywaysm the conclusion of 'Index page' was commited and pushed do GitHub. 

3. SEARCH
Before start to work in Search, I corrected a mistake I made. I was modifying layout.html, but it wasn't the best idea - so i created title.html to inherit layout.html template and redirected title and text to title.html render the individual pages. The file layout.html now doesn't have strange lines. At last, I don't know if was this change - but that double click issue reported in 2. Index Page is not ocurring now. 

QUERY MATCHES TASK.
I had a really bad time trying to figure out how to solve this task. The first thing I tried was to use the wiki/<str:title> to receive back the POST data. But to configure this as a form, is expected that I provide a <str:title> value. So, I created another url, called just 'wiki', but to define a wiki function I not knew how to acess the data that came from form. 
After some days watching tutorial videos and reading documentation, I figured that request.POST gives the data sent by a form - and it is possible to print this data. I printed and saw that the request.POST is, in fact, a dictionary. In my investigation, was: <QueryDict: {'csrfmiddlewaretoken': ['4qSFfVCKnoDtKfQG5QQ47NH8rhTJrNok50dqpwFKWJMpYfaUh1m0r39Qg5PfOLcd'], 'q': ['CSS']}>
So, I reached the data I needed after these tests:
def wiki(request):
    print("the requested data is:", request.POST)
    post_dict = request.POST
    print("the inside data is:", post_dict['q'])
    post_data = post_dict['q']
And passed post_data as value to render the page. Probably I will only comment the excedent lines of code.  

QUERY DOESN'T MATCH TASK.
This part was very pleasant to develop. Not in this order: I created a url to results and a results.html. The corresponding funcion in view was an alteration of wiki. 
Wiki, now, has (a) takes the dict from POST and saves in post_data; (b) loops into the list of saved entries; (c) if statement checks if the capitalized post_data is equal to an entry - if True, reders the page; (d) elif cheks if post_data.upper() is equal to an entry - if True, renders de page; (e) elif checks if there is a substring in post_data that matches entry (independent of case) and populates a list if True; (f) at the end, if only the list was populated, the wiki function renders results.html with links corresponding the list. 

4. NEW PAGE
I had some trouble with this part, but at the end I could make things work. I used the method .get() to retrieve data from the request-dict as bonus of my research - because the initial mistake was not make an if statement to execute part of the code only when a form is submitted. After I corrected this part, all worked fine. The code still needs to be changed - there is two requisites to implement: (a) present error message if the page that the user is trying to create already exists; (b) redirect to the new entry's page on submit.

REDIRECT TO THE NEW ENTRY. 
Ok, I'll confess something - I don't really master the hability of working with GET and POST. So, to do this part, I only copied the part of code that renders the page from index function - it means that the page is 'redirected' - but not really... **it takes to the created page, but in the url /create**. That was predictable, because I'm spending a lot of time figuring out how to deal with some issues in views.py, and the urls.py is not generating many issues. I'll not gonna change it for now.

ERROR MESSAGE
I learned some new stuff with this part of New Page. Fist, I created conditions and loop inside views.create to identify when the user is trying to create a page with a title that already exists. I created a counter variable that turns 0> when 'if' finds an existing title. When it doesn't find: save and render new page. When find: don't save, and render create with error message. **There are capitalization issues**. 

