---
tags:
  - charging-master
---
# CGM-System: 系統架構說明

![image 86.png](./CGM-System!%20系統架構說明-assets/image%2086.png)

這個系統架構圖描繪了一個基於 Azure 雲平台建置的電動巴士充電管理系統，主要由 ABS 自建服務、Azure 服務資源和外部服務三部分組成。

**一、核心功能**

此系統旨在實現電動巴士充電的排程、監控和管理，主要功能包括：

- **充電排程演算法**: 透過 Azure Event Hub 接收充電需求，並根據預設的演算法進行排程，最佳化充電效率。

- **即時監控**: Dashboard 應用程式提供充電狀態、電力數據等即時監控功能，方便管理者掌握系統運行狀況。

- **效能報告**: Dashboard 應用程式也提供效能報告功能，分析充電效率、能源消耗等數據，協助管理者優化系統運營。

- **身份驗證和授權**: Admin Portal 負責管理使用者帳戶和權限，確保系統安全。

- **外部服務整合**: 系統與飛宏 Zerova API 服務整合，實現充電樁數據的同步和控制。

**二、系統組成**

- **藍色區塊：ABS 自建服務**

   - **Backend**: 系統後端服務，負責處理業務邏輯、數據存儲和外部服務整合。採用 Spring Boot 框架，使用 Java 17 LTS 開發。

   - **Admin Portal**: 系統管理平台，提供使用者管理、權限控制等功能。採用 ReactJS 18.2 和 NodeJS 18 LTS 開發。

   - **Internal Service**: 內部服務，負責處理系統內部任務，例如數據同步、事件處理等。採用 Spring Boot 框架，使用 Java 17 LTS 開發。

   - **Webhook Service**: Webhook 服務，負責接收外部事件通知，並觸發相應的系統操作。採用 Spring Boot 框架，使用 Java 17 LTS 開發。

   - **Dashboard**: 數據儀表板，提供充電狀態監控、效能分析等功能。採用 Dash、Pandas 和 Python 3.8 開發。

- **綠色區塊：Azure 服務資源**

   - **Container Registry**: 儲存 Docker images，方便應用程式部署和更新。

   - **Azure MySQL**: 提供資料庫服務，儲存系統數據。

   - **Azure Blob Account**: 提供物件儲存服務，儲存系統檔案和資料。

   - **Azure Event Hub**: 提供事件串流服務，接收和處理充電事件。

- **灰色區塊：外部服務**

   - **AUO**: 友達光電，可能是系統的使用者或合作夥伴。

   - **Internet**: 網際網路，提供外部網路連接。

   - **Admin Users**: 系統管理員，透過 Admin Portal 管理系統。

   - **Zerova API Service**: 飛宏 Zerova 充電樁 API 服務，提供充電樁數據和控制功能。

   - **WAF**: Web 應用程式防火牆，保護系統免受網路攻擊。

**三、系統架構細節**

1. **使用者存取**: 使用者透過 Internet 訪問 Dashboard 或 Admin Portal，系統透過 WAF 進行安全防護。

2. **身份驗證**: Dashboard 和 Admin Portal 透過 Header Login Token 進行身份驗證，確保只有授權使用者才能存取系統。

3. **資料存儲**: 系統數據儲存在 Azure MySQL 資料庫中，應用程式透過資料庫連線進行數據讀寫。

4. **事件處理**: 充電事件透過 Azure Event Hub 接收，Internal Service 負責處理事件並觸發相應的系統操作。

5. **外部服務整合**: Backend 服務透過 API 呼叫與飛宏 Zerova API 服務進行數據交換和控制。

6. **Webhook**: Webhook Service 接收 Zerova API Service 的事件通知，並觸發相應的系統操作。

**四、開發環境資訊**

- **Database Compute**: 採用 Standard_B1ms 虛擬機器，配備 1 個 vCore、2 GB RAM 和 20 GB 儲存空間。

- **Backend Compute**: 採用 Basic B2 虛擬機器，配備 2 個 vCPU、3.5 GB RAM 和 10 GB 儲存空間。

- **Admin Portal Compute**: 採用 Basic B2 虛擬機器，配備 2 個 vCPU、3.5 GB RAM 和 10 GB 儲存空間。

- **Internal Service Compute**: 採用 Basic B2 虛擬機器，配備 2 個 vCPU、3.5 GB RAM 和 10 GB 儲存空間。

- **Webhook Service Compute**: 採用 Basic B2 虛擬機器，配備 2 個 vCPU、3.5 GB RAM 和 10 GB 儲存空間。

