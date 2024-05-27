import sys
import traceback

import requests


# TODO (10 concurrent requests from the same client causes cherrypy to drop the requests and give connection timeout.)
CURRENT_VS_EXPECTED_VALUE_MAPPING = (
    ("aa", [1]),
    ("abbcc", [2, 6]),
    ("dz_a_aazzaaa", [28, 53, 1]),
    ("a_", [0]),
    ("abcdabcdab", [2, 7, 7]),
    ("abcdabcdab_", [2, 7, 7, 0]),
    ("zdaaaaaaaabaaaaaaaabaaaaaaaabbaa", [34]),
    ("zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_", [26]),
    ("za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa", [40, 1]),
    ("_", [0]),
    ("_ad", [0]),
    ("a_", [0]),
    ("_zzzb", [0]),
    ("__", [0]),
    ("   ", []),
    ("@@@", []),
    ("1234", []),
    ("aaa", []),
    ("ccc", []),
    ("", []),
)

SERVER_ADDRESS = sys.argv[1] if len(sys.argv) > 1 else "localhost"
SERVER_PORT = sys.argv[2] if len(sys.argv) > 2 else 8080
# BASE_URL = f"http://{SERVER_ADDRESS}:{SERVER_PORT}/api/v1/convert-measurements"
BASE_URL = f"http://192.168.137.62:8080/convert_measurements"


def status_for_valid_measurement(measurement, expected_value):
    try:
        response = requests.get(BASE_URL, params={"input": measurement})
        response_dict = response.json()
        result = response_dict['result']
        print(f"PASS for {measurement}" if result == expected_value else f"FAIL for {measurement}")
    except Exception:
        print(traceback.format_exc())


for entry in CURRENT_VS_EXPECTED_VALUE_MAPPING:
    status_for_valid_measurement(entry[0], entry[1])

