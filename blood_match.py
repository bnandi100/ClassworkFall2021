import requests

server_name = "http://vcm-7631.vm.duke.edu:5002/"

r = requests.get(server_name + "get_patients/bn74")
print(r.text)

r = requests.get(server_name + "get_blood_type/M1")
print(r.text)

request_json = {"Name": "bn74", "Match": "Yes"}
r = requests.post(server_name + "match_check", json = request_json)
print(r.text)