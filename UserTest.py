import requests

session = requests.Session()


def signupTest():
    data = {
        "name": "李松",
        "phone": "15810958128",
        "password": "root",
        "passwordVerify": "root"
    }
    response = requests.put(url="http://localhost:8080/api/user", data=data)
    print("signupTest:", response.content.decode("utf8"))


def loginTest():
    data = {
        "phone": "15810958128",
        "password": "root"
    }
    response = session.put("http://localhost:8080/api/user/session", data)
    print("loginTest:", response.content.decode("utf8"))
    print("loginTest(cookie)", response.cookies)


def getUserInfoTest():
    response = session.get("http://localhost:8080/api/user/user-info")
    print("getUserInfoTest:", response.content.decode("utf8"))


def updateInformationTest():
    data = {
        "experience": "rookie",
        "graduatedSchool": "北京大学"
    }
    response = session.post("http://localhost:8080/api/user/information", json=data)
    print("updateInformationTest:", response.content.decode("utf8"))


def updateFieldTest():
    data = {
        "fields": ["finance", "broker", "internet"]
    }
    response = session.post("http://localhost:8080/api/user/field", data=data)
    print("updateFieldTest:", response.content.decode("utf8"))
    data = {
        "fields": ["internet"]
    }
    response = session.post("http://localhost:8080/api/user/field", data=data)
    print("updateFieldTest:", response.content.decode("utf8"))


signupTest()
loginTest()
getUserInfoTest()
updateInformationTest()
updateFieldTest()
