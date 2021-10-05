# import json
#
# import requests
#
#
# def getinfo():
#     headers = {
#         'content-type': 'text/plain;',
#     }
#     data = {"jsonrpc": "2.0", "id": "curltest", "method": "getinfo", "params": []}
#     data = json.dumps(data)
#     rpcuser = 'user'
#     rpcpassword = 'pass'
#     response = requests.post('http://127.0.0.1:33825/', headers=headers, data=data,
#                              auth=(rpcuser, rpcpassword))
#     response = response.json()
#     return response
#
#
# def getblockhash(height):
#     headers = {
#         'content-type': 'text/plain;',
#     }
#     data = {"jsonrpc": "2.0", "id": "curltest", "method": "getblockhash", "params": [height]}
#     data = json.dumps(data)
#     rpcuser = 'user'
#     rpcpassword = 'pass'
#     response = requests.post('http://127.0.0.1:33825/', headers=headers, data=data,
#                              auth=(rpcuser, rpcpassword))
#     response = response.json()
#     return response
#
#
# print(getblockhash(1))
# print(getinfo())


import pycurl
import json
from io import StringIO

curl = pycurl.Curl()
curl.setopt(curl.URL, 'http://127.0.0.1:33825/')
curl.setopt(curl.USERPWD, "user:pass")
curl.setopt(curl.HTTPHEADER, ["Content-Type: text/plain"])
curl.setopt(curl.VERBOSE, True)  # to print entire request flow
curl.setopt(curl.POST, 1)


# curl.setopt(pycurl.TIMEOUT_MS, 3000)  # If you want to set a total timeout, say, 3 seconds

## depending on whether you want to print details on stdout, uncomment either
# curl.setopt(pycurl.VERBOSE, 1) # to print entire request flow
## or
# curl.setopt(pycurl.WRITEFUNCTION, lambda x: None)  # to keep stdout clean

# preparing body the way pycurl.READDATA wants it
# NOTE: you may reuse curl object setup at this point
#  if sending POST repeatedly to the url. It will reuse
#  the connection.
body_as_dict = {"jsonrpc": "2.0", "id": "curl", "method": "getinfo", "params": []}
body_as_json_string = json.dumps(body_as_dict)  # dict to json
body_as_file_object = StringIO(body_as_json_string)


# prepare and send. See also: pycurl.READFUNCTION to pass function instead
curl.setopt(pycurl.READDATA, body_as_file_object)
curl.setopt(pycurl.POSTFIELDSIZE, len(body_as_json_string))
curl.perform()

# you may want to check HTTP response code, e.g.
status_code = curl.getinfo(pycurl.RESPONSE_CODE)
if status_code != 200:
    print("Aww Snap :( Server returned HTTP status code {}".format(status_code))

curl.close()  # release connection when finished
