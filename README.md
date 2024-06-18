# 240613 git-practice
## 學到的新的git指令
- `git log --oneline -n 3`: 將log顯示oneline 且前三筆
- `git branch -a`: 顯示remote的所有branch
- `git checkout`:
- `ls`: 看資料夾有甚麼資料
- `vi test.txt`: 修改
- `cat test.txt`:看資料上傳的狀態
- `git merge [branch]`
- `git HEAD^`: 會帶到log的前一條
- `git HEAD~2`: 會帶到log的前兩條等等

## pandas
主要是如何使用Series以及DataFrame
- pd.Series(), 括號裡面可以放list或dict
    `list_to_series = pd.Series(a)`
    將list或是dict轉乘Series
- pd.DataFrame()
    將dict轉乘DataFrame的表格
- pd.read_csv('data.csv')
    將data.csv的資料讀入

## requests
- requests.get(url), 可以得到網站的資料, 以下是可以用的method
```python
response = requests.get('https://api.github.com/')
print(response.url) # https://api.github.com/
print(response.status_code) # 200
print(response.headers) # returns a dictionary of respose headers
print(response.encoding) # utf-8
print(response.elapsed) # request time 0:00:00.679034
print(response.content) # returns all content in bytes
print(response.cookies) # return <RequestsCookieJar[]>
print(response.history) # history of request
print(response.is_permanent_redirect) # True -> response is the permanent redirected url
print(response.is_redirect) # True -> response was redirected
print(response.json()) # return json obj of the result
print(response.status_code) # 200 -> OK, 404 -> Not Found
print(response.ok) # True -> status_code < 200
print(response.text) # returns the content of the response, in unicode.
print(response.links) # returns the header links.
response.close()
```

# 240618 FastAPI
### venv環境建置
`python -m venv venv`
`pip install fastapi`

### FastAPI
``