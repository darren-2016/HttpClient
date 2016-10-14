###################################################
# Basic HTTP Client Module
#
# A Simple HTTP Client module for testing out and 
# exploring HTTP functionality. 
#
# Darren J. Draper
# Created: October 2016
#

import httplib
import urllib
import requests
import base64
import string
import json


##################################################
# GetAuthentication
# Take the UserID and Password and return the 
# authentication string.
def GetAuthentication(userid, passwd):
    auth = 'Basic ' + string.strip(base64.encodestring(userid + ':' + passwd))
    return auth
    

##################################################
# TestGETRequest
# Testing out a GET request
def TestGETRequest(connection):
    # Send a GET request to the server at the url '/' 
    connection.request("GET", "/")

    # Read the response after the request has been sent
    response = connection.getresponse()
    print "Response status/reason: " + str(response.status), response.reason

    # Display the HTTP protocol version used by the server (10 = HTTP/1.0, 11=HTTP/1.1)
    print "HTTP protocol version: " + str(response.version)

    # Display a list of the (header,value) tuples
    #print response.getheaders()

    # Get data
    #data = response.read()
    #print data

##################################################
# CustomRequest
#
def CustomRequest(connection):
    connection.request("GET", "/")

     # Read the response after the request has been sent
    response = connection.getresponse()

    print "Response status/reason: " + str(response.status), response.reason

    # Display the HTTP protocol version used by the server (10 = HTTP/1.0, 11=HTTP/1.1)
    print "HTTP protocol version: " + str(response.version)

    # Display a list of the (header,value) tuples
    print response.getheaders()

    # Get data
    data = response.read()
    print "Data Length: " + str(len(data))
    print "Data: " + data

##################################################
# CustomRequest2
#
def CustomRequest2(connection):
    connection.request("GET", "/admin/testpage")

     # Read the response after the request has been sent
    response = connection.getresponse()
    print "Response status/reason: " + str(response.status), response.reason

    # Display the HTTP protocol version used by the server (10 = HTTP/1.0, 11=HTTP/1.1)
    print "HTTP protocol version: " + str(response.version)

    # Display a list of the (header,value) tuples
    print response.getheaders()

    # Get data
    data = response.read()
    print "Data Length: " + str(len(data))
    print "Data: " + data

##################################################
# TestSetupAccount
#
def TestSetupAccount(connection):
    connection.request("POST", "/test/setupaccount")

    # Read the response after the request has been sent
    response = connection.getresponse()
    print "Response status/reason: " + str(response.status), response.reason

####################
# SendSMS
# Send a message. 
def SendSMS(connection, userid, passwd, requesturl, message, phone):
    auth = 'Basic ' + string.strip(base64.encodestring(userid + ':' + passwd))
    print "Auth: " + auth

    params = urllib.urlencode({ "Body": message, "To": phone})

    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Authorization": auth}
    
    connection.request("POST", requesturl, params, headers)
    
    #connection.putrequest("POST", requesturl)
    #connection.putheader('Authorization', auth)
    #connection.endheaders()

    
    # Read the response after the request has been sent
    response = connection.getresponse()
    print "Response status/reason: " + str(response.status), response.reason

####################
# ReadSMS
#
def ReadSMS(connection, userid, passwd, requesturl):
    auth = 'Basic ' + string.strip(base64.encodestring(userid + ':' + passwd))
    print "Auth: " + auth

    #params = urllib.urlencode({"" : ""})

    connection.set_debuglevel(1)

    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Authorization": auth}

    connection.putrequest("GET", requesturl)
    connection.putheader("Content-type", "application/x-www-form-urlencoded")
    connection.putheader("Authorization", auth)
    connection.endheaders()

    #import time
    #time.sleep(5)
    # Read the response after the request has been sent
    response = connection.getresponse()
    response.read()
    print "Response status/reason: " + str(response.status), response.reason


##################################################
# ReadSMS action
#
def ReadSMS2(connection, userid, passwd, requesturl):
    # Read SMS        
    
    try:
        auth = 'Basic ' + string.strip(base64.encodestring(userid + ':' + passwd))
        response = requests.get(
            url=requesturl,
            headers={
                "Authorization": auth,
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            },
            data={
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        # Pretty-print the JSON output
        parsed = json.loads(response.content)
        print json.dumps(parsed, indent=4, sort_keys=True)

    except requests.exceptions.RequestException:
        print('HTTP Request failed')

##################################################
# NewIncomingPhone
#
def NewIncomingPhone(connection, userid, passwd, requesturl, phone, sid, workerpassword, friendlyname, printlog ):
    print "NEW INCOMING PHONE"
    try:
        auth = 'Basic ' + string.strip(base64.encodestring(userid + ':' + passwd))
        response = requests.post(
            url=requesturl,
            headers={
                "Authorization": auth,
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            },
            data={
                "PhoneNumber": phone,
                "Sid": sid,
                "WorkerPassword": workerpassword,
                "FriendlyName": friendlyname,
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        if printlog == 2:
            # Pretty-print the JSON output
            print('Response HTTP Response Body:(PrettyPrint)')
            parsed = json.loads(response.content)
            print json.dumps(parsed, indent=4, sort_keys=True)
        elif printlog == 1:
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))


    except requests.exceptions.RequestException:
        print('HTTP Request failed')



##################################################
# WorkerPending
#
def WorkerPending(userid, passwd, printlog):
    if printlog > 0:
        print "WORKER PENDING"
    
     # Worker Pending
    # GET https://dev-messaging-service.appspot.com/worker/pending.json

    try:
        auth = 'Basic ' + string.strip(base64.encodestring(userid + ':' + passwd))
        print "auth = " + auth
        response = requests.get(
            url="https://dev-messaging-service.appspot.com/worker/pending.json",
            headers={
                "Authorization": auth,
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        if printlog == 2:
            # Pretty-print the JSON output
            print('Response HTTP Response Body:(PrettyPrint)')
            parsed = json.loads(response.content)
            print json.dumps(parsed, indent=4, sort_keys=True)
        elif printlog == 1:
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


##################################################
# WorkerPending
#
def WorkerPending2(connection, userid, passwd, requesturl, phone, sid, workerpassword, friendlyname, printlog):
    if printlog > 0:
        print "WORKER PENDING"

    try:
        auth = 'Basic ' + string.strip(base64.encodestring(userid + ':' + passwd))
        print "auth = " + auth
        response = requests.get(
            url=requesturl,
            headers={
                "Authorization": auth,
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            },
            data={
                "PhoneNumber": phone,
                "Sid": sid,
                "WorkerPassword": workerpassword,
                "FriendlyName": friendlyname,
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        if printlog == 2:
            # Pretty-print the JSON output
            print('Response HTTP Response Body:(PrettyPrint)')
            parsed = json.loads(response.content)
            print json.dumps(parsed, indent=4, sort_keys=True)
        elif printlog == 1:
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))


    except requests.exceptions.RequestException:
        print('HTTP Request failed')


##################################################
# TestPUTRequest
def TestPUTRequest(connection):
    body = "***thebodycontentshere***"
    connection.request("PUT", "/file", body)
    response = connection.getresponse()
    print response.status, response.reason

