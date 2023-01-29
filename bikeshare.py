import time
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
    while True:
      city = input("\nEnter the name of the city to filter. 'New York City', 'Chicago' or 'Washington'\n").lower()
      if city not in ('chicago', 'new york city', 'washington'):
        print("Sorry, I didn't catch you entered.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("\Enter the month to filter.  'january' to 'june' or type 'all' \n").lower()
      if month not in ('january', 'feburary', 'march', 'april', 'may', 'june', 'all'):
        print("Sorry, I didn't catch you entered.")
        continue
      else:
        break
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nEnter the day of week to filter. 'monday' to 'sunday' or type 'all' \n").lower()
      if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        print("Sorry, I didn't catch you entered.")
        continue
      else:
        break

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
   
    df = pd.read_csv(CITY_DATA[city])    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    m_c_m = df['month'].mode()[0]
    print('Most Common Month:', m_c_m)

    # TO DO: display the most common day of week
    m_c_dow = df['day_of_week'].mode()[0]
    print('Most Common day:', m_c_dow)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    m_c_h = df['hour'].mode()[0]
    print('Most Common Hour:', m_c_h)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    m_c_ss = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', m_c_ss)


    # TO DO: display most commonly used end station
    m_c_es = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', m_c_es)

    # TO DO: display most frequent combination of start station and end station trip
    m_c_cose = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', m_c_ss, " & ", m_c_es)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    t_t_t = sum(df['Trip Duration'])
    print('Total travel time:', t_t_t/86400, " Days")

    # TO DO: display mean travel time
    m_t_t = df['Trip Duration'].mean()
    print('Mean travel time:', m_t_t/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    u_t = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', u_t)

    # TO DO: Display counts of gender
    try:
      g_t = df['Gender'].value_counts()
      print('\nGender Types:\n', g_t)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      e_y = df['Birth Year'].min()
      print('\nEarliest Year:', e_y)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      m_r_y = df['Birth Year'].max()
      print('\nMost Recent Year:', m_r_y)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      m_c_y = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', m_c_y)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def individual_data(df):
    start_data = 0
    end_data = 5
    df_length = len(df.index)
    
    while start_data < df_length:
        raw_data = input("\nDo you want to  see individual trip data? Enter 'yes' or 'no'.\n")
        if raw_data.lower() == 'yes':
            
            print("\nDisplaying only 5 rows of data.\n")
            if end_data > df_length:
                end_data = df_length
            print(df.iloc[start_data:end_data])
            start_data += 5
            end_data += 5
        else:
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