- **Dashboard Compute**: 採用 Basic B2 虛擬機器，配備 2 個 vCPU、3.5 GB RAM 和 10 GB 儲存空間。

**五、環境變數設定**

.env 檔案中包含了系統運行所需的環境變數，例如資料庫連線資訊、API 金鑰、外部服務 URL 等。

**六、總結**

這個系統架構圖清晰地展示了電動巴士充電管理系統的組成部分、功能模組和互動關係，以及系統的開發環境和設定資訊。透過此架構圖，開發者和管理者可以更好地理解系統的運作機制，方便進行系統開發、維護和優化。





## Webhook Service 

- 主要負責接收來自飛宏 Zerova API Service 的事件通知，並觸發相應的系統操作。更具體來說，Webhook Service 的作用如下：

1. **即時事件通知**: Zerova API Service 會將充電樁的狀態變化，例如充電開始、充電結束、故障發生等，即時推送給 Webhook Service。

2. **事件處理**: Webhook Service 接收事件通知後，會解析事件內容，並根據預先設定的規則進行處理。

3. **觸發系統操作**: Webhook Service 會根據事件類型，觸發相應的系統操作，例如更新充電狀態、發送告警訊息、記錄事件日誌等。

4. **系統整合**: Webhook Service 作為系統與 Zerova API Service 之間的橋樑，實現了系統與外部服務的整合，增強了系統的自動化和響應能力。

舉例來說，當 Zerova API Service 偵測到某個充電樁發生故障時，它會立即發送一個事件通知給 Webhook Service。Webhook Service 接收通知後，會解析故障資訊，並觸發以下操作：

- **更新充電樁狀態**: 將充電樁狀態更新為「故障」。

- **發送告警訊息**: 向系統管理員發送告警訊息，通知故障情況。

- **記錄事件日誌**: 將故障事件記錄到系統日誌中，方便日後查詢和分析。

透過 Webhook Service，系統可以即時掌握充電樁的狀態變化，並自動執行相應的操作，提高了系統的運營效率和可靠性。

此外，Webhook Service 還可以與其他系統組件進行互動，例如：

- **Backend Service**: Webhook Service 可以將事件資訊傳遞給 Backend Service，觸發更複雜的業務邏輯處理。

- **Admin Portal**: Webhook Service 可以將事件資訊推送給 Admin Portal，在管理界面上顯示告警訊息或更新充電樁狀態。

總之，Webhook Service 在這個電動巴士充電管理系統中扮演著重要的角色，它負責接收外部事件通知，觸發系統操作，實現系統整合，提高系統的自動化和響應能力。





## \[ ebus-internalservice \]

![CleanShot 2024-12-04 at 23.37.46@2x.png](./CGM-System!%20系統架構說明-assets/CleanShot%202024-12-04%20at%2023.37.46@2x.png)

本服務用 java 來進行子行程

### Azure EventHub

- 不同的程式間的溝通，除了像 API 這種類似電話要連線的方式外，尚有**訊息佇列**工具，它就像寄信到信箱，丟訊息跟收訊息不用同一時間，有空再去收信就好

- **訊息佇列工具的核心功能就是：**

   - **儲存訊息：** 就像信箱可以存放信件一樣，訊息佇列工具可以暫時儲存程式發送的訊息，直到其他程式來取走它們。

   - **傳遞訊息：** 訊息佇列工具會確保訊息被可靠地傳遞到目標程式，就像郵差會把信件送到正確的收件人手中。

- **Azure Event Hub、RabbitMQ、Kafka 都是訊息佇列工具，：**

   - **Azure Event Hub：** 專注於處理大量的訊息流，例如來自感測器、網站或行動應用程式的數據

   - **RabbitMQ：** 功能豐富，支持多種訊息傳遞模式，適合各種應用場景

   - **Kafka：** 專為處理高吞吐量的數據流而設計，例如網站活動追蹤、日誌收集等

- 適用情境：

   - 高吞吐量的事件流處理

   - 解耦生產者與消費者：系統間處理速度或時間不同步時，訊息佇列可以作為緩衝區

   - 彈性擴展性需求：訊息佇列工具能夠輕鬆擴展讀取或處理節點

   - 支援多消費者場景**：** 一個訊息需要被多個消費者處理，且這些消費者的功能或邏輯各不相同

   - **容錯與持久性需求：**當需要確保訊息在任何情況下都不丟失，並可以在消費者失敗時重新傳遞訊息

   

- Azure EnentHub SDK - Python

