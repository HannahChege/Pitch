# Pitch

Pitch
Built By Hannah Chege
Description
In life, you only have 60 seconds to impress someone. 1 minute can make or break you. How do we make sure that you use your 1 minute to actually say something meaningful?

Your task this week is to create an application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

The pitches are organized by category. You can have different categories like pickup lines, interview pitch, product pitch, promotion pitch.(You don't have to use these categories, you can come up with your own creative categories) 

The pitches should be arranged by category and the new posts should be displayed first.
You can view the site at:Heroku

User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:

See various news sources
Select the ones they prefer
See the top news articles from that news source
See the image, description and time the news article was created
Click on an article and read it fully from the news source
Specifications
Behaviour	Input	Output
Display news sources	On page load	List of various news sources is displayed in a list
Display tabs with news by category	On Tab link click	Clickable links to open news based on category
Display articles from a news source	Click a news source	Redirected to a page with articles from the source
Display the preview of an article	On page load	Each article displays an image,description and publication date
To Read an entire article	Click an article	Redirected to the news source's site to read the entire article
SetUp / Installation Requirements
Prerequisites
python3.6
pip
virtualenv
Cloning
In your terminal:

  $ git clone https://github.com/HannahChege/Pitch/
  $ cd Pitch
Running the Application
Creating the virtual environment

  $ python3.6 -m venv --without-pip virtual
  $ source virtual/bin/env
  $ curl https://bootstrap.pypa.io/get-pip.py | python
Installing Flask and other Modules

  $ python3.6 -m pip install Flask
  $ python3.6 -m pip install Flask-Bootstrap
  $ python3.6 -m pip install Flask-Script
  
  * In the root directory of the project folder create a file: start.sh
  * Insert the following info into it:

          python3.6 manage.py server
To run the application, in your terminal:

  $ chmod +x start.sh
  $ ./start.sh
Testing the Application
To run the tests for the class files:

  $ python3.6 manage.py tests
Technologies Used
Python3.6
Flask
License
Copyright (c) 2018 HannahChege

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
