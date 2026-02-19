---
tags:
  - asp-dot-net-core
---
# 🚀 新 API 開發入門指南 ([ASP.NET](http://ASP.NET) Core)

歡迎加入專案開發！本指南將引導您如何依照現有的專案架構，一步步建立一支新的 API。我們將以開發一個管理「產品 (Product)」的 API 為例。

---

## 🧭 專案功能區塊回顧

在開始之前，請先熟悉我們專案的各個分層：

> 各項目功能說明如下，實際依照專案需求調整與擴充。

### 1\. `API` (`Todo.Api` 專案)

- **用途**: 接收前端請求、回傳處理結果。使用 Swagger 提供 API 文件與測試。

- **核心**: 定義 API 端點 (URL)、接收參數 (通常是 ViewModel)、回傳格式 (通常是 `Result` 包裝 ViewModel 或其他資料)。

- **範例**: `Todo.Api/Controllers/DemoController.cs`

### 2\. `LogicServer` (`Todo.BLogicService` 專案)

- **用途**: 處理核心業務邏輯。例如：資料驗證、條件判斷、組合不同來源的資料。

- **核心**: 包含 `Interface` (定義服務契約) 和 `Services` (實作具體邏輯)。它會呼叫 `Repository` 層來存取資料。

- **範例**: `Todo.BLogicService/Interface/IDemoService.cs`, `Todo.BLogicService/Services/DemoService.cs`

### 3\. `Repository` (`Todo.CRepository` 專案)

- **用途**: 負責與資料庫互動。封裝資料庫操作的細節。

- **核心**: 包含 `Repositories` (定義具體資料表的 CRUD 操作)、`UnitOfWorkPattern` (管理資料庫交易)。可能包含自動產生的 SQL (透過 Generic Repository) 或自定義 SQL (如 Dapper)。

- **範例**: `Todo.CRepository/Repositories/DemoRepo.cs`, `IUnitOfWork/IDefaultUOW.cs`, `UnitOfWork/DefaultUOW.cs`

### 4\. `Dentity` (`Todo.DEntity` 專案)

- **用途**: 定義資料庫資料表對應的 C# 物件模型 (Entity)。

- **核心**: 每個 `.cs` 檔案通常對應一個資料表，包含欄位屬性與對應的資料庫欄位名稱、主鍵等資訊 (使用 `[Table]`, `[Column]` 等 Attribute)。

- **範例**: `Todo.DEntity/Demo/DemoModel.cs`

### 5\. `ViewModel` (`Todo.EViewModel` 專案)

- **用途**: 定義 API 的輸入與輸出資料結構 (DTO - Data Transfer Object)。

- **核心**: 作為 `API` 層與 `LogicServer` 層之間，以及 `API` 層與前端之間傳遞資料的模型。它通常只包含必要顯示或接收的欄位，避免暴露過多的內部 `Entity` 細節。

- **範例**: `Todo.EViewModel/Demo/DemoVM.cs` (雖然 DemoController 直接用了 Entity，但通常建議用 ViewModel)

---

## 🏗️ 新 API 建置流程 (以 "Product" API 為例)

請依照以下步驟逐步建立您的新 API 功能：

### ✅ 第 1 步：定義資料庫模型 (Entity)

- **目標**: 建立與資料庫 `Product` 資料表對應的 C# 類別。

- **操作**:

   1. 在 `Todo.DEntity` 專案中，建立一個新的資料夾 (例如 `Product`)。

   2. 在該資料夾下建立 `ProductModel.cs` 檔案。

   3. 定義 `ProductModel` 類別，包含對應資料表欄位的屬性 (如 `Id`, `Name`, `Price`, `CreatedTime` 等)。

   4. 使用 `[Table(Name = "Products")]` (假設資料表名為 Products) 和 `[Column(Name = "...", IsKey = true)]` 等 Attribute 標註類別與屬性。

   5. 參考 `Todo.DEntity/Demo/DemoModel.cs` 的結構。

### ✅ 第 2 步：定義 API 資料傳輸模型 (ViewModel)

- **目標**: 建立 API 接收請求和回傳資料時使用的 C# 類別。

- **操作**:

   1. 在 `Todo.EViewModel` 專案中，建立一個新的資料夾 (例如 `Product`)。

   2. 建立 `ProductVM.cs` (用於查詢結果) 或 `CreateProductVM.cs` (用於新增)、`UpdateProductVM.cs` (用於更新) 等 ViewModel 檔案。

   3. 定義 ViewModel 所需的屬性，通常是 `ProductModel` 的子集或經過格式轉換的欄位。

   4. 參考 `Todo.EViewModel/Demo/DemoVM.cs`。

