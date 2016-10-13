# Basic HTTP Client Module
import httplib, urllib


# Make the connection with the HTTP server
serverurl = "www.google.com"
connection = httplib.HTTPSConnection(serverurl)

# Set the debug level (0 is the default, indicating no debug output is displayed)
connection.set_debuglevel(0)

#### Testing out a GET request

# Send a GET request to the server at the url '/' 
connection.request("GET", "/")

# Read the response after the request has been sent
response = connection.getresponse()
print response.status, response.reason

# Get data
data = response.read()
print data

# Close the connection to the server
connection.close()

