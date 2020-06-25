class WifiScanInfo:
    def __init__(self, ssid: str, bssid: str, signal: int, is_encrypted: bool, time: int):
        self.ssid = ssid
        self.bssid = bssid
        self.signal = signal
        self.is_encrypted = is_encrypted
        self.time = time