### ✅ 第 3 步：建立資料庫操作層 (Repository)

- **目標**: 建立負責 `Product` 資料表 CRUD 操作的 Repository。

- **操作**:

   1. 在 `Todo.CRepository/Repositories` 資料夾下，建立 `ProductRepo.cs`。

   2. 讓 `ProductRepo` 繼承 `GenericRepository<ProductModel, int>` (假設主鍵 `Id` 是 `int` 型別)。

      ```csharp
      using Todo.DEntity; // 引用 Entity
      using System.Data;
      
      namespace Todo.CRepository.Repositories
      {
          public class ProductRepo : GenericRepository<ProductModel, int>
          {
              public ProductRepo(IDbTransaction transaction) : base(transaction)
              {
              }
      
              // 如果需要複雜查詢，可以在這裡自訂方法
              // public IEnumerable<ProductModel> GetProductsByName(string name) { ... }
          }
      }
      ```

   3. 如果需要自訂 SQL 查詢 (例如 JOIN)，可以參考 `DemoRepo.cs` 中的 `Retrieve` 方法，使用 Dapper 或其他方式撰寫。

### ✅ 第 4 步：將 Repository 加入工作單元 (Unit of Work)

- **目標**: 讓 `LogicServer` 可以透過 UoW 存取到 `ProductRepo`。

- **操作**:

   1. **修改 `IDefaultUOW.cs`**:

      - 在 `Todo.CRepository/IUnitOfWork/IDefaultUOW.cs` 介面中，加入 `ProductRepo` 的屬性宣告。

      ```csharp
      using Todo.CRepository.Repositories;
      // ... 其他 using ...
      
      namespace Todo.CRepository
      {
          public interface IDefaultUOW : IUnitOfWork
          {
              // ... 其他 Repo ...
              ProductRepo ProductRepo { get; } // <--- 新增這行
          }
      }
      ```

   2. **修改 `DefaultUOW.cs`**:

      - 在 `Todo.CRepository/UnitOfWork/DefaultUOW.cs` 類別中，加入私有欄位和公開屬性的實作。

      ```csharp
      using Todo.CRepository.Repositories;
      // ... 其他 using ...
      
      namespace Todo.CRepository.UnitOfWorkPattern
      {
          public class DefaultUOW : GenericUnitOfWork, IDefaultUOW
          {
              // ... 其他 config 和 private repo 欄位 ...
              private ProductRepo _ProductRepo; // <--- 新增私有欄位
      
              // ... 其他 public repo 屬性 ...
      
              // <--- 新增公開屬性實作 --->
              public ProductRepo ProductRepo =>
                  _ProductRepo == null || _ProductRepo._dbConnection == null ? (_ProductRepo = new ProductRepo(_transaction)) : _ProductRepo;
          }
      }
      ```

### ✅ 第 5 步：定義業務邏輯層介面 (Service Interface)

- **目標**: 定義 `Product` 相關業務邏輯的方法簽章。

- **操作**:

   1. 在 `Todo.BLogicService/Interface` 資料夾下，建立 `IProductService.cs`。

   2. 定義介面，包含需要提供的業務邏輯方法，例如：

      ```csharp
      using Todo.ViewModel; // 引用 ViewModel
      using Todo.ViewModel.Models.Product; // 假設 ProductVM 在此
      
      namespace Todo.BLogicService.Interface
      {
          public interface IProductService
          {
              Result RetrieveProducts(ProductFilterVM filter); // 假設有篩選條件 ViewModel
              Result GetProductById(int id);
              Result CreateProduct(CreateProductVM model);
              Result UpdateProduct(UpdateProductVM model);
              Result DeleteProduct(int id);
          }
      }
      ```

   3. 注意：方法的參數和回傳值通常使用 `ViewModel` 和 `Result` (或 `Result<T>`)。

### ✅ 第 6 步：實作業務邏輯層 (Service Implementation)

- **目標**: 撰寫 `Product` 相關的具體業務邏輯。

