SECONDS_IN_A_MINUTE = 60
SECONDS_IN_AN_HOUR = SECONDS_IN_A_MINUTE * 60
SECONDS_IN_A_DAY = SECONDS_IN_AN_HOUR * 24

total_seconds = int(input("Please enter total number of seconds: "))
seconds_remaining = total_seconds

days = total_seconds // SECONDS_IN_A_DAY
seconds_remaining %= SECONDS_IN_A_DAY

hours = seconds_remaining // SECONDS_IN_AN_HOUR
seconds_remaining %= SECONDS_IN_AN_HOUR

minutes = seconds_remaining // SECONDS_IN_A_MINUTE
seconds_remaining %= SECONDS_IN_A_MINUTE

seconds = seconds_remaining

print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")