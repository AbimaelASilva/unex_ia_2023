import requests




def has_internet():
    
    try:
        print('antes do equests.get("https://google.com", timeout=5)')
        response = requests.get("https://google.com", timeout=5)
        print('DEPOIS do equests.get("https://google.com", timeout=5)')
        return True
    except requests.ConnectionError:
        print("DEPOIS do requests.ConnectionError:")
        return False



