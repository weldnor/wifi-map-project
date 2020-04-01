import csv
import sys
import time

import termux_api

DEFAULT_FILENAME = "gps.csv"
DEFAULT_DELAY = 0


def save_log(filename):
    location = termux_api.location()
    latitude = location["latitude"]
    longitude = location["longitude"]
    accuracy = location["accuracy"]
    _time = time.time()

    csv_file = open(filename, "a")

    row = [latitude, longitude, accuracy, _time]

    writer = csv.writer(csv_file)
    writer.writerow(row)

    print(', '.join(str(v) for v in row))

    csv_file.close()


def main():
    filename = DEFAULT_FILENAME
    delay = DEFAULT_DELAY

    if len(sys.argv) >= 2:
        filename = sys.argv[1]

    if len(sys.argv) >= 3:
        delay = int(sys.argv[2])

    print(f"filename: {filename}")
    print(f"delay: {delay}")

    print("start scanning...\n")
    while True:
        save_log(filename)
        time.sleep(delay)


if __name__ == "__main__":
    main()
