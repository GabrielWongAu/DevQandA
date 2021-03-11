# T4A2 - Full Stack Application - Part B

The purpose of the Dev Q&A website is to provide an open-source question and answer forum, where developers (e.g. aspiring developers, CS students, bootcamp students, self-learners, professional developers) can post their questions and other developers can provide helpful answers. 

The website is targeted at **questioners** (developers posting questions) and **respondents** (developers posting answers to questions). It is open to the public to read however you will need to sign up for an account in order to post a question, post an answer or upvote or downvote questions/answers.

<br>

# Links
* [Deployed Website](http://www.devqanda.ml)
* [Part A Documentation](PartA_README.md)

<br>

# How to install this app

### How to setup the Django application

**Step 1.** Install Python 3.8, python3-pip and python3.8-venv

    sudo apt install python3.8, python3.8-venv, python3-pip

**Step 2.** Clone GitHub repo to local project folder, then cd into the folder

    git clone https://github.com/GabrielWongAu/devqanda.git

    cd devqanda

**Step 3.** Create a virtual environment

We need to create a virtual env for our app to run in. Run this command in whatever folder you want to create your venv folder.

    python3.8 -m venv venv

**Step 3.** Activate the virtual environment

    # Mac/Linux
    source venv/bin/activate

    # Windows
    venv\Scripts\activate.bat - May need to add full path (c:\users\....venv\Scripts\activate.bat)
    
To escape from the virtual environment

    deactivate

**Step 4.** Install dependencies

    pip install -r requirements.txt

**Step 5.** Run Server (http://127.0.0.1:8000) CTRL+C to stop

    python manage.py runserver

**Step 6.** Create migrations 

    python manage.py makemigrations

**Step .** Run migrations 

    python manage.py migrate

<br>

### **Requirement 1: Use appropriate libraries**



### Libraries Used

#### Django libraries
* **Django-allauth** - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication. 
* **Pagination** - Django provides high-level and low-level ways to help you manage paginated data – that is, data that’s split across several pages, with “Previous/Next” links.
* **Django admin site** - Django's automatic admin interface. It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site. 
* **Django-heroku** - This is a Django library for Heroku applications that ensures a seamless deployment and development experience.

#### Built-in libraries
*	**Json** – a built-in Python package that works with JSON data.
    *	I have used the json module to decode the JSON data from the API requests.
*	**Os** – Python’s built in miscellaneous operating system interfaces 
    *	Sys and os have been used to print to the centre of the screen.

#### Other libraries
*	**Requests** – an elegant and simple HTTP library for Python, built for human beings. 
    * I have used the Python Requests module to make API get requests.
* **Bootstrap** - the most popular HTML, CSS, and JavaScript framework for developing responsive, mobile-first websites. 
* **Vue.js** - a progressive, incrementally-adoptable JavaScript framework for building UI on the web.
* **Gunicorn** - a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.
* **Psycopg2** - Psycopg is the most popular PostgreSQL database adapter for the Python programming language. 
* **Whitenoise** - With a couple of lines of config, WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service. (Especially useful on Heroku, OpenShift and other PaaS providers.)

<br>

### **Requirement 3. Project Management/ Task Delegation Methodology**

<br>

**Day 0** 

![Trello Screenshot 1](./docs/PartB/TrelloScreenshot1.png) 

![Trello Screenshot 2](./docs/PartB/TrelloScreenshot2.png) 

<br>

**Day 1** 

![Trello Screenshot 3](./docs/PartB/TrelloScreenshot3.png) 

![Trello Screenshot 4](./docs/PartB/TrelloScreenshot4.png) 

<br>

**Day 2** 

![Trello Screenshot 5](./docs/PartB/TrelloScreenshot5.png) 

![Trello Screenshot 6](./docs/PartB/TrelloScreenshot6.png) 

<br>

**Day 3** 
![Trello Screenshot 7](./docs/PartB/TrelloScreenshot7.png) 

![Trello Screenshot 8](./docs/PartB/TrelloScreenshot8.png) 

<br>

**Day 4** 

![Trello Screenshot 9](./docs/PartB/TrelloScreenshot9.png) 

![Trello Screenshot 10](./docs/PartB/TrelloScreenshot10.png) 

<br>

**Day 5** 

![Trello Screenshot 11](./docs/PartB/TrelloScreenshot11.png) 

![Trello Screenshot 12](./docs/PartB/TrelloScreenshot12.png) 

<br>

**Day 6** 

![Trello Screenshot 13](./docs/PartB/TrelloScreenshot13.png) 

![Trello Screenshot 14](./docs/PartB/TrelloScreenshot14.png) 

<br>

**Day 7** 

![Trello Screenshot 15](./docs/PartB/TrelloScreenshot15.png) 

![Trello Screenshot 16](./docs/PartB/TrelloScreenshot16.png) 

<br>

**Day 8** 

![Trello Screenshot 17](./docs/PartB/TrelloScreenshot17.png) 

<br>

**Day 9** 

![Trello Screenshot 18](./docs/PartB/TrelloScreenshot18.png) 

<br>

**Day 10** 

![Trello Screenshot 19](./docs/PartB/TrelloScreenshot19.png) 
<br>
<br>

### **Requirement 8 b): Provides evidence of user testing in the development environment**

<br>

See Requirement 9 below

<br>

### **Requirement 8 b): Provides evidence of user testing in the production environment**

<br>

![Trello Screenshot 19](./docs/PartB/ProductionTesting.png)

<br>

### **Requirement 9: Utilise a formal testing framework**

<br>

**Standard tests** 

    python manage.py test tests


**Functional tests (using Selenium)** 

    python manage.py test functional_tests

