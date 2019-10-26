
 
  # AndroidStackOverflow-Web-site
This is web site that extracts (backend) and displays recent/most voted Stack Overflow Android related questions.

### Problematic:
We want a simple way to go through the recent Android programming questions on Stack Overflow with the intention of answering them. 

### Solution: 

The solution proposed is a web site that provides the following:
  
  1- Collection of information about most recent Android questions, as well as most voted questions.
  
  2- Possibility to view the questions, and be directed to answer it on Stack Overflow. 
  
  3- Bonus: The registered users are able to receive emails each time a new question is asked. 
    (This feature might cause receiving a lot of emails. Although, it can be improved to only send question
     notifications depending on preferences of the user and his answering history, although due to time constraints I kept it as simple as possible for now.)
     
 
 ### Realization of the website:

#### Conception: 

  The website is built using the MVC design pattern supported by Django.

##### Tools: 

I chose to use Django framework to build this website, this is probably a good time for you to install the last version of django via the following command: 

``` pip install django ```

Two important tools for this website that allowed the extraction of data are:

  1-Requests:       ``` pip install requests ```  https://requests.kennethreitz.org/en/master/
  
  2- BeautifullSoup4: ``` pip install bs4 ``` https://www.crummy.com/software/BeautifulSoup/bs4/doc/

HTML/CSS obviously included, in particular I used Materialize framework (https://materializecss.com/) for some pages styling.

#### How to deploy the web site locally: 

Unfortunately, due to inconsistency of most free website hosts I didn't publish it. Although, it can be easily deployed on your machine locally, by following these steps: (I'm assuming you have python installed).

  1- If you didn't install django, requests and bs4 yet, please do.
  
  2- You can download this full directory (the zip file) and unzip it.
  
  3- Using your command prompt, navigate the unzipped file directory (The folder where manage.py is). 
  
  4- Run the following command: ``` python manage.py runserver ``` 
  
  5- On your browser visit: localhost:8000.

You can also visit the website instead: https://ysfess.herokuapp.com

Youssef Esseddiq Ouatiti.
