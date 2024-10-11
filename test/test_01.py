import pytest
import requests

def test_root():
    req = requests.get('http://localhost:8080')
    print(req.text)
    assert req.text == '{"message":"hello World"}'

if __name__ == '__main__':
    # pytest.main()
    test_root()