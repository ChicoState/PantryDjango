# Food Pantry [![Build Status](https://travis-ci.org/ChicoState/PantryDjango.svg?branch=master)](https://travis-ci.org/ChicoState/PantryDjango)

Chico State, like many other universities, has a food pantry for students who do not have access to enough to eat. The pantry provides food for students for free by storing donated and wholesale purchased bulk foods. We want to create a system to manage the inventory of a food pantry, as well as generate reports about the pantry's activities. We need to design a website that manages the information.


## Before UML diagram

![before UML diagram ](before.png "Before UML Diagram")


## After UML diagram (added appliance rental)


![after UML diagram ](after.png "After UML Diagram")



# Starting the web server


You need to be in the directory that contains the manage.py file (the PantryDjango directory). In the console, we can start the web server by running python manage.py runserver: 


{% filename %}command-line{% endfilename %}
```
(myvenv) ~/DjangoPantry$ python manage.py runserver
```

If you are on a Chromebook, use this command instead:

{% filename %}Cloud 9{% endfilename %}
```
(myvenv) ~/DjangoPantry$ python manage.py runserver 0.0.0.0:8080
```

If you are on Windows and this fails with UnicodeDecodeError, use this command instead:

{% filename %}command-line{% endfilename %}
```
(myvenv) ~/DjangoPantry$ python manage.py runserver 0:8000
```

Now you need to check that your website is running. Open your browser (Firefox, Chrome, Safari, Internet Explorer or whatever you use) and enter this address:

{% filename %}browser{% endfilename %}
```
http://127.0.0.1:8000/
```
