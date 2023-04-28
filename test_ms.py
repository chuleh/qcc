import requests

def test_microservice_a():
    response = requests.get('http://localhost:5000/')
    assert response.status_code == 200

def test_microservice_b():
    response = requests.get('http://localhost:5001/')
    assert response.status_code == 200

def test_microservice_c():
    response = requests.get('http://localhost:5002/')
    assert response.status_code == 500

if __name__ == '__main__':
    test_microservice_a()
    test_microservice_b()
    test_microservice_c()