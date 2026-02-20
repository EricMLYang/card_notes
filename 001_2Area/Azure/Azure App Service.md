---
tags:
  - azure
---
# Azure App Service

- try :

   - `pm2 serve /home/site/wwwroot/dist --spa --no-daemon`

just give config file of PM2 (PM2 configuration file or your script file)

ecosystem.config.js



## Set Environment Variable

-  **設定環境變數**

   - 在 Azure Portal 中，進入您的 App Service 應用程式。

   - 點選「設定」 -> 「組態」。

   - 在「應用程式設定」區段，新增您的資料庫連線資訊作為環境變數。例如：

      - 名稱：`DB_HOST`，值：`your_database_host`

      - 名稱：`DB_USER`，值：`your_database_user`

      - 名稱：`DB_PASSWORD`，值：`your_database_password`

      - 名稱：`DB_NAME`，值：`your_database_name`

   - 儲存您的變更。

- Get the environment in Python code

```python
import os

# ... other imports ...

# 從環境變數獲取資料庫連線資訊
db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')
```



## Basic Concept

- [Azure App Service Doc](https://learn.microsoft.com/en-us/azure/app-service/)

- **[Configure an App Service app](https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal)**

   - In App Service, app settings are variables passed as environment variables to the application code.

   - For Linux apps and custom containers, App Service passes app settings to the container using the `--env` flag to set the environment variable in the container.

- **[Configure a Node.js app for Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/configure-language-nodejs?pivots=platform-linux)**

   - Node.js apps must be deployed with all the required NPM dependencies

      The App Service deployment engine automatically runs `npm install --production `for you when you deploy a Git repository, or a Zip package with build automation enabled

   - App Service sets the environment variable `PORT` in the Node.js container, and forwards the incoming requests to your container at that port number.

   - The Node.js containers come with [PM2](https://pm2.keymetrics.io/), a production process manager. You can configure your app to start with PM2, or with NPM, or with a custom command.

## Node.js   &   Vue.js

- Node.js Application

- Vue.js Router/ Deployment

- Basic Web

- Static Page  vs  Dynamic ( Application )

   - do you need run the service side code (JS) or not 

### How to deploy frontend dist to Azure app service 

- What is Build

   - 網站本質上是由 **HTML, CSS, JaveScript** 文件所組成，User 瀏覽器收這些格式文字，再渲染成使用者所看到的畫面  ([Reference](https://app.heptabase.com/e2b4d180-4e0a-45c6-9989-dea4bc781f8a/card/80877e71-9e3b-412b-b6d8-11257ccb2bcf))

   - \*.vue file need to be converted to above file by **Vite ( npx vite build )**

   - `npm run build` = `npx vite build`: it will start the bundle process

   - `npm run preview` = npx vite preview —port 5173 

   - After Build, you will get directory **dist**

- 

### Deploy by run the frontend code

- make sure memory: at least 8G

   - Hardware Scale up 

   - Set environment variables (memory, port … )

      - ENABLE_ORYX_BUILD is kind of deploy method

      - when you deploy, please delete dir “node_modules“, this dir is the result of num install

      ![image 58.png](./Azure%20App%20Service-assets/image%2058.png)

      ![image 59.png](./Azure%20App%20Service-assets/image%2059.png)

      

      

      ```plain
      
      [
        {
          "name": "ENABLE_ORYX_BUILD",
          "value": "true",
          "slotSetting": false
        },
        {
          "name": "NODE_OPTIONS",
          "value": "--max-old-space-size=8192",
          "slotSetting": false
        },
        {
          "name": "PORT",
          "value": "5173",
          "slotSetting": false
        },
        {
          "name": "SCM_DO_BUILD_DURING_DEPLOYMENT",
          "value": "true",
          "slotSetting": false
        }
      ]
      ```

      

## Error Handle Tips

- Check 日誌文件 

   - Url : <https://sss-frontend.scm.azurewebsites.net/api/dump>

   - 會直接下載一個日誌文件

-  查看project的文件是否已經被成功部署

   - <https://sss-frontend.scm.azurewebsites.net/newui/fileManager> 

   - site -> wwwroot

![image 60.png](./Azure%20App%20Service-assets/image%2060.png)



- Check Log