# Spring Introduction

## **\[ 什麼是 Spring Boot\]**

- Spring:

   - A Java framework for building applications.

   - Provides dependency injection, transaction management, and MVC architecture.

   - Requires manual configuration for setup.

- Spring Boot:

   - A pre-configured extension of Spring 

   - makes development faster and easier

   - Provides embedded servers (Tomcat, Jetty), auto-configuration, and less boilerplate code.

   - Ideal

- 類似:

   -  [ASP.NET](http://ASP.NET) Core 對於 .NET 生態系統的作用

   - Flask, Django, Fast API  對於 Python 的作用。



## **\[ 核心概念類比 \]**

1. **快速啟動（Convention Over Configuration）**

   - **類似於**：[ASP.NET](http://ASP.NET) Core 的預設模板或 Flask 的快速開發模式。

   - **說明**：Spring Boot 提供了預設的配置和最佳實踐，讓你可以快速啟動一個新項目，而無需過多的手動設置。這就像在 [ASP.NET](http://ASP.NET) Core 使用模板創建新項目一樣，減少了初始配置的工作量。

2. **依賴注入（Dependency Injection）**

   - **類似於**：[ASP.NET](http://ASP.NET) Core 內建的依賴注入容器，或 Python 中使用的依賴注入庫（如 `injector`）。

   - **說明**：Spring Boot 使用依賴注入來管理對象的創建和依賴關係，促進了代碼的鬆耦合和可測試性。這與 [ASP.NET](http://ASP.NET) Core 的 DI 容器或 Python 的依賴注入庫有相似之處。

3. **內嵌伺服器（Embedded Server）**

   - **類似於**：[ASP.NET](http://ASP.NET) Core 使用的 Kestrel 伺服器，或 Flask/Django 的內建開發伺服器。

   - **說明**：Spring Boot 提供了內嵌的 Tomcat、Jetty 或 Undertow 伺服器，使得應用程序可以直接運行而無需單獨部署伺服器。這與你在 [ASP.NET](http://ASP.NET) Core 或 Flask 中的開發體驗相似。

4. **RESTful API 支援**

   - **類似於**：[ASP.NET](http://ASP.NET) Core 的 Web API 或 Flask 的路由系統。

   - **說明**：使用 Spring Boot，你可以輕鬆定義 REST 端點，通過註解（如 `@RestController`、`@RequestMapping`）來設置路由，這與在 [ASP.NET](http://ASP.NET) Core 中使用控制器和路由屬性或在 Flask 中定義路由非常相似。

5. **數據持久化（JPA - Java Persistence API）**

   - **類似於**：[ASP.NET](http://ASP.NET) Core 的 Entity Framework 或 Python 的 SQLAlchemy。

   - **說明**：Spring Boot 通常與 Spring Data JPA 結合使用，提供了類似於 Entity Framework 的 ORM（對象關聯映射）功能，簡化了與資料庫的交互。

6. **配置文件（application.properties / application.yml）**

   - **類似於**：[ASP.NET](http://ASP.NET) Core 的 `appsettings.json` 或 Python 的環境變數配置。

   - **說明**：Spring Boot 使用 `application.properties` 或 `application.yml` 來管理應用配置，如資料庫連接、伺服器設置等，這類似於你在 [ASP.NET](http://ASP.NET) Core 中配置 `appsettings.json` 或在 Python 中使用環境變數進行配置。

### **為什麼使用 Spring Boot？**

- **生產力高**：減少了樣板代碼和配置，讓你更快地開發應用。

- **微服務支持**：像 [ASP.NET](http://ASP.NET) Core 一樣，Spring Boot 非常適合構建微服務架構，並且能夠與雲平台和容器化工具（如 Docker）無縫集成。

- **豐富的生態系統**：擁有廣泛的社區支持和大量的插件，滿足各種開發需求。

- **強大的測試框架**：提供了類似於 xUnit（.NET）或 PyTest（Python）的測試支持，使單元測試和集成測試更加便捷。

### **快速比較表**

| 概念 | Spring Boot | [ASP.NET](http://ASP.NET) Core | Python (Flask/Django) | 
|---|---|---|---|
| **框架類型** | Java (類似 Java EE) | .NET ([ASP.NET](http://ASP.NET) Core) | Python (Flask/Django) | 
| **依賴注入** | 內建 | 內建 | 外部庫 | 
| **REST API 支援** | `@RestController` 等註解 | 控制器和路由屬性 | Flask 路由或 Django 視圖 | 
| **資料庫存取** | Spring Data JPA (類似 EF) | Entity Framework (EF) | SQLAlchemy / Django ORM | 
| **內嵌伺服器** | Tomcat (預設) | Kestrel | Flask/Django 內建伺服器 | 
| **配置文件** | `application.properties/yml` | `appsettings.json` | 環境變數或配置文件 | 



## \[Java 版本\]

### **1\. Java 版本演變與權限爭議**

- **Java 誕生與早期版本**：Java 由 Sun Microsystems 在 1996 年首次發布，強調跨平台應用的能力。隨後版本（如 Java 2、Java 5）不斷增強語言特性和庫功能，提升了 Java 在企業應用中的地位。

- **Oracle 收購與權限爭議**：2010 年，Oracle 收購 Sun Microsystems，成為 Java 的主要擁有者。收購後，Oracle 開始強化對 Java 的商業控制，特別是在 Java SE（標準版）上實施了新的商業授權策略，使得某些版本的使用需要付費授權，引發社群爭議。

- **付費與免費版本的區別**：

   - **Oracle JDK**：這是 Oracle 提供的官方 JDK（Java Development Kit）。從 Java 11 開始，Oracle JDK 變為商業授權版本，企業需要付費才能使用長期支持 (LTS) 版本。

   - **OpenJDK**：為了維持社群的開放性，Oracle 和開源社群共同維護了 OpenJDK，它是 Java 的免費開源版本。大多數 Java 發行版（如 AdoptOpenJDK、Amazon Corretto、Red Hat OpenJDK）都是基於 OpenJDK 開發，並遵循 GNU General Public License (GPL)。

- **Google 與 Oracle 的 API 版權訴訟**

   - 2010 年 Oracle 起訴 Google 在 Android 中未經授權使用 Java API

   - 歷經多年終在 2021 年最高法院裁定 Google 的使用屬於合理使用（fair use）

### **2\. 版本維護與支持**

- **Oracle Corporation**：作為 Java 的擁有者，Oracle 負責釋出商業版本（Oracle JDK），並提供長期支持服務（需要付費）。

- **OpenJDK 社群**：由 Oracle 和其他公司（如 Red Hat、IBM、Microsoft）共同維護的免費開源版本。OpenJDK 是目前大多數企業和開發者的首選版本，並且有多個免費的變體（如 Amazon Corretto、Azul Zulu）

- **AdoptOpenJDK**：現已轉變為 Eclipse Adoptium，提供基於 OpenJDK 的免費版本，得到眾多社群成員和企業的支持。

這樣的版本區分和授權策略讓 Java 在保持開源特性的同時，也為企業用戶提供了可選的商業支持方案。這種模式使 Java 能夠繼續保持穩定和發展，同時又允許開發者根據需求選擇合適的版本。





## \[Java 應用\]

Java 在許多領域具有領導地位，特別是在企業級應用開發、大數據處理、金融服務、嵌入式系統以及 Android 應用開發等方面。以下是詳細說明及一些持續大量使用 Java 的企業：

### **Java 在各領域的領導地位**

1. **企業級應用開發**

   - **Spring 框架**：Java 是構建企業應用的首選語言，特別是在使用 Spring 框架時，Spring Boot 等工具大大提高了開發效率，使得 Java 成為企業級應用和微服務架構的核心技術。

   - **金融服務與銀行系統**：Java 的穩定性和高安全性，使其在銀行、保險和金融技術（FinTech）領域廣泛使用。它常用來構建交易系統、網上銀行平台和風險管理工具。

   - **持續使用 Java 的企業**：

      - **J.P. Morgan Chase**、**Goldman Sachs** 等金融機構都大量依賴 Java 來維護其後端系統。

      - **Oracle** 和 **IBM** 這些技術公司也在其產品中廣泛使用 Java，並提供 Java 解決方案。

2. **大數據與分佈式系統**

   - **Hadoop 與 Apache Kafka**：大數據處理領域中的領先技術，如 Hadoop 和 Kafka，都是使用 Java 開發的。Java 的強大和穩定性使其適合處理大規模數據處理和分佈式系統架構。

   - **Apache Spark**：雖然它也支持其他語言，但 Java 在 Spark 中仍然扮演著重要角色，許多核心 API 和底層邏輯都是用 Java 開發的。

   - **持續使用 Java 的企業**：

      - **Cloudera** 和 **Hortonworks** 等大數據公司大量依賴 Java 來開發和維護其大數據平台。

      - **Netflix** 和 **LinkedIn** 等公司也使用 Java 來管理其分佈式系統和數據流處理架構。

3. **嵌入式系統與物聯網 (IoT)**

   - Java 在嵌入式系統領域也有廣泛應用，如車載系統、工業控制系統和家庭自動化設備。其跨平台性和穩定性使得它成為物聯網設備和嵌入式應用的熱門選擇。

   - **持續使用 Java 的企業**：

      - **Bosch**、**Siemens** 等工業領域的領導者使用 Java 開發其嵌入式和 IoT 解決方案。

      - **General Motors (GM)** 和其他汽車公司也使用 Java 來開發車載資訊系統。

4. **Android 應用開發**

   - **早期 Android 應用的核心語言**：雖然 Kotlin 現在是 Android 開發的主要語言，但 Java 仍然是 Android 應用的基礎。大部分 Android SDK 和核心 API 都是用 Java 編寫的，因此 Java 在 Android 生態系統中仍具有重要地位。

   - **持續使用 Java 的企業**：

      - **Google** 本身（Android 的開發者）仍然維護著大量基於 Java 的 Android SDK 和工具。

      - 許多移動應用開發公司仍然使用 Java 來維護和升級現有的 Android 應用。

5. **Web 應用與微服務架構**

   - Java 在構建 Web 應用和微服務架構上非常流行，特別是使用 Spring Boot 時。許多大型網站和企業應用程序後端都是用 Java 開發的。

   - **持續使用 Java 的企業**：

      - **Amazon**、**eBay** 和 **Alibaba** 等電商平台使用 Java 來構建其後端系統，以支持大量用戶和交易的處理。

      - **Uber** 和 **Airbnb** 也在其微服務架構中大量使用 Java 來保證系統的可擴展性和穩定性。