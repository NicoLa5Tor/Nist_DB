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
    def search_vulnerabilities(self,start):
        api_key = '45e9ee1d-47f7-4be9-893b-c54feb808265'  
       # print(f"El start en la api es: {start}")
        start_index = start
        results_per_page = 2000
        amount = (self.search_amount() - start_index ) / results_per_page
        am = int(amount)
        data_return = {}
        arr = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Authorization': f'Bearer {api_key}'  
        }
        try :
            if am == 0:
                am += 1
            for i in range(am):
                response = requests.get(self.url_base+
                                        f"?startIndex={start_index}"+
                                        f"&resultsPerPage={results_per_page}",
                                        headers=headers)
                data = response.json()
                arr.extend(data['vulnerabilities'])
                data_return['vulns'] = arr
                start_index += results_per_page
                time.sleep(10)
                print(i)
                print(f"amount {am}")
                if i > 4 or i >= int(amount)-1:
                      print("retortna y termina el ciclo for")
                      return data_return,start_index
        except requests.HTTPError as e:
            print(f"Error http: {e}")
        except requests.ConnectionError as e:
            print(f"Error al conectar con el servicio {e}")
        except requests.Timeout as e:
            print(f"Tiempo de espera sobrepasado {e}")
        except requests.RequestException as e:
            print(f"Error al capturar el dato o error en requests {e}")
        except Exception as e:
            print(f"Error no específico: {e}")
    def search_amount(self):
        try:
            time.sleep(5)
            response = requests.get(self.url_base)   
            data = response.json()
            time.sleep(5)
            return data['totalResults']
        except requests.HTTPError as e:
            print(f"Error http: {e}")
        except requests.ConnectionError as e:
            print(f"Error al conectar con el servicio {e}")
        except requests.Timeout as e:
            print(f"Tiempo de espera sobrepasado {e}")
        except requests.RequestException as e:
            print(f"Error al capturar el dato o error en requests {e}")


        
    
        

  

        