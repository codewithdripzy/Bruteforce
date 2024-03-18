import os;
import requests;
import json;

class Proxy:
    def __init__(self, url = "") -> None:
        self.list = None;
        self.url = url;
    
    def getProxies(self):
        path = os.path.abspath("./data/proxies.json")

        with open(path, 'r') as file:
            proxies = json.load(file)
            
        return proxies
    
    def getProxiesFromNetwork(self):
        try:
            response = requests.get(self.url);
            
            if response.status_code == 200:
                proxy_list = response.json();
                self.list = proxy_list;
                
            else:
                print("Failed to fetch proxy list");

            return self.list;
        except Exception as e:
            print("Failed to fetch proxy list");
        