import sys

from utils import *

DEFAULT_OUTPUT_FILENAME = "map.csv"

HELP_MESSAGE = """
usage: main wifi.csv gps.csv [output_filename]
"""

wifi = []
gps = []


def main():
    output_filename = DEFAULT_OUTPUT_FILENAME
    wifi_filename = ""
    gps_filename = ""

    if len(sys.argv) < 3:
        print(HELP_MESSAGE)
        sys.exit()

    if len(sys.argv) >= 3:
        wifi_filename = sys.argv[1]
        gps_filename = sys.argv[2]

    if len(sys.argv) >= 4:
        output_filename = sys.argv[3]

    wifi_scan_info_list = load_wifi_scan_info_from_file(wifi_filename)
    gps_scan_info_list = load_gps_scan_info_from_file(gps_filename)
    points = select_wifi_points(wifi_scan_info_list)

    for point in points:
        set_best_location(point, gps_scan_info_list)

    save_wifi_points_to_file(output_filename, points)


def save_wifi_points_to_file(filename, points):
    with open(filename, "w") as f:
        writer = csv.writer(f)

        for point in points:
            ssid = point.ssid
            bssid = point.bssid
            is_encrypted = point.is_encrypted
            latitude = point.latitude
            longitude = point.longitude
            writer.writerow([ssid, bssid, is_encrypted, latitude, longitude])


if __name__ == '__main__':
    main()
