import requests

server_name = "http://vcm-21170.vm.duke.edu:5000/"

request_json = {"name": "Bidisha Nandi", "net_id": "bn74", "e-mail": "bidisha.nandi@duke.edu"}
r = requests.post(server_name + "student", json = request_json)
print(r.text)