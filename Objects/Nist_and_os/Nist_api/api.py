import requests
import json
import time
class NistApi:
    def __init__(self):
        self.url_base = self.url()

    def url(self):
        with open('config.json','r') as conf:
            data = json.load(conf)
            return data['urlNist']   
    def search_vulnerabilities(self,cont):
        api_key = '45e9ee1d-47f7-4be9-893b-c54feb808265'  
        start_index = 200000
        results_per_page = 2000
        amount = cont / results_per_page
        data_return = {}
        arr = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Authorization': f'Bearer {api_key}'  
        }
        try :
            for i in range(int(amount)):
                response = requests.get(self.url_base+
                                        f"?startIndex={start_index}"+
                                        f"&resultsPerPage={results_per_page}",
                                        headers=headers)
                data = response.json()
                arr.extend(data['vulnerabilities'])
                data_return['vulns'] = arr
                data_return['amount'] = data['totalResults']
                start_index += results_per_page
                time.sleep(10)
                print(i)

            return data_return
        except requests.HTTPError as e:
            print(f"Error http: {e}")
        except requests.ConnectionError as e:
            print(f"Error al conectar con el servicio {e}")
        except requests.Timeout as e:
            print(f"Tiempo de espera sobrepasado {e}")
        except requests.RequestException as e:
            print(f"Error al capturar el dato o error en requests {e}")

        
    
        

  

        