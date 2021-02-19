import pandas as pd
from tabulate import tabulate

# read the csv file and parse the dates
df = pd.read_csv("raw_data.csv", parse_dates=['SubmissionDate', 'starttime', 'endtime'])
# displaying the DataFrame
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

# Remove Time from SubmissionDate Column
df['Date'] = pd.to_datetime(df['SubmissionDate']).dt.date
print(tabulate(df[['Date', 'SubmissionDate']], headers = 'keys', tablefmt = 'psql'))


# Set start and end date
start_date = '2020-12-04'
end_date = '2020-12-07'
# Define datatype
df['Date'] = (df['Date']).astype('datetime64[D]')
#select only particular date data
df = df.loc[((df['Date'] >= start_date) & (df['Date'] <= end_date))]
# Print the dataframe
print(tabulate(df[['SubmissionDate', 'user_id', 'gadget']], headers = 'keys', tablefmt = 'psql'))

df = df.loc[((df['Date'] >= start_date))]
# Print the dataframe
print(tabulate(df[['SubmissionDate', 'user_id', 'gadget']], headers = 'keys', tablefmt = 'psql'))


# Convert Date to respective day name
df['Date'] = (df['Date']).astype('datetime64[D]')
# convert Date to day name
df['Day'] = df['Date'].dt.day_name()
df['Date'] = pd.to_datetime(df['Date']).dt.date
# Print the dataframe
print(tabulate(df[['Date', 'Day', 'user_id', 'gadget']], headers = 'keys', tablefmt = 'psql'))


# Convert Date to respective day name
df['Date'] = (df['Date']).astype('datetime64[D]')
# convert Date to day name
df['old_day'] = df['Date'].dt.day_name()
df['old_date'] = pd.to_datetime(df['Date']).dt.date
df['new_date'] = pd.to_datetime(df['old_date']).dt.date
# increase day by 1 if Sunday and by 2 if Saturday
df.loc[df['old_day'] == 'Sunday', 'new_date'] = df['old_date'] + pd.tseries.offsets.DateOffset(days=1)
df.loc[df['old_day'] == 'Saturday', 'new_date'] = df['old_date'] + pd.tseries.offsets.DateOffset(days=2)
df['new_date'] = pd.to_datetime(df['new_date']).dt.date
df['new_day'] = df['new_date'].astype('datetime64[D]').dt.day_name()
# Print the dataframe
print(tabulate(df[['old_date', 'old_day', 'new_date', 'new_day']], headers = 'keys', tablefmt = 'psql'))


# Increase Date to days, months and years
df['original_date'] = df['Date']
# increase date by 1
df['increase_date'] = df['Date'] + pd.tseries.offsets.DateOffset(days=1)
# increase date by 3 month
df['increase_month'] = df['Date'] + pd.tseries.offsets.DateOffset(months=3)
# increase date by 2 year
df['increase_year'] = df['Date'] + pd.tseries.offsets.DateOffset(years=2)
# Remove time and keep date only
df['increase_date'] = pd.to_datetime(df['increase_date']).dt.date
df['increase_month'] = pd.to_datetime(df['increase_month']).dt.date
df['increase_year'] = pd.to_datetime(df['increase_year']).dt.date
# Print the dataframe
print(tabulate(df[['original_date', 'increase_date', 'increase_month', 'increase_year']], headers = 'keys', tablefmt = 'psql'))


# read the csv file and parse the dates
df = pd.read_csv("raw_data.csv", parse_dates=['SubmissionDate', 'starttime', 'endtime'])
# Remove Date from SubmissionDate Column
df['Time'] = pd.to_datetime(df['SubmissionDate']).dt.time
print(tabulate(df[['Time', 'SubmissionDate']], headers = 'keys', tablefmt = 'psql'))


df['old_time'] = pd.to_datetime(df['SubmissionDate']).dt.time
#df['new_time'] = df['old_time'] + pd.Timedelta(hours=2)
#print(tabulate(df[['old_time', 'new_time']], headers = 'keys', tablefmt = 'psql'))

# read the csv file and parse the dates
df = pd.read_csv("raw_data.csv", parse_dates=['SubmissionDate', 'starttime', 'endtime'])
df['hour'] = df['SubmissionDate'].dt.hour
df['minute'] = df['SubmissionDate'].dt.minute
df['seconds'] = df['SubmissionDate'].dt.second
# Remove Date from SubmissionDate Column
df['Time'] = pd.to_datetime(df['SubmissionDate']).dt.time
print(tabulate(df[['Time', 'hour', 'minute', 'seconds']], headers = 'keys', tablefmt = 'psql'))


# read the csv file and parse the dates
df = pd.read_csv("raw_data.csv", parse_dates=['SubmissionDate', 'starttime', 'endtime'])
df['Time'] = pd.to_datetime(df['SubmissionDate']).dt.time
#print(df['Time'].dtype)
# increase hours by 2
df['increased_hours'] = df['SubmissionDate'] + pd.tseries.offsets.DateOffset(hours=2)
# increase minutes by 20
df['increased_minutes'] = df['SubmissionDate'] + pd.tseries.offsets.DateOffset(minutes=20)
# increase seconds by 40
df['increased_seconds'] = df['SubmissionDate'] + pd.tseries.offsets.DateOffset(seconds=40)
# Convert respective columns in datetime format and extract time only
df['increased_hours'] = pd.to_datetime(df['increased_hours']).dt.time
df['increased_minutes'] = pd.to_datetime(df['increased_minutes']).dt.time
df['increased_seconds'] = pd.to_datetime(df['increased_seconds']).dt.time
df['original_time'] = pd.to_datetime(df['SubmissionDate']).dt.time
# Print the dataframe
print(tabulate(df[['original_time', 'increased_hours', 'increased_minutes', 'increased_seconds']], headers = 'keys', tablefmt = 'psql'))