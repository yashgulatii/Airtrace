import pywifi
from pywifi import const
import time

def scan_with_pywifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(2)  # Allow time for the scan to complete
    results = iface.scan_results()

    networks = []
    for network in results:
        ssid = network.ssid
        signal = network.signal  # dBm (negative values usually)
        quality = min(max(2 * (signal + 100), 0), 100)  # Normalize to 0-100 scale
        networks.append({'SSID': ssid, 'Signal': int(quality)})
    return networks

def scan_networks():
    try:
        from pywifi import PyWiFi
        return scan_with_pywifi()
    except ImportError:
        print("pywifi not installed. Falling back to subprocess-based scan.")
        return ()
