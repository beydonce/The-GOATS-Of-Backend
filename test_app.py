import requests

BASE_URL = "http://127.0.0.1:5000"

def test_home():
    response = requests.get(BASE_URL + "/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the Restaurant Management System API!"

# ✅ Test Registering a New Customer
def test_register():
    response = requests.post(BASE_URL + "/register", json={
        "first_name": "Lola",
        "last_name": "User",
        "phone": "9876543210",
        "email": "testuser@example.com",
        "address": "Test Address",
        "username": "noga",
        "password": "lola123"
    })
    assert response.status_code in [201, 400]  # 201 = Success, 400 = Already Exists


# ✅ Test Customer Login (Valid Credentials)
def test_login_success():
    response = requests.post(BASE_URL + "/login", json={
        "username": "noga",
        "password": "lola123"
    })
    assert response.status_code == 200
    assert "customer_id" in response.json()  # Should return a customer ID

# ✅ Test Customer Login (Invalid Credentials)
def test_login_fail():
    response = requests.post(BASE_URL + "/login", json={
        "username": "wronguser",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.json()["error"] == "Invalid username or password"

# ✅ Test Get Menu Items
def test_get_menu():
    response = requests.get(BASE_URL + "/menu")
    assert response.status_code == 200
    assert "menu" in response.json()


