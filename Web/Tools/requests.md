# Web

This document is meant to be used as a quick reference or 'cheat sheet'. Please refer to the documentation linked below for a more detailed look at Python Requests.
## [Requests Library](https://2.python-requests.org/en/master/user/quickstart/)
The Python Requests library allows you to send HTTP requests as well as edit and view headers and cookies. The ability to do this in Python makes brute forcing and programmatically attacking web challenges much easier.


### Getting Started
Make sure to import the Requests module:
```python
import requests
```


### Making Requests
```python
# Get Request
r = requests.get('https://api.github.com/events')

# Post Request
r = requests.post('https://httpbin.org/post', data = {'key':'value'})

# Other requests
r = requests.put('https://httpbin.org/put', data = {'key':'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')
```

After making a request, we now have a Respone object *r*. We'll get into accessing the information from a Response later.


### Adding Parameters, Headers, and Cookies to a Request
#### Parameters
How parameters are passed in an URL:
```httpbin.org/get?key1=val1&key2=val2```

How to pass parameters in the URL using Requests:
```python
p = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=p)

# Check the url
print(r.url) # https://httpbin.org/get?key1=value1&key2=value2
```


#### Headers
```python
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'} 	# Custom headers

r = requests.get(url, headers=headers)		# Pass headers into Request
```


#### Cookies
```python
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
```


### Getting Info from a Response
```python
r.text			# Get the response as text
r.encoding = 'utf-8'	# Change the encoding of the text response


r.content		# Get the response as bytes, for non-text requests


r.json()		# Decode the response as JSON


r.status_code		# Get the response status code


r.headers		# Get the response headers
r.headers['Content-Type']
r.headers.get('content-type')


r.cookies		# Get the response cookies
r.cookies['example_cookie']
```


