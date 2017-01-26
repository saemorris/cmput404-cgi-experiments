#!/usr/bin/env python

# ^ this is called the shebang -> tells the os how to run the script

import os
import json
import cgi
import Cookie

form = cgi.FieldStorage()

username = form.getvalue('user')
password = form.getvalue('password')

C = Cookie.SimpleCookie()
C.load(os.environ['HTTP_COOKIE'])

print "Content-Type: text/html"

if username == "bob" and password == "bob":
	print "Set-Cookie: loggedin=true"

print
print "<html><body>"
print "<h1>Hello World!</h1>"
print "Your magic tracking number is: " 
print form.getvalue('magic_tracking_number')
print "<p>Your browser is: "

if "Firefox" in os.environ['HTTP_USER_AGENT']:
	print "Firefox!"

if "Chrome" in os.environ['HTTP_USER_AGENT']:
	print "Chrome!"
print "</p>"

# prints out all of the environment variables
# print json.dumps(dict(os.environ), indent=2, sort_keys=True)

print "<form method='POST'><input name='user'><input name='password' type='password'>"
print "<input type='submit'></form>"


print "<p>Username: " + str(username)
print "<p>Password: " + str(password)

if username == "bob" and password == "bob":
	print "<p>Login Sucessful!"

if 'loggedin' in C:
	print "<p>Logged In: " + str(C['loggedin'].value)
else:
	print "<p>No Cookie"

print "</body></html>"
