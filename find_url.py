import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import time

def find_path():
    n_start = int(input("n_start >>> "))
    n_stop = int(input("n_stop  >>> "))
    
    t0 = time.time()
    url_main =  "http://ocsc.chulaonline.net/main/checkuser.asp?uid=OCSC"

    list_df = []

    for i in range(n_start, n_stop+1):
        url_i = f"{url_main}{str(i).zfill(6)}"
        response = requests.get(url_i)
        soup = BeautifulSoup(urlopen(response.url))
        text_return = (soup.findAll('b')[-1]).get_text()
        is_valid_username = (text_return.find("ไม่สามารถใช้"))<0
        print(f"{i-n_start+1}/{(1+n_stop-n_start)}, {str(i).zfill(6)}, {is_valid_username}")
        list_df.append((i, is_valid_username))
    
    
    df = pd.DataFrame(list_df, columns=["userid", "is_valid"])
    df.to_csv(f"username_{str(n_start).zfill(6)}_{str(n_stop).zfill(6)}.csv")

    t1 = time.time()
    print(f"Records {n_start} to {n_stop} in {t1-t0} seconds : Avg {(t1-t0)/(n_stop - n_start +1)} seconds per page")
    return 

if __name__ == "__main__":
    find_path()