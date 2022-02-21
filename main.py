from collections import Counter


# transfer the time format to a number of minutes for needed calculations
def time_to_minutes(given_format):
    years = int(given_format[:4]) * 60 * 24 * 365
    months = int(given_format[5:7]) * 60 * 24 * 30
    days = int(given_format[8:10]) * 60 * 24
    hours = int(given_format[11:13]) * 60
    minutes = int(given_format[14:16])
    total_time = years + months + days + hours + minutes
    return total_time


# transfer the time format to minutes to calculate the exact time of sleep
def time_of_sleep(given_format):
    minutes = int(given_format[14:16])
    return minutes


def main():
    # guard_data will be the file with data
    path = input("please put the path to the file: ")
    with open(path) as guard_data:
        data_lines = guard_data.read().splitlines()
    guard = ""
    sleep_count_start = 0
    sleep_time_start = 0
    guard_10 = [0]  # amount of sleep in minutes
    guard_99 = [0]
    for line in data_lines:
        if "#10" in line:
            guard = "#10"
        elif "#99" in line:
            guard = "#99"
        if "falls asleep" in line:
            sleep_count_start = time_to_minutes(line[1:17])
            sleep_time_start = time_of_sleep(line[1:17])
        if "wakes up" in line:
            sleep_count_end = time_to_minutes(line[1:17])
            sleep_time_end = time_of_sleep(line[1:17])
            sleep_count = sleep_count_end - sleep_count_start
            sleeping_time = [n for n in range(sleep_time_start, sleep_time_end + 1)]
            # sleeping_time adds the times that the guard was asleep
            if guard == "#10":
                guard_10[0] += sleep_count
                guard_10.extend(sleeping_time)
            if guard == "#99":
                guard_99[0] += sleep_count
                guard_99.extend(sleeping_time)

    guard_10_minutes_of_sleep = guard_10[0]
    guard_99_minutes_of_sleep = guard_99[0]
    guard_10_sleepiest_time = Counter(guard_10[1:]).most_common(1)  # the exact time that the guard slept the most
    guard_99_sleepiest_time = Counter(guard_99[1:]).most_common(1)

    if guard_10_minutes_of_sleep > guard_99_minutes_of_sleep:
        print(f"Guard #10 is most likely to be asleep in 00:{guard_10_sleepiest_time[0][0]}")
    elif guard_99_minutes_of_sleep > guard_10_minutes_of_sleep:
        print(f"Guard #99 is most likely to be asleep in 00:{guard_99_sleepiest_time[0][0]}")
    elif guard_10_minutes_of_sleep == guard_99_minutes_of_sleep:
        print(f"both guards slept the same amount of time."
              f"Guard #10 is most likely to be asleep in 00:{guard_10_sleepiest_time[0][0]}"
              f"guard #99 is most likely to be asleep in 00:{guard_99_sleepiest_time[0][0]}")


main()
