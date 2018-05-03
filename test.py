import requests
import time
link = "http://127.0.0.1:8000/get";
i=100;

while i > 35:
    PARAMS = {'temperature':i,'humidity':i+20}
    r = requests.get(url = link, params = PARAMS)
    i=i-1;