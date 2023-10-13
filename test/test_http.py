import requests

def test_http_requests():
    url = 'http://127.0.0.1:8080/hi'
    
    data = 'hahahaha'
    ret = requests.get(url=url, data=data)
    print(ret.text)
    

if __name__=='__main__':
    
    test_http_requests()