```python
from azure.eventhub import EventHubProducerClient, EventData

connection_string = "<Your Event Hub Namespace Connection String>"
event_hub_name = "<Your Event Hub Name>"

producer = EventHubProducerClient.from_connection_string(conn_str=connection_string, eventhub_name=event_hub_name)

try:
    event_data_batch = producer.create_batch()
    event_data_batch.add(EventData("Message 1"))
    event_data_batch.add(EventData("Message 2"))
    event_data_batch.add(EventData("Message 3"))

    producer.send_batch(event_data_batch)
    print("A batch of events has been sent.")
finally:
    producer.close()

```



```python
import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.storage.blob.aio import ContainerClient

connection_string = "<Your Event Hub Namespace Connection String>"
consumer_group = "$Default"
event_hub_name = "<Your Event Hub Name>"

async def on_event(partition_context, event):
    print(f"Received event from partition: {partition_context.partition_id}")
    print(f"Event data: {event.body_as_str()}")
    await partition_context.update_checkpoint(event)

async def main():
    consumer = EventHubConsumerClient.from_connection_string(
        conn_str=connection_string,
        consumer_group=consumer_group,
        eventhub_name=event_hub_name
    )
    async with consumer:
        await consumer.receive(on_event=on_event, starting_position="-1")  # "-1" means from the beginning.

if __name__ == "__main__":
    asyncio.run(main())

```



- Azure EnentHub SDK - Java

```java
import com.azure.spring.messaging.eventhubs.core.EventHubsTemplate;
import com.azure.spring.messaging.eventhubs.implementation.core.annotation.EventHubsListener;

try {
  Message<String> message = MessageBuilder.withPayload(result).build();
  log.info("[EventHub][{}] Sending result back to the Event Hub {}: {}", EVENT_HUB_NAME_RESULT, requestId, message);
  return eventHubsTemplate.sendAsync(EVENT_HUB_NAME_RESULT, message);
} catch (Exception e) {
  log.error("Error while sending message to event hub {}: {}", requestId, e.getMessage());
}
```



### Dockerfile 

- Purpose: Give a Java Env. that can run python script

- Container 像是資源使用上更彈性的 VM

   **Dockerfile（食譜）**：

   - 指定要用 `python:3.8`（基底），複製程式碼，安裝 `flask`，啟動網站。

   ```dockerfile
   FROM python:3.8
   COPY app.py /app/app.py
   RUN pip install flask
   CMD ["python", "/app/app.py"]
   ```

   **Docker Image（冷凍速食包）**：

   - 用這個 Dockerfile 製作出的 Image 包含：

      - Python 環境（3.8）

      - Flask（已安裝的依賴）

      - 你的 `[app.py](app.py)` 程式碼





## Java Run Python

- 使用 `ProcBuilder` 執行外部程式

```java
private ProcBuilder buildCommand(String requestInputFile) {
    return new ProcBuilder("python3.8")
        .withArgs(programPathToRun, requestInputFile)
        .withTimeoutMillis(programTimeout * 1000);
}
```

- `ProcBuilder` 是外部程式的執行工具，生成執行外部程式（如 Python 腳本）的命令

- 指定 `python3.8` 為執行的可執行檔，確保使用 Docker 中安裝的 Python 版本

- `programPathToRun` 是 Python 腳本的路徑，來自 Spring 配置檔案的 `@Value`。

- `requestInputFile` 是傳遞給 Python 腳本的參數，通常是輸入檔案的路徑。

- 設定了執行的超時時間，防止程式無限運行。

![CleanShot 2024-12-05 at 23.13.17@2x.png](./CGM-System!%20系統架構說明-assets/CleanShot%202024-12-05%20at%2023.13.17@2x.png)

## Java Spring

以下是幾個使用 Java Spring 建構 API backend 的基本語法範例，涵蓋基礎的 CRUD 操作：

---

### 1\. 建立 Controller

```
@RestController
@RequestMapping("/api/example")
public class ExampleController {

    @GetMapping("/hello")
    public String sayHello() {
        return "Hello, Spring Boot!";
    }

    @GetMapping("/{id}")
    public ResponseEntity<String> getExample(@PathVariable int id) {
        return ResponseEntity.ok("Example ID: " + id);
    }
}

```

---

### 2\. 定義 Service 層

```
@Service
public class ExampleService {

    public String getGreeting() {
        return "Hello from Service!";
    }

    public String getDataById(int id) {
        return "Data for ID: " + id;
    }
}

```

---

### 3\. 整合 Controller 與 Service

```
@RestController
@RequestMapping("/api/service")
public class ServiceController {

    private final ExampleService exampleService;

    public ServiceController(ExampleService exampleService) {
        this.exampleService = exampleService;
    }

    @GetMapping("/greet")
    public String greet() {
        return exampleService.getGreeting();
    }

    @GetMapping("/data/{id}")
    public String getData(@PathVariable int id) {
        return exampleService.getDataById(id);
    }
}

```

