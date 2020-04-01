from subprocess import Popen, PIPE
import json


def exec_(command):
    proc = Popen(
        command,
        shell=True,
        stdout=PIPE, stderr=PIPE
    )
    proc.wait()
    res = proc.communicate()
    if proc.returncode:
        print(res[1])
    return res[0].decode("ascii")


def parse_json(text):
    return json.loads(text)


def exec_and_parse_json(command):
    return parse_json(exec_(command))


def location():
    """
    example output:
    [
        {
            "bssid": "55:55:55:55:55:55",
            "frequency_mhz": 2462,
            "rssi": -33,
            "ssid": "example name",
            "timestamp": 11872798197,
            "channel_bandwidth_mhz": "20"
        }
    ]
    """
    return exec_and_parse_json("termux-location")
