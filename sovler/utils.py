import csv

from model import *


def load_wifi_scan_info_from_file(wifi_filename):
    res = []
    with open(wifi_filename) as wifi_file:
        wifi_file_reader = csv.reader(wifi_file)
        for row in wifi_file_reader:
            ssid = row[0]
            bssid = row[1]
            signal = int(row[2])
            is_encrypted = row[3]
            time_ = float(row[4])
            res.append(WifiScanInfo(ssid, bssid, signal, is_encrypted, time_))
    return res


def load_gps_scan_info_from_file(gps_filename):
    res = []
    with open(gps_filename) as gps_file:
        gps_file_reader = csv.reader(gps_file)
        for row in gps_file_reader:
            latitude = row[0]
            longitude = row[1]
            accuracy = row[2]
            time_ = float(row[3])
            res.append(GpsScanInfo(latitude, longitude, accuracy, time_))
    return res


def select_wifi_points(wifi_scan_info_list):
    res = []
    for scan_info in wifi_scan_info_list:
        point = WifiPoint(scan_info.ssid, scan_info.bssid, scan_info.is_encrypted)
        if point not in res:
            res.append(point)
        else:
            t = list(filter(lambda a: a == scan_info, res))[0]
            if scan_info.signal > t.best_signal:
                t.signal = scan_info.signal
                t.best_wifi_scan_time = scan_info.time
    return res


def set_best_location(point, gps_scan_info_list):
    for scan_info in gps_scan_info_list:
        d = abs(point.best_wifi_scan_time - point.best_gps_scan_time)
        nd = abs(point.best_wifi_scan_time - scan_info.time)
        if abs(nd < d):
            point.best_gps_scan_time = scan_info.time
            point.latitude = scan_info.latitude
            point.longitude = scan_info.longitude
