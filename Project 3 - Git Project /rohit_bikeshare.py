<<<<<<< HEAD
# The project is coded by Rohit
# This line has been added by Refactoring branch 
||||||| ced1f63
# The project is coded by Rohit
=======
# The code was written by Rohit Kaundal on Atom Text Editor

>>>>>>> documentation
# Important points to consider
    # time.sleep() function is used to provide better readability during program execution
    #Various spaces and next line have been includes to have better readability

import os
import time
import sys
import datetime as dt
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Defining global variables for months and weekdays
months = ('january', 'february', 'march', 'april', 'may', 'june')

weekdays = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')

def get_filters():

#Ask user to specify city(ies) and filters, month(s) and weekday(s).
#Returns:
#    (str) city -name of the city(ies) to analyze
#    (str) month -name of the month(s) to filter
#    (str) day -name of the day(s) of week to filter

    os.system('cls' if os.name == 'nt' else 'clear')
    print('|'*100)
    print('-'*100)
    print("\t\t\t\t Welcome! Greetings for the day\n \t\t\t       Lets explore some US bikeshare data")
    print('-'*100)

    print("Please Select the parameters for analysis\n\n")


    # get user input for city (chicago, new york city, washington)
    while True:

        city = input ("1.   Please select the city you want to Explore: - \n     -   Chicago \n     -   New York City \n     -   Washington \n\nPlease write your choice here: ")
        city = city.lower().strip()

        if city in ('washington','new york city','chicago'):
            print("\n\nThe city to be analysed has been locked")
            break
        else:
            print("\n\nPlease enter a valid City\n")


    # get user input for month (all, january, february, ... , june)
    filter_Mon = input ("\n\nWould you like to filter based on month : \nPlease Enter :  Yes  or  No\n\n")
    filter_Mon = filter_Mon.lower()

    while filter_Mon not in ['yes', 'no']:
        filter_Mon = input("\nPlease Select a valid parameter: \nYes\nor \nNo\n")
        filter_Mon = filter_Mon.lower()

    if filter_Mon == 'yes':
        while True:
            Input_month = input ("\n2.   Please select the month for analysis: - \n     -   January\n     -   February\n     -   March\n     -   April\n     -   May\n     -   June\n     -   All\nPlease write your choice here: ")
            Input_month = Input_month.lower().strip()
            if Input_month in months:
                month = Input_month
                print("The month to be analysed is locked")
                break
            elif Input_month == 'all':
                month = None
                print("\nAll months included and locked for analysis\n")
                break
            else:
                print("\nPlease Select a valid option\n")
    elif filter_Mon == 'no':
        month = None
        print("\nNo Month based filter has been applied\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    filter_Day = input("\nWould you like to filter based on a day : \nPlease Enter Yes or No:\n")
    filter_Day = filter_Day.lower()

    while filter_Day not in ['yes', 'no']:
        filter_Day = input("Please Select a valid parameter: \nPlease Enter Yes or No:\n")
        filter_Day = filter_Mon.lower()

    if filter_Day == 'yes':
        while True:
            Input_day = input("\n3.   Please Select the day of the week: - \n     -   Monday\n     -   Tuesday\n     -   Wednesday\n     -   Thursday\n     -   Friday\n     -   Saturday\n     -   Sunday\n     -   All\nPlease write your choice here:  ")
            Input_day = (Input_day.lower()).strip()
            if Input_day in weekdays:
                day = Input_day
                print("\nThe day to be analysed has been locked\n")
                break
            elif Input_day == 'all':
                day = None
                print("\nAll days included for analysis")
                break
            else:
                print("\nPlease select a valid day option\n")
    elif filter_Day == 'no':
        day = None
        print("\nNo Day Level filter applied\n")

    print('-'*100)
    time.sleep(1)

    #Printing the Selected Choices
    if month == None and day == None:
        print("You have selected following inputs: - \n   City    =   "
                + city.capitalize())


    elif day == None:
        print("You have selected following inputs: - \n   City    =   "
                + city.capitalize(),"\n   Month   =   " + month.capitalize())


    elif month == None:
        print("You have selected following inputs: - \n   City    =   "
                + city.capitalize(),"\n   Day     =   " + day.capitalize())

    else:
        print("You have selected following inputs: - \n   City    =   "
            + city.capitalize(),"\n   Month   =   " + month.capitalize(),
            "\n   Day     =   " + day.capitalize())


    print('-'*100)
    time.sleep(2)
    return city, month, day

def load_data(city, month, day):

#Loads data for the specified city and filters by month and day if applicable.

#Args:
#    (str) city - name of the city to analyze
#    (str) month - name of the month to filter by, or "all" to apply no month filter
#    (str) day - name of the day of week to filter by, or "all" to apply no day filter
#Returns:
#    df - Pandas DataFrame containing city data filtered by month and day
#"""
    print("Loading Data. Please Wait...")
    time.sleep(2)

    # Loading data file into a dataframe.
    df = pd.read_csv(CITY_DATA[city])

    # Converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracting month day and hour of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['Start Hour'] = df['Start Time'].dt.hour


    # Filtering by month if applicable
    if month != None:
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    # Filtering by day of week if applicable
    if day != None:
        df['day_of_week'] = df['Start Time'].dt.dayofweek
        df['day_of_week'] = df
    print("Loading of Data Completed")
    print('-'*100)
    time.sleep(2)
    return df



def time_stats(df):

    #    """Displays statistics on the most frequent times of travel."""

    start_time = time.time()

    print("\n\n\n\t\t\tModule 1 - Calculating the Most Frequent Times of Travel")
    print("Please Wait...")
    time.sleep(3)
    start_time = time.time()

    # Extracting month from the Start Time column to create a month column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month

    # Finding the most common month of the year
    popular_month = df['month'].mode()[0]
    print("\n\n\nThe most popular Month is: ", (months[popular_month - 1]).capitalize())

    # Extracting week from the Start Time column to create a day_of_week column
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # Finding the most common day
    popular_day = df['day_of_week'].mode()[0]
    print("\nThe most popular day is:   ", (weekdays[popular_day]).capitalize())

    # Extracting hour from the Start Time column to create a month hour
    df['hour'] = df['Start Time'].dt.hour

    # Finding the most common hour
    popular_hour = df['hour'].mode()[0]
    print("\nThe most popular hour is:  ", popular_hour)

    print('='*100)
    print("\nThe First module is over")
    print("\nThis took %s seconds." % (time.time() - start_time))

    print('='*100)
    time.sleep(2)



def station_stats(df):

    #Displays statistics on the most popular stations and trip.
    print("\n\n\n\t\t\tModule 2 - Calculating The Most Popular Stations and Trip")
    print("Please Wait...")
    time.sleep(2)
    start_time = time.time()

    # display most commonly used start station
    print("\n\n\nThe most commonly used Start Station is                                    :     ", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("\nThe most commonly used End Station is                                      :     ", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Start-End Combination'] = df['Start Station'] + ' ' + df['End Station']
    print("\nThe most frequently combination of start station and end station trip is   :     ", df['Start-End Combination'].mode()[0])
    print('-'*100)
    print("The Second Module is over")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)
    time.sleep(2)

def trip_duration_stats(df):
    #Displays statistics on the total and average trip duration."""
    print("\n\n\n\t\t\tModule 3 - Calculating Trip Duration\n")
    print("Please Wait...")
    time.sleep(2)
    start_time = time.time()

    # display total travel time

    print("\n\n\nThe total travel time         :     ", df['Trip Duration'].sum())
    # display mean travel time
    print("\nThe mean travel time is       :     ",  df['Trip Duration'].mean())


    print('-'*100)
    print("\nThe Third Module is over")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df):
    #Displays statistics on bikeshare users."""

    print("\n\n\n\t\t\tModule 4 - Calculating User Stats\n")
    print("Please Wait...")
    time.sleep(2)
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThe count of user types are as follows: -\n",user_types)


    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print("\nThe count of Gender types are as follows: -\n",gender_count)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nEarliest year of Birth      :     ', int(df['Birth Year'].min()))
        print('\nMost Recent year of Birth   :     ', int(df['Birth Year'].max()))
        print('\nMost Common year of Birth   :     ', int(df['Birth Year'].mode()[0]))

    print('-'*100)
    print("The Fourth Module is over")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)
    time.sleep(2)

