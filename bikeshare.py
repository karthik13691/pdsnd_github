import time
import numpy as np
import pandas as pd


CITY_DATA = {'chicago': "chicago.csv", 'new york city': "new_york_city.csv", 'washington': "washington.csv"}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
`
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hey! Welcome to Udacity's Python for Data Science Nanodegree project #2")
    print("Let's explore some US bikeshare data!")

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    city = ''

    while city not in CITY_DATA.keys():
        city = input("Which city data you like to look at? \n Chicago, New York City or Washington?").lower()
        # lower() is used to standardize the input
        if city not in CITY_DATA.keys():
            # tell the user off
            print("{} doesn't appear to in our database, please enter a city name mentioned in the above".format(city))

    print("\nYou have chosen {} to view.".format(city.title()))

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = ''

    while month not in month_list:
        month = input("Which month do you want to view january, february, march, april, may, june? or all").lower()
        if month not in month_list:
            # Inform the user to refine their input according to available datasets
            print("We don't have data for the month of {}, please enter a month mentioned in the above".format(month))

    print("\nYou have chosen {} .".format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''

    while day not in day_list:
        print("Which day in the week would you like to view (Eg: sunday, monday, etc. enter 'all' for no day filter)")
        day = input().lower()

        if day not in day_list:
            print("\nInvalid input. Please reform your input to one of the accepted formats.")

    print("\nYou have decided to view {}.".format(day.title()))

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['com_month'] = df['Start Time'].dt.month
    common_month = df['com_month'].mode()[0]
    print("The most number of trips were in month#: {}".format(common_month))

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    common_day = df['day_of_week'].mode()[0]
    print("Most trips are on {}".format(common_day))

    # TO DO: display the most common start hour
    df['com_hour'] = df['Start Time'].dt.hour
    common_hour = df['com_hour'].mode()[0]
    print("The most frequent hour of use is: {}:00".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("\nMost trips start from:\n {}".format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("\nStation with most trip destination is:\n {}".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df["popular_trip_route"] = df["Start Station"] + " to " + df["End Station"]
    popular_trip_route = df['popular_trip_route'].mode()[0]
    print("\nMost popular route is:\n {}".format(popular_trip_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is: \n{} hours or {} days".format(round(total_travel_time / (60 * 60), 2), round(total_travel_time / (60 * 60 * 24), 2)))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nThe Mean travel time is: {} minutes".format(round(float(mean_travel_time / 60), 2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_type = df['User Type'].value_counts()
        print("bikeshare user count is:\n{}".format(user_type))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_ratio = df['Gender'].value_counts()
        print("\nThe Male to Female user ratio is:\n{}".format(gender_ratio))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("\nThe oldest user was born in {}".format(int(df['Birth Year'].min())))
        print("The youngest user was born in {}".format(int(df['Birth Year'].max())))
        print("Most bikeshare users in this city are born in {}".format(int(df['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def raw_data(df):
    # TO displays 5 rows of data from the csv file for the selected city
    more_data = ''
    counter = 0
    while more_data not in ['yes', 'no']:
        more_data = input("\nDo you wish to view the raw data? Enter yes or no").lower()
        # The raw data is displayed if user chooses to view it
        if more_data == "yes":
            print(df.head())
        elif more_data not in ['yes', 'no']:
            print("\nInvalid input, Please reform your input to a yes or no.")

    # Extra while loop here to ask user if they want to continue viewing data
    while more_data == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        more_data = input().lower()
        # If user opts for it, this displays next 5 rows of data
        if more_data == "yes":
            print(df[counter:counter + 5])
        elif more_data != "yes":
            break

    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? \nEnter yes to restart or no to exit.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
