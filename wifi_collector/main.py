import sys
import time

from wifi import Cell


def save_log(filename, interface):
    points = Cell.all(interface)
    _time = time.time()

    f = open(filename, "a")
    try:
        for point in points:
            ssid = point.ssid
            addr = point.address
            signal = point.signal
            is_encrypted = point.encrypted
            f.write(f"{ssid},{addr},{signal},{is_encrypted},{_time}")
            print(f"{ssid},{addr},{signal},{is_encrypted},{_time}")
        print("\n")
    except Exception:
        print("error")


def main():
    filename = "wifi.csv"
    interface = 'wlan0'
    delay: int = 1

    if len(sys.argv) == 2:
        filename = sys.argv[1]

    if len(sys.argv) == 3:
        delay = int(sys.argv[2])

    if len(sys.argv) == 4:
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