def city_data(df):

    #Defining function to display spreadsheet (5 lines at a time)
    # Taking user inputs for displaying data
    data_input = input('Would you like to city data spreadsheet?\nEnter : Yes or No\n\n')

    while data_input.lower() not in ['yes' or 'no']:
        data_input = input('\nPlease Enter Yes or No:\n\n')
        data_input = data_input.lower()

    loc = 0

    while True :
        # Loop to print 5 lines from df
        while data_input.lower() == 'yes':
            end_loc = len(df.index)
            if (loc + 5) < end_loc:
                print(df.iloc[loc : loc + 5])
                loc += 5
            else:
                print(df.iloc[loc : end_loc])
            data_input = input('\n\nWould you like to see next five line of data? \n Enter : Yes or No\n\n')

        while data_input.lower() not in ('yes','no'):
            data_input = input('\nPlease Enter Yes or No:\n\n')
            data_input = data_input.lower()

        if data_input.lower() == 'no':
            break



# Main function

def main():
    while True:
        # Calling function one by one to complete the task
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        city_data(df)

        # taking input to restart analysis or not
        Restart_Input = input("\nWould You like to see mora analysis? \n\nPlease Enter Yes or No\n\n")
        Restart_Input = Restart_Input.lower()
        while Restart_Input not in ['yes', 'no']:
            Restart_Input = input ("\nEnter a Yes or No\n")
            Restart_Input = Restart_Input.lower()
        if Restart_Input == 'no':
            # Shutting down the program
            print("\nThe Program is shutting down")
            Bye_Message = "I hope you are satisfied with the results\nThank You\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            for c in Bye_Message:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.15)
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()

if __name__ == '__main__':
    main()
