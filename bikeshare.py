import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('What city your are interested in?\nType either:\nc for Chicago, nyc for New York City or w for Washington\n')
    city = city.lower()
    while city not in ['c', 'nyc', 'w']:
        city = input('Incorrect input!\n Type either:\nc for Chicago, nyc for New York City or w for Washington\n')
        city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('What month your are interested in?\nType either:\nall, january, february, ... or june\n')
    month = month.lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may','june']:
        month = input('Incorrect input!\nType either:\nall, january, february, ... or june\n')
        month = month.lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('What day your are interested in?\nType either:\nall, monday, tuesday, ... or sunday\n')
    day = day.lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('Incorrect input!\nType either:\nall, monday, tuesday, ... or sunday\n')
        day = day.lower()

    print('-'*40)
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

    if city == 'c':
        df = pd.read_csv('chicago.csv')
    elif city == 'nyc':
        df = pd.read_csv('new_york_city.csv')
    elif city == 'w':
        df = pd.read_csv('washington.csv')
            
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.strftime("%B")
    df['month'] = df['month'].str.lower() 
    df['weekday'] = df['Start Time'].dt.strftime("%A")
    df['weekday'] = df['weekday'].str.lower() 
    df['hour'] = df['Start Time'].dt.hour
    if month == 'all':
        return df
    else:
        df = df[df.month == month]
    if day == 'all':
        return df
    else: 
        df = df[df.weekday == day]
    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_weekday = df['weekday'].mode()[0]

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('The most common month: {}\nThe most common day of the week: {}\nThe most common start hour: {}'.format(popular_month.capitalize(), popular_weekday.capitalize(), popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = (df['Start Station'] + ' + ' + df['End Station']).mode()[0]
    
    print('The most common start station: {}\nThe most common end station: {}\nThe most common combination of start station and end station trip: {}'.format(popular_start, popular_end, popular_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    
    print('Total travel time: {} min\nMean travel time: {} min\n'.format(total_time, round(mean_time, 1)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    else:
        print('No gender data in washington')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        yob_earliest = df['Birth Year'].min()
        yob_recent = df['Birth Year'].max()
        yob_common = df['Birth Year'].mode()[0]
        print('Earlierst date of birth: {}\nMost recent date of birth: {}\nMost common date of birth: {}\n'.format(int(yob_earliest), int(yob_recent), int(yob_common)))
    else:
        print('No birth year data in washington')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Provides the option to display the first 5 rows of the filtered dataframe.
    With a short input (yes) the user can display 5 more rows"""
    i = 0
    raw = input("Do you want to have a look at the first 5 rows of the dataframe?\nType yes oder no: ").lower() 
        
    # TO DO: convert the user input to lower case using lower() function

    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5])
            # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input('Do you want to have a look at the next 5 rows of the dataframe?\nType yes oder no: ').lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
