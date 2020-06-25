class WifiPoint:
    def __init__(self, ssid, bssid, is_encrypted):
        self.ssid = ssid
        self.bssid = bssid
        self.is_encrypted = is_encrypted
        self.best_signal = -1000000
        self.best_wifi_scan_time = -1000000  # unix time
        self.best_gps_scan_time = -1000000
        self.latitude = -1
        self.longitude = -1

    def __eq__(self, other):
        return self.bssid == other.bssid

    def __repr__(self):
        return f"WifiPoint({self.ssid}, {self.bssid}, {self.is_encrypted})"
