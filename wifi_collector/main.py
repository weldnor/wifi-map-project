import csv
import sys
import time

from wifi import Cell

DEFAULT_FILENAME = "wifi.csv"
DEFAULT_INTERFACE = "wlan0"
DEFAULT_DELAY = 1


def save_log(filename: str, interface: str):
    points = Cell.all(interface)
    _time = time.time()

    csv_file = open(filename, "a")
    for point in points:
        ssid = point.ssid
        bssid = point.address
        signal = point.signal
        is_encrypted = point.encrypted

        if ssid == '':
            continue

        row = [ssid, bssid, signal, is_encrypted, _time]

        writer = csv.writer(csv_file)
        writer.writerow(row)

        print(', '.join(str(v) for v in row))
    print("\n")

    csv_file.close()


def main():
    filename = DEFAULT_FILENAME
    interface = DEFAULT_INTERFACE
    delay = DEFAULT_DELAY

    if len(sys.argv) >= 2:
        filename = sys.argv[1]

    if len(sys.argv) >= 3:
        delay = int(sys.argv[2])

    if len(sys.argv) >= 4:
        interface = sys.argv[3]

    print(f"filename: {filename}")
    print(f"interface: {interface}")
    print(f"delay: {delay}")

    print("start scanning...\n")
    while True:
        save_log(filename, interface)
        time.sleep(delay)


if __name__ == '__main__':
    main()
