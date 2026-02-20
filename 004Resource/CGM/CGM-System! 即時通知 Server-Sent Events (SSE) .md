---
tags:
  - charging-master
---
# CGM-System: 即時通知 **Server-Sent Events (SSE)** 

![image 87.png](./CGM-System!%20即時通知%20Server-Sent%20Events%20(SSE)%20-assets/image%2087.png)



## \[ 架構 \]

這系統架構利用 **Server-Sent Events (SSE)** 技術來實現即時通知的功能, 以下說明：

### **為什麼要做這件事？**

- 後端資料發生變化時，讓前端能夠即時地接收到這些變化並顯示給使用者。特別是對於監控或管理系統（例如電動巴士充電管理系統），當站點或充電樁有異常（如錯誤發生）或狀態變化時，系統需要即時地通知使用者，以便他們能夠迅速採取行動。

- 這種即時通知的機制使得系統更具反應性和互動性，提高了用戶體驗。這裡使用 SSE 技術是一種高效的方法來實現這類功能，因為 SSE 可以讓伺服器持續向客戶端傳送更新，而不需要客戶端頻繁地請求伺服器查詢最新狀態。

### **架構說明**

1. **前端 (ReactJS)** 會透過 **fetch stream** 方式向 SSE 服務（位於 `/api/sse`）發送請求，這樣一來，當 SSE 路由有新事件時，就會推送到前端

2. 後端包含了一個 **Proxy Middleware**（可能是 NodeJS 中間層或 Java 的中介層），這層會處理 API 的請求和回應，並建立 SSE 路由供前端連接

3. 當後端（**Java Backend**）或 **Webhook Service** 接收到新的事件（例如來自遠端系統或設備的通知）時，會將這些事件包裝成新訊息，並透過 `/api/event` 路由發送到 SSE 路由，從而觸發前端的更新

### **SSE 的工作流程**

- 當後端有新事件發生（例如充電站狀態異常），它會將事件發送到 `/api/event` 路由。

- 該路由會將事件傳遞到 `/api/sse`，從而讓前端能夠透過 SSE 連接及時接收到這些事件。

- 前端收到事件後，會根據事件的類型（例如錯誤通知或資料變更）來更新介面，或顯示通知給使用者。

### **事件的資料格式**

事件的資料格式是統一的，以 JSON 格式發送到前端。每個通知包含以下必填和選填欄位：

- **faultType**: 通知的類型（例如系統錯誤、遠端錯誤或一般通知）。

- **action**: 通知後的行為類型，例如系統資料變更或一般通知。

- **id**: 訊息的唯一識別碼。

- **stationId**: 充電站的識別碼，這是必填欄位。

- 其他選填欄位如 **boxId**（充電樁識別）、**connectorId**（充電槍識別）等等。

### **可以用哪些技術實現這個架構？**

- **Java 和 ReactJS** 是這裡用到的主要技術，但不一定是唯一選項。SSE 是一個基於 HTTP 協定的技術，它可以在任何支援 HTTP 的後端框架中實現，例如：

   - **後端**：可以使用 NodeJS（Express.js）、Python（Flask 或 Django）、Ruby on Rails 等等，這些都能實現 SSE 路由。

   - **前端**：除了 ReactJS，也可以使用其他前端框架如 Angular、Vue.js，或甚至是原生 JavaScript 來實現 SSE 連接。

### **小結**

這個架構利用了 SSE 技術讓前端在後端資料變更時能即時更新。這樣的設計在充電管理系統中非常重要，可以讓管理者即時了解系統狀態，並快速反應。雖然目前使用的是 Java 和 ReactJS，但其他支援 SSE 的技術同樣可以實現這個架構。

---

## \[ What is SSE \]

- 一種基於 HTTP 的技術，用來實現從伺服器到客戶端的單向即時資料傳輸。雖然它不是最新的技術，但它在某些即時通訊應用場景中非常有效。以下是關於 SSE 的更詳細說明：

### **What is SSE ？**

- SSE 允許伺服器在特定的路由上，持續地向已經連接的客戶端發送更新。這與傳統的 HTTP 請求-回應模型不同，SSE 是一個 **伺服器推送（Server Push）** 的模式，即伺服器主動發送資料，而客戶端只是保持連接，等待資料的到來。

### **SSE 的特點**

1. **單向連接**：SSE 是一種單向的通訊方式，伺服器可以推送資料給客戶端，但客戶端無法主動向伺服器傳送資料。客戶端如果需要傳送資料給伺服器，必須透過其他 HTTP 請求。

2. **簡單實現**：SSE 的實現相對簡單，特別是在後端，只需建立一個特定的路由來推送資料；前端則可以使用 JavaScript 原生 API 來接收資料。

3. **自動重新連接**：SSE 具備自動重新連接的特性，如果連接中斷，客戶端會自動重新嘗試連接伺服器。

4. **持續連接但輕量**：相比於 WebSocket，SSE 是一種持續連接但更輕量的解決方案，因為它基於 HTTP 協定，而不需要特殊的協定協商。

### **SSE 的常見使用場景**

SSE 特別適合一些對資料流有即時需求，但不需要雙向通訊的場景，例如：

- **即時通知系統**：例如網站上的系統通知、數據變更通知、監控警報等。

- **數據流式更新**：例如股票市場的即時數據、電力系統的數據流、充電管理系統的充電狀態更新。

- **簡單的聊天應用**：在簡單的聊天應用中，伺服器可以持續推送新消息給客戶端，而客戶端的消息發送則可以使用標準的 HTTP POST。

