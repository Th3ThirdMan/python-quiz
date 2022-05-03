# The Python Quiz


## Python Quiz Overview


The Python Quiz is a quiz designed to be representative of studies undertaken for the third project and is a learning vehicle to recap on information garnered in the form of a mini-quiz. The quiz contains information on python and has various trivia and light-hearted info on the programming language. It is designed to test the knowledge of those who have studied python and who enjoy coding in this language.
<br><br>

The quiz concept is a well-known one and its purpose is for a large swathe of people of all ages to interact with it. Familiarity and useability are key constructs for the quiz and it also serves to provide a fun experience for those who want to know if their knowledge is up to scratch in Python. 
<br><br>

The quiz opens with a greeting, offering two options - Start the quiz or Read the Instructions. The Instruction page gives simple instructions on how to complete the quiz and what the user will come to expect. On the Instruction page it indicates there are 10 questions available for users to attempt. It shows instructions on how to start the quiz  and how many correct questions will be totted up upon conclusion of the quiz.
<br><br>


![Image of Python Quiz](images/deployment.png)

<br>

# Planning Stage
<br>

## Identifying a Target Audience
<br>

* People who have a keen interest in quizzes, particularly aligned to that of computer languages.

* People who are interested in testing their knowledge of Python.

* People who have a penchant for getting to know fun facts relating to a history-defining programming language.

<br><br>

# User Stories
<br>

## First-time Visitors

* The terminal should display immediate information about the subject matter of the quiz.

* The terminal should deploy effectively and be easily navigable for visitors to get started in taking part in the quiz.

* The site should provide inspiration for a visitor who is interested in all things related to programming languages, not least to answer the questions, but also to provide a foundation of interest for a user surrounding the mechanics of the project deployment.


<br>

## Returning Visitors

* For returning visitors it would be good to have a larger bank of questions for a user to test themselves.

* For returning visitors an indicator of correct and incorrect answers during the quiz would be helpful.

<br>

<br>

# Design

<br>

## Application Workflow Chart

<br>

![Image of Flow Chart](images/quizflow.png)

<br>

<br>

# Features

<br>

## The Start & Welcome Page

<br>

  * The Start Page consists of ASCII Welcome text with an option to start the quiz or open up details on instruction about the quiz. 

  <br>

  ![Start Page](images/deployment.png) 

  <br>

  ## The Instructions Page

  <br>

  * The Instruction Page consists of the primary details and instructions on how to take part in the quiz.

  <br>

  ![Information Page](images/instructions.png)

  <br>

  ## The Quiz Page

  <br>

  * The Quiz Page is where a bank of 10 questions on Python are compiled and rendered.

  * The questions are multiple choice with 4 options to choose from.

  <br>

  ![Quiz Page](images/quizpage.png)

  <br><br>

  # Testing

  <br>

  # Validation

  <br>

  ![Image of PEP8 Validator](images/pep8.png)

  * No errors were recorded when entered into the official PEP8 Python Validator.

   <br>

  # Future Features

  * Include a feature that compiles and documents a High Score for users with the use of an API as per the Love Sandwiches project.

  <br><br>

  # Bugs

  <br>

  * I encountered a few issues where the site didn't meet my intended expectations. This primarily resided in the arena of responsiveness when viewing the screen at mobile level. The quiz didn't render seamlessly in a landscape view. A fix for this was to dispense with static height and width properties that were yielding limitations when added to the body.

  * Much to my chagrin, the project's quiz page featured radio buttons which wouldn't have been an initial preference for inclusion. They work as designed, but limitations in time and JavaScript learning prevented a nicer styling method whereby a user can submit answers. It wasn't necessarily a bug but I attempted many workarounds to diminish or hide their presence as I felt that they didn't quite suit the aesthetic of the quiz that I was hoping to make.

  <br><br>

  # Unfixed Bugs

  <br>

  * There were no unfixed bugs that were detected or proved to break the flow of the application.

  <br><br>

  # Deployment

  <br>

  * The project was deployed to Heroku in the following manner:

    * Sign into the Heroku website.
    * Select New, Create New App.
    * Assign a name for the App: python-quiz-project-p3.
    * Assign a Region: Europe.
    * Navigate to Settings to add Buildpacks of Python and Node.js.
    * Navigate to Deploy, Deployment Method and choose GitHub.

    <br>

    At the time of completing the project Heroku was compromised in a security attack denying users the ability to deploy via the dashboard. The prevailing fix was to deploy the application from the terminal here as follows:

    * Run the command heroku login -i and login when prompted. 
    * Run the command heroku git: remote - a python-quiz-project-p3 to create a new app with the aforementioned name as an example. 
    * This will create a new Heroku app and link it to the Gitpod terminal. 

    <br>

    There were further bugs and issues related to this process, which are addressed in the Bugs section.

    <br>

    You can find the live site here: [The Python Quiz](https://python-quiz-project-p3.herokuapp.com/)

    <br><br>

    # Content & Media

    <br>

    The content and media used during the project was sourced and referenced as follows:

    <br>

     * Lucid Flow Chart [Lucid](https://pixlr.app)
     * Knowledge Base [W3Schools](https://www.w3schools.com/)
     * Heroku Deployment Platform [Heroku](https://www.heroku.com)
     * Python Quiz Game [YouTube](https://www.youtube.com/watch?v=yriw5Zh406s)
     * Python For Beginners [YouTube](https://www.youtube.com/watch?v=kqtD5dpn9C8)