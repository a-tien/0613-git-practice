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
## 使用pytest跑unitest
一開始因為用powershell跑一直出現錯誤，後來改用cmd就可以了
1. `cd venv`
2. 啟用venv `Scripts\activate`
3. 下載pytest `pip install pytest`
3. 下載coverage `pip install pytest-cov`
4. 回到根目錄 `cd ..`
5. 創一個tests資料夾，裡面放想測試的程式(可以看下面範例)
6. 用pytest去對tests檔案做檢查 `pytest --cov=/tests /tests`
7. 跑出來的結果

![image](https://hackmd.io/_uploads/HynmKZ_L0.png)

6. 可以透過coverage html看miss的東西 `coverage html` 點網址進入

![image](https://hackmd.io/_uploads/SymKFZdLR.png)

綠色是測試過的地方，紅色的部分代表還沒寫單元測試的地方

## 範例

將其中一個測資拿出來對應，透過test_main.py的`test_read_name()`函式來對main.py的`@app.get("/{name}")`進行測試

**tests/main.py** (原本的FastAPI程式)
```python
app = FastAPI(title="2024/06/18 FastAPI Practice")
@app.get("/{name}", description="Hello name")
async def root(name: str):
    return {"message": "Hello World {name}"}
```

**tests/test_main.py** (測試FastAPI的程式)
```python
from fastapi.testclient import TestClient
from tests.main import app

client = TestClient(app) # 連接main.py的API

def test_read_name():
    response = client.get("/{name}")
    assert response.status_code == 200
    assert response.json() == {"message" : "Hello World {name}"}
```