### **SSE 與其他技術的比較**

1. **SSE vs. Polling**:

   - **Polling** 是客戶端定時向伺服器請求更新的一種方式。這種方法的缺點是容易造成伺服器負載過高，並且即時性不如 SSE。

2. **SSE vs. WebSocket**:

   - **WebSocket** 是一種雙向通信協定，可以同時支持客戶端和伺服器互相傳送資料。它適合需要互動性很強的應用（如多人遊戲或複雜的聊天應用）。相對於 WebSocket，SSE 更適合單向通訊、簡單、輕量的即時更新場景。

3. **SSE vs. Long Polling**:

   - **Long Polling** 是在沒有 SSE 或 WebSocket 支持的情況下，通過持續保持 HTTP 請求來實現即時更新的一種方式。Long Polling 可以模擬 SSE 的效果，但開銷較大，效能不如 SSE。

### **SSE 的局限性**

1. **不支援二進制資料**：SSE 只支援傳輸純文字資料，不像 WebSocket 支援二進制傳輸。如果需要傳送複雜的二進制數據，可能需要使用 WebSocket。

2. **受瀏覽器支持限制**：雖然大多數現代瀏覽器都支持 SSE，但有些舊版或非標準瀏覽器（例如早期版本的 IE）可能不支援。

3. **單向通訊**：SSE 只能由伺服器向客戶端發送資料，客戶端如果需要與伺服器通信，仍需通過其他 HTTP 方法（如 POST 請求）。

### **小結**

SSE 是一種方便、高效且輕量的伺服器推送解決方案，特別適合即時性高、雙向互動要求不高的場景。在構建這些應用時，它可以與其他技術（如 WebSocket、Polling）互補使用，以達到最佳的效果。

---



## \[ Python 中實現 SSE \]

可以使用多個框架來達成，如 **Flask** 和 **FastAPI** 等，這些框架都可以方便地設置 SSE 路由來實現伺服器推送更新的功能。以下是如何使用 Python 技術實現 SSE 的詳細步驟：

### **Flask + SSE 的實現方式**

Flask 是一個輕量級的 Python 網頁框架，適合快速搭建 SSE 應用。以下是一個簡單的 Flask 範例，展示如何設置 SSE 路由並推送資料給客戶端。

#### **安裝 Flask**

首先，確保安裝了 Flask：

```bash
pip install flask
```

#### **建立 Flask 應用**

```python
from flask import Flask, Response, stream_with_context
import time

app = Flask(__name__)

def generate_events():
    while True:
        time.sleep(5)  # 模擬每 5 秒發送一個事件
        yield f"data: The time is now {time.ctime()}\n\n"

@app.route('/stream')
def stream():
    return Response(stream_with_context(generate_events()), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
```

#### **說明**

1. **generate_events() 函數**:

   - 這個生成器函數會持續生成事件，並且每 5 秒鐘發送一次。

   - SSE 的格式要求每個事件以 `data: ` 開頭，並以 `\n\n` 作為事件的結束。

2. **/stream 路由**:

   - 這個路由使用 `Response` 和 `stream_with_context` 函數來將生成器函數包裝成一個 SSE 流。

   - `content_type='text/event-stream'` 表示這是 SSE 的 MIME 類型，客戶端會將其視為 SSE 連接。

#### **運行 Flask 應用**

運行 Flask 應用後，客戶端（如瀏覽器）可以訪問 `http://localhost:5000/stream` 來接收 SSE 事件。這樣的設計允許伺服器在生成新數據時，自動推送給已連接的客戶端。

### **FastAPI + SSE 的實現方式**

FastAPI 是另一個受歡迎的 Python 網頁框架，性能優異且支持非同步操作，非常適合 SSE 的實現。

#### **安裝 FastAPI**

首先，安裝 FastAPI 及其 ASGI 伺服器 `uvicorn`：

```bash
pip install fastapi uvicorn
```

#### **建立 FastAPI 應用**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def event_generator():
    while True:
        await asyncio.sleep(5)  # 模擬每 5 秒發送一個事件
        yield f"data: The time is now {time.ctime()}\n\n"

@app.get("/stream")
async def stream():
    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

#### **說明**

1. **event_generator() 函數**:

   - 使用 `async` 定義的非同步生成器函數，可以在每次事件生成之間使用 `await asyncio.sleep(5)` 暫停 5 秒鐘。

2. **/stream 路由**:

   - 使用 `StreamingResponse` 將事件生成器包裝成 SSE 流，並設置 `media_type="text/event-stream"` 來標記這是 SSE 資料流。

#### **運行 FastAPI 應用**

運行 FastAPI 應用後，訪問 `http://localhost:8000/stream` 可以看到持續更新的 SSE 事件。

### **客戶端實現 SSE**

無論使用 Flask 還是 FastAPI，客戶端都可以使用 JavaScript 原生的 `EventSource` API 來接收 SSE 事件。例如：

```javascript
const eventSource = new EventSource("http://localhost:8000/stream");

eventSource.onmessage = function(event) {
    console.log("New event received:", event.data);
};
```

### **總結**

在 Python 中使用 Flask 或 FastAPI 都可以輕鬆實現 SSE。SSE 是實現即時性要求高但不需要雙向通訊的應用場景的理想選擇，且 SSE 是基於 HTTP 協定的，所以相較於 WebSocket 實現上更簡單，適合流式數據更新、系統通知和即時監控。


