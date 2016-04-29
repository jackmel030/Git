import requests
"""make an HTTP GET request"""
response = requests.get("https://api.github.com/events")
"""GET request's URL"""
print(response.url)
"""GET request's message body with utf-8 encode"""
print(response.text.encode('utf-8'))

"""make an HTTP GET request with passing parameter"""
response = requests.get("http://httpbin.org/get", params={"key1": "value1", "key2": "value2"})
print(response)
"""GET request's URL"""
print(response.url)
"""GET requests's message body with utf-8 encode"""
print(response.text.encode('utf-8'))