# T4A2 - Full Stack Application - Part B

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

<br>

# T4A2 - Full Stack Application - Part A Documentation
### **Requirement R1: Description of your website**

**Purpose**

The purpose of the Dev Q&A website is to provide an open-source question and answer forum, where developers (e.g. aspiring developers, CS students, bootcamp students, self-learners, professional developers) can post their questions and other developers can provide helpful answers. The website is targeted at **questioners** (developers posting questions) and **respondents** (developers posting answers to questions). It is open to the public to read however you will need to sign up for an account in order to post a question, post an answer or upvote or downvote questions/answers.

**What is important for Questioners?**

Figuring things out as a developer can sometimes feel very lonely. Especially if you are new to the industry and don’t have any friends who are developers. As someone just starting out in programming, you might get stuck on a coding problem and not know where to turn to. This is the problem Dev Q&A is trying to solve.

Alternatively you may be a CS student or bootcamp student. You may be learning programming concepts formally but still have knowledge gaps that require filling. As a developer student, you want to be able to ask questions in a safe and welcoming place. Dev Q&A provides this online space for students to ask their questions. 

**What is important for Respondents?**

As a CS student or bootcamp student, you may want to consolidate your knowledge. You may have been taught various CS concepts and theories which you understand. But you realise the best way to test your knowledge is whether you are able to teach the concepts to others. Dev Q&A allows you to solve this need of consolidating knowledge by answering other people’s questions. The forum also encourages the spirit of open source and giving back by having a leaderboard.

You may be a professional developer who is passionate about development. You may wish to give back to the community just like how others have helped you when you were starting out. Dev Q&A provides you with this avenue of helping others and giving back. 

As a respondent, you want to see how your answers are received. By users having the option to upvote and downvote answers, you will be able to see whether your questions/answers resonate with people. There will also be a leaderboard which provides a running tally of the people with the most upvoted answers.




**Functionality / Features**

* A responsive website
* Single page application
* Registration and signing in with just the required information
* Display questions with pagination
* Search functionality to search previous questions posted
* Options to add and view new questions and new answers
* Option to upvote and downvote other people’s questions and answers
* Options to view own questions and answers
* Link to about page
* Leaderboard to view top contributors/helpers

**Target audience**

The website is best suited for developers of all levels (aspiring developers, CS students, bootcamp students, self-learners, professional developers) who either have developer related questions or have developer knowledge/experience which they wish to share to the community.

**Tech stack**

* **Frontend Technologies:** HTML5, CSS, Javascript

* **Frontend Frameworks:** Vue.js

* **Backend Technologies:** Python

* **Backend Frameworks:** Django

* **Database and Database Access Library:** Sqlite3

* **Cloud Application Platform:** Heroku

<br>

### **Requirement 2: Data Flow Diagram**

![Data Flow Diagram](./docs/PartA/dataflowdigram.png) 

<br>

### **Requirement 3. Application Architecture**

![Application Architecture](./docs/PartA/applicationarchitecture.png) 

<br>

### **Requirement 4. User Stories**


![User Stories Brainstorming](./docs/PartA/UserStoriesBrainstorming.png) 

![User Stories Refinement](./docs/PartA/UserStoriesRefinement.png) 

![User Stories Revision](./docs/PartA/UserStoriesRevision.png) 

<br>

### **Requirement 5 Wireframes**

<br>

Wireframe - Home Page (Not Logged In)

![Wire Frames Home Page](./docs/PartA/Wireframes-1HomePage.png) 

<br>

Wireframe - Question Page (Logged In)

![Wire Frames Selected Question Page Logged In](./docs/PartA/Wireframes-2SelectedQuestionPageLoggedIn.png) 

<br>

Wireframe - Question Page (Not Logged In)

![Wire Frames Selected Question Page Not Logged In](./docs/PartA/Wireframes-3SelectedQuestionPageNotLoggedIn.png) 

<br>

Wireframe - Sign Up Page

![Wire Frames Sign Up Page](./docs/PartA/Wireframes-4SignUpPage.png) 

<br>

Wireframe - Sign In Page

![Wire Frames Sign In Page](./docs/PartA/Wireframes-5SignInPage.png) 

<br>

Wireframe - New Question Page (Logged In)

![Wire Frames New Question page](./docs/PartA/Wireframes-6NewQuestionPage.png) 

<br>

Wireframe - Search Page (Logged In)

![Wire Frames Search page](./docs/PartA/Wireframes-7SearchPage.png) 

<br>

Wireframe - Leaderboard Page (Logged In)

![Wire Frames Leaderboard page](./docs/PartA/Wireframes-8Leaderboard.png) 

<br>

![Wire Frames About page](./docs/PartA/Wireframes-9About.png) 

<br>
Wireframe - My Questions Page (Logged In)

![Wire Frames My Questions](./docs/PartA/Wireframes-10MyQuestions.png) 

<br>

Wireframe - My Answers Page (Logged In)

![Wire Frames My Answers](./docs/PartA/Wireframes-11MyAnswers.png) 


### **Requirement 6 - Screenshots of your Trello Board throughout the duration of the project**

**15 February**
![Trello Screenshot 1](./docs/PartA/TrelloScreenshot1.png) 

![Trello Screenshot 2](./docs/PartA/TrelloScreenshot2.png) 

<br>

**16 February** 
![Trello Screenshot 3](./docs/PartA/TrelloScreenshot3.png) 

![Trello Screenshot 4](./docs/PartA/TrelloScreenshot4.png) 

![Trello Screenshot 5](./docs/PartA/TrelloScreenshot5.png) 

<br>

**17 February**
![Trello Screenshot 6](./docs/PartA/TrelloScreenshot6.png) 

![Trello Screenshot 7](./docs/PartA/TrelloScreenshot7.png) 

<br>

**18 February**
![Trello Screenshot 8](./docs/PartA/TrelloScreenshot8.png) 

![Trello Screenshot 9](./docs/PartA/TrelloScreenshot9.png) 

<br>

**19 February**
![Trello Screenshot 10](./docs/PartA/TrelloScreenshot10.png) 

![Trello Screenshot 11](./docs/PartA/TrelloScreenshot11.png) 

<br>

**20 February** 

![Trello Screenshot 12](./docs/PartA/TrelloScreenshot12.png) 

![Trello Screenshot 13](./docs/PartA/TrelloScreenshot13.png) 


