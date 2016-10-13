# Basic HTTP Client Module
import httplib, urllib


# Make the connection with the HTTP server
#serverurl = "dev-messaging-service.appspot.com"
serverurl = "www.gpsengine.net"
#serverurl = "www.google.com"
connection = httplib.HTTPSConnection(serverurl)

# Set the debug level (0 is the default, indicating no debug output is displayed)
connection.set_debuglevel(0)

#### Testing out a GET request

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

# Close the connection to the server
connection.close()

