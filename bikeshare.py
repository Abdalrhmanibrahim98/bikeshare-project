import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=['chicago','new york city','washington']
months=['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December','All']
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']

def get_filters():

    print('Hello! Ready to explore some US bikeshare data?!')

    while True:
        city=str(input('Please specify a city from Chicago, New York City and Washington: ')).lower()
        if city not in cities:
            print('City name entered is invalid')
        else:
            break

    while True:
        month=str(input('Do you want to filter by month? If yes, then type out the month. If not, type in all: ')).title()
        if month not in months:
            print('Please enter a valid month name')
        else:
            break

    while True:
        day=str(input('Do you want to filter by day? If yes, then type out the day. If not, type in all: ')).title()
        if day not in days:
            print('Please enter a valid day')
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'All':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    df['day_of_week']= df['Start Time'].dt.weekday_name
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    month_mode=df['month'].mode()[0]
    print('The most common month is ' + months[month_mode-1])
    
    print('The most common day is ' + df['day_of_week'].mode()[0])
    
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is ' + format(df['hour'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    print('The most common start station is ' + df['Start Station'].mode()[0])
    
    print('The most common end station is ' + df['End Station'].mode()[0])
    
    most_common_combination = df['Start Station'].map(str) + ' to ' + df['End Station']
    print('The most popular combination is ' + most_common_combination.mode()[0])
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    total_m, total_s = divmod(df['Trip Duration'].sum(), 60)
    total_h, total_m = divmod(total_m, 60)
    print ('Total travel time is ',total_h,' hours, ', total_m,' minutes, and ', total_s,' seconds.')
    
    mean_m, mean_s = divmod(df['Trip Duration'].mean(), 60)
    mean_h, mean_m = divmod(mean_m, 60)
    print ('Mean travel time is ',mean_h,' hours, ', mean_m,' minutes, and ', mean_s,' seconds.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    print('The user can be broken down into \n{}'.format(df['User Type'].value_counts()))
    
    if('Gender' not in df):
        print('Sorry! no available gender data for that data for that City')
    else:
        print('The genders are \n{}'.format(df['Gender'].value_counts()))
    
    if ('Birth Year' not in df):
        print('Sorry! no available birth year data for that City')
    else:
        print('The Earliest birth year is: {}'.format(df['Birth Year'].min()))
        print('The most recent birth year is: {}'.format(df['Birth Year'].max()))
        print('The most common birth year is: {}'.format(df['Birth Year'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):

    print(df.head())
    num = 0
    while True:
        view_raw_data = input('\nDo you want to view five row of the raw data? Enter "yes" or "no"\n')
        if view_raw_data.lower() != 'yes':
            return
        num = num + 5
        print(df.iloc[num:num+5])
def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()