- **操作**:

   1. 在 `Todo.BLogicService/Services` 資料夾下，建立 `ProductService.cs`。

   2. 讓 `ProductService` 實作 `IProductService` 介面。

   3. 透過**建構子注入 (Constructor Injection)** 注入 `IDefaultUOW` 和 `IMapper` (如果使用 AutoMapper)。

   4. 實作介面中的所有方法：

      - 呼叫 `_uow.ProductRepo` 的方法進行資料庫操作。

      - 使用 `_mapper` 進行 `ViewModel` 和 `Entity` 之間的轉換 (或手動轉換)。

      - 處理業務規則、驗證。

      - 使用 `try-catch` 包裹資料庫操作，並在成功時呼叫 `_uow.Commit()`，失敗時呼叫 `_uow.Rollback()`。

      - 將最終結果包裝在 `Result` 物件中回傳。

   5. 參考 `Todo.BLogicService/Services/DemoService.cs` 的寫法。

### ✅ 第 7 步：註冊服務 (Dependency Injection)

- **目標**: 讓 .NET Core 知道如何建立 `ProductService` 的實例。

- **操作**:

   1. 找到專案設定 DI 的地方 (通常是 `Todo.Api` 專案的 `Program.cs` 或 `Startup.cs`，或像本專案可能在 `AutofacModule` 資料夾下的某個設定檔)。

   2. 加入 `IProductService` 和 `ProductService` 的註冊。例如 (語法可能因 DI 容器而異)：

      ```csharp
      // 假設使用 .NET Core 內建 DI
      builder.Services.AddScoped<IProductService, ProductService>();
      
      // 或 假設使用 Autofac
      // builder.RegisterType<ProductService>().As<IProductService>().InstancePerLifetimeScope();
      ```

   3. 確保 `IDefaultUOW` 和 `DefaultUOW` 以及 AutoMapper 也已被正確註冊。

### ✅ 第 8 步：建立 API 控制器 (Controller)

- **目標**: 建立處理 `/api/product` 請求的端點。

- **操作**:

   1. 在 `Todo.Api/Controllers` 資料夾下，建立 `ProductController.cs`。

   2. 繼承 `BaseController` 或 `ControllerBase`。

   3. 加上 `[ApiController]` 和 `[Route("api/[controller]")]` Attribute。

   4. 透過**建構子注入**注入 `IProductService`。

   5. 建立對應的 Action 方法 (如 `Get`, `Post`, `Put`, `Delete`)。

   6. 使用 `[HttpGet]`, `[HttpPost]`, `[HttpPut]`, `[HttpDelete]` 和 `[Route(...)]` (如果需要自訂路由) 來標註方法。

   7. 方法的參數使用 `[FromQuery]` (用於 GET 的查詢字串) 或 `[FromBody]` (用於 POST/PUT 的請求本文) 來綁定 `ViewModel`。

   8. 在方法內部呼叫注入的 `_productService` 的對應方法。

   9. 回傳 `_productService` 回傳的 `Result` 物件。

   10. **重要**: 加上 Swagger 文件註解 (`<summary>`, `<remarks>`, `<param>`, `<returns>`, `<response>`)，說明 API 用途、參數、回傳值和可能的錯誤。

   11. 參考 `Todo.Api/Controllers/DemoController.cs` 的結構和寫法。

### ✅ 第 9 步：設定物件映射 (AutoMapper - 如果使用)

- **目標**: 定義 `ProductModel` (Entity) 和 `ProductVM` (ViewModel) 之間的轉換規則。

- **操作**:

   1. 找到 AutoMapper 的 Profile 設定檔 (可能在 `Todo.BLogicService/AutoMapperProfiles` 下)。

   2. 在 Profile 的建構子中，加入 `CreateMap<ProductModel, ProductVM>();` 和 `CreateMap<CreateProductVM, ProductModel>();` 等映射規則。

### ✅ 第 10 步：測試 API

- **目標**: 驗證新建立的 API 是否正常運作。

- **操作**:

   1. 執行 `Todo.Api` 專案 (通常按 F5)。

   2. 開啟瀏覽器，導覽至 Swagger UI 的路徑 (通常是 `/swagger`)。

   3. 找到 "Product" API 區塊。

   4. 使用 Swagger 介面測試每個端點 (GET, POST, PUT, DELETE)，檢查參數是否正確傳遞、回傳結果是否符合預期、資料庫資料是否正確變更。

---

恭喜！依照這些步驟，您應該就能成功建立並測試一支新的 API。如果在過程中遇到問題，請隨時參考 Demo 範例或詢問團隊成員。祝您開發順利！