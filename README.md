

Project : Data Analytics on Bikeshare Data using Python				

Dated   : 07-03-2021
 
Project Overview:

A simple analytical project on bikeshare dataset using Python programming language and Pandas library.


Dataset:

3 datasets of bikeshare data from three major U.S. cities namely New York city, Chicago, and Washington
* chicago.csv - Stored in the data folder, the chicago.csv file is the dataset containing all bikeshare information for the city of Chicago provided by Udacity.
* new_york_city.csv - Dataset containing all bikeshare information for the city of New York provided by Udacity.
* washington.csv - Dataset containing all bikeshare information for the city of Washington provided by Udacity. Note: This does not include the 'Gender' or 'Birth Year' data.


Running this script:

I used PyCharm software on Mac to prepare and test this python script.
Used 3 libraries Pandas, Numpy and Time.


Program Script Details:

The program script takes user input for the cities, month and day for which the user wants to view data. 
Users can choose one city at a time, each month or all months, and each day of the week or all days in the week. 
It also asks if the user would like to view the first 5 rows of the dataset. And, the next five and so on until the user opts out of the function.
Finally, the user is prompted with the choice of restarting the program or not.


Requirements:

* Language:  Python 3.6.6 or above
* Libraries: pandas, numpy, time


Statistics Computed:

In this project, we’ll write code to provide the following information:


#1 Popular times of travel (i.e., occurs most often in the start time)
* most common month
* most common day of week
* most common hour of day

#2 Popular stations and trip
* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration
* total travel time
* average travel time

#4 User info
* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago)