# Basic HTTP Client Module
import httplib

# Make the connection
connection = httplib.HTTPSConnection("www.google.com")
connection.request("GET", "/")

# Check the response
response = connection.getresponse()
print response.status, response.reason

# Get data
data = response.read()
print data

# Close the connection
connection.close()

