import requests
import time

def check_http(url):
    start = time.time()
    
    try:
        response = requests.get(url, timeout=5)
        duration = time.time() - start

        return {
            "status": response.status_code,
            "response_time": duration,
            "healthy": response.status_code == 200
        }
    except:
        return {
            "healthy": False
        }