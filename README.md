# Ted Analyzer
This python application analyzes TED Talk data and recommends user which TED Talk will help him to get a positive feedback
from the audience. It also searches tweets for the '#TedTalk' and displays user the most recent ones using Twitter APIs.
Ted Talk Analyzer has Graphical User Interface which uses the paramters set by the user to filter the TED Talks as per
his/her requirements. The applications shows the output on python console and GUI both.

## How to run?

1. On running the "main.py" in python IDE, a GUI window will appear.
2. It will ask the user to provide parameters in the form of "duration" of the TED Talk, number of languages 
   in which TED Talk is converted and Tags associated to the videos.
3. The duration of video is in the form of minutes. Once the user provides the input and clicks on "Run" button,
   the code will start processing and will provide the following list of data on python IDE Console:
   A) Speaker's Occupation
   B) Number of views based on Speaker's Occupation
   C) Most popular Tags
   D) Most recent 20 Tweets containing "#TedTalk".
4. Following graphs were generated by the application:
   A) Number of Talks Vs Published_Year
   B) Number of Talks Vs Rating
   C) Number of Talks Vs Tags
   User can see these graphs using File Menu. Under the option "Graphs Data", the user can select which graph, one wants
   to see.
5. The application also recommends the list of TED Talks based on the number of user requirements and saves it in
   excel file in the current directory with the name "TedTalkRecommendations.xlsx".
