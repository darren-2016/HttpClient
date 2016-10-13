###################################################
# Basic HTTP Client Module
#
# A Simple HTTP Client module for testing out and 
# exploring HTTP functionality. 
#
# Darren J. Draper
# Created: October 2016
#

import httplib, urllib


#### Testing out a GET request
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




# Make the connection with the HTTP server
#serverurl = "dev-messaging-service.appspot.com"
serverurl = "www.gpsengine.net"
#serverurl = "www.google.com"
conn = httplib.HTTPSConnection(serverurl)


# Set the debug level (0 is the default, indicating no debug output is displayed)
conn.set_debuglevel(0)
TestGETRequest(conn)

# Close the connection to the server
conn.close()