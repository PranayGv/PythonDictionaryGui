import requests
from bs4 import BeautifulSoup
import scripts.config as config

def get(query, class_names):
    URL = config.website + query
    header = {
        "User-Agent": config.User_Agent
    }
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content, "html.parser")
    result = None
    try:
        for className in class_names:
            htmlElement = soup.find(class_=className)
            result = htmlElement.get_text() if htmlElement != None else None
            if result != None:
                break
    except Exception as e:
        print(e)
        pass

    return result
