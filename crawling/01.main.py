import requests as req

# res = req.get("https://api.ipify.org/", headers={"fast": "campus"})
res = req.get("https://api.ipify.org/")

# print(res.request.headers)
# print(res.elapsed)
print(res.text)
print(res.raw)

# print(res.status_code)
# print(res.text)
