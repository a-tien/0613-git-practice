import requests

response = requests.get('https://api.github.com/')
print(response.headers)
print(response.encoding)
print(response.elapsed)
print(response.content)
print(response.cookies)
print(response.history)
print(response.is_permanent_redirect)
print(response.is_redirect)
print(response.url)
print(response.json())
print(response.status_code)
print(response.ok)
print(response.request)
print(response.text)
print(response.links)
response.iter_content()
response.close()


# use session objects by setting a cookie to a url and chack again by making another request
s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
print(s)
r = s.get('https://httpbin.org/cookies') 
print(r.text)