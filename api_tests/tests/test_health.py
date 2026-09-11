import pytest
import requests

@pytest.mark.smoke
def test_health_status_code(base_url):
    res = requests.get(f"{base_url}/health")
    assert res.status_code == 200

@pytest.mark.smoke
def test_health_response_body(base_url):
    res = requests.get(f"{base_url}/health")
    res_json = res.json()
    assert "status" in res_json
    status = res_json["status"]
    assert isinstance(status, str)

@pytest.mark.smoke
def test_health_response_headers(base_url):
    res = requests.get(f"{base_url}/health")
    assert "application/json" in res.headers["content-type"]

@pytest.mark.smoke
def test_health_response_time(base_url):
    res = requests.get(f"{base_url}/health")
    assert res.elapsed.total_seconds() < 1

