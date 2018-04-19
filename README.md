#Youtube Analyzer Project
#####By Emil Meireles

In this repository you will find the Files to the Youtube Analyzer Final Project for SI 206
You will be running this program from main.py but need to have data.py imported to main and in the same directory 

##What does this Program do?

This Application compares youtubers based on different metrics such as subscribers,views, social blade rank etc...

####Sources:
	-Social Blade (Subscriber Information and other updated Youtuber information)
	-Youtube API (Comments, Various IDs to pinpoint videos,channels, comments, etc.)
	-Microsoft AZURE API (Sentiment Analysis)
	-Twitter API (Tweets)

##Important Points of the Function
	-data.py runs off of two functions: init_db() and pop_table()
	-init_db()
		-Creates SQL Database of all necesary information
	-pop_table()
		-Populates database for use by main.py

##Running the Program 
To Run this program you will need to **install**:
	-Dash from Plotly
	-OAuth
	-Beautiful Soup
	-NLTK
	-Plotly

You will also need to **import**:
	-sqlite3
	-requests
	-time

If all goes well you will be prompted to enter in your Youtubers for comparison

From there you can enter an option to run the application. (*please see bleow for options*)

###Options:

There are 2 types of Graphs: Bar and Box. They each have there own subset of data

Below are the subsets of data and below each option is how to call it.  

**Bar Graph**:
	-Total Subs
		-bar TotalSubs
	-Total Views in the last 30 Days
		- bar TotalView30
	-Total Subs in the Last 30 days
		- bar TotalSubs30
	-Total Views
		-bar TotalViews

**Box Plot**:
	-Twitter Senitment Analysis
		-box Twitter
	-Comment Sentiment Analysis 
		-box Comments 

*Each option launches a NEW Dash Application, therefore to get a new comparison kill the current application and run main.py with a new option*


