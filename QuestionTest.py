import requests
import json

session = requests.Session()


def dump(jsonStr):
    return json.dumps(json.loads(jsonStr), sort_keys=True, indent=4, separators=(',', ':'))


def loginTest():
    data = {
        "phone": "15810958128",
        "password": "root"
    }
    response = session.put("http://localhost:8080/api/user/session", data)
    print("loginTest:", dump(response.content.decode("utf8")))
    print("loginTest(cookie)", response.cookies)


def uploadQuestionTest():
    data = {
        "fileType": "csv"
    }
    file = {
        "file": ("file", open("template.csv", "rb"))
    }
    response = session.put("http://localhost:8080/api/question", data=data, files=file)
    print("uploadQuestionTest:", dump(response.content.decode("utf8")))
    data = {
        "fileType": "excel"
    }
    file = {
        "file": ("file", open("template.xlsx", "rb"))
    }
    response = session.put("http://localhost:8080/api/question", data=data, files=file)
    print("uploadQuestionTest:", dump(response.content.decode("utf8")))


def createQuizLimitedTest():
    data = {
        "questionNum": 10,
        "tagsId": [
            1, 2
        ]
    }
    response = session.get("http://localhost:8080/api/quiz/limited-quiz", params=data)
    print("createQuizLimitedTest:", dump(response.content.decode("utf8")))


def createQuizUnlimitedTest():
    data = {
        "questionNum": 10,
        "tagsId": [
            1, 2
        ]
    }
    response = session.get("http://localhost:8080/api/quiz/unlimited-quiz", params=data)
    print("createQuizUnlimitedTest:", dump(response.content.decode("utf8")))


loginTest()
uploadQuestionTest()
createQuizLimitedTest()
createQuizUnlimitedTest()