---

### 4\. 使用 Repository 連接資料庫

假設你使用 Spring Data JPA，定義一個 Repository：

```
@Repository
public interface ExampleRepository extends JpaRepository<ExampleEntity, Long> {
    List<ExampleEntity> findByName(String name);
}

```

---

### 5\. 定義資料實體 (Entity)

```
@Entity
public class ExampleEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

```

---

### 6\. 完整的 CRUD Controller 範例

```
@RestController
@RequestMapping("/api/crud")
public class CrudController {

    private final ExampleRepository exampleRepository;

    public CrudController(ExampleRepository exampleRepository) {
        this.exampleRepository = exampleRepository;
    }

    @PostMapping("/create")
    public ExampleEntity create(@RequestBody ExampleEntity entity) {
        return exampleRepository.save(entity);
    }

    @GetMapping("/{id}")
    public ResponseEntity<ExampleEntity> read(@PathVariable Long id) {
        return exampleRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PutMapping("/{id}")
    public ResponseEntity<ExampleEntity> update(@PathVariable Long id, @RequestBody ExampleEntity updatedEntity) {
        return exampleRepository.findById(id)
                .map(entity -> {
                    entity.setName(updatedEntity.getName());
                    return ResponseEntity.ok(exampleRepository.save(entity));
                })
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        if (exampleRepository.existsById(id)) {
            exampleRepository.deleteById(id);
            return ResponseEntity.ok().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}

```

---



### 商務邏輯

1. 基本請求流程：

   - ebus-svc 發送請求到 Event Hub (schedule-request-eventhub)

   - 演算法處理後將結果送回 Event Hub (schedule-result-eventhub)

   - ebus-svc 接收並處理結果

2. 結果驗證：

   - 驗證 LogChargingScheduleTrigger 是否存在

   - 檢查 schedules 和 faultDetails

   - 確認是否需要放棄結果（檢查站點其他未完成/取消的 trigger log 或 disabled timeslot）

3. ScheduleResult 處理：

   - 確保每個 ScheduleResult 的 periods 至少有兩個

   - 查找並確認 active session

   - 轉換為 ZerovaChargingProfile

4. 時間參數設定：

   - 如果第一個 period.start = 0：

      - startAt = 現在

      - estimatedStartAt = null

   - 如果第一個 period.start ≠ 0：

      - startAt = null

      - estimatedStartAt = 現在 + period\[0\].start

   - estimatedEndAt = 現在 + 最後一個 period.start

5. 錯誤處理：

   - 當發生錯誤時，系統會：

      - 標記 ERROR_CHARGING_REQUEST_RESULT_FAILED

      - 讀取原始請求中的 OperationSchedule

      - 建立最低功率設定

      - 重新呼叫 API



讓我來分析 periods 和時間參數的實際意義：

periods 應該是在描述充電排程的時間區段：

1. 為什麼需要至少兩個 periods：

   - 很可能第一個 period 是充電開始時間點

   - 第二個 period 則代表充電結束或功率變化時間點

   - 透過至少兩個時間點才能定義出一個完整的充電時段

時間參數的邏輯推測：

```
period[0].start = 0 的情況：
- 代表要立即開始充電
- 所以 startAt = 現在
- estimatedStartAt = null（因為不需要預估，就是現在開始）

period[0].start ≠ 0 的情況：
- 代表是預約未來某個時間點開始充電
- 所以 startAt = null（因為不是現在開始）
- estimatedStartAt = 現在 + period[0].start（預計未來啟動時間）
```

estimatedEndAt 的計算：

- 使用最後一個 period 的 start 時間

- 現在 + period\[最後\].start

- 這應該代表整個充電排程的預計結束時間

實務上的應用推測：

1. 即時充電模式：

   ```
   periods = [
     { start: 0, power: 30 },      // 立即開始，30kW
     { start: 7200, power: 0 }     // 2小時後結束（7200秒）
   ]
   ```

2. 預約充電模式：

   ```
   periods = [
     { start: 3600, power: 30 },   // 1小時後開始，30kW
     { start: 10800, power: 0 }    // 3小時後結束（從開始算起）
   ]
   ```

3. 變動功率充電模式：

   ```
   periods = [
     { start: 0, power: 30 },      // 立即開始，30kW
     { start: 3600, power: 20 },   // 1小時後降至20kW
     { start: 7200, power: 0 }     // 2小時後結束
   ]
   ```




