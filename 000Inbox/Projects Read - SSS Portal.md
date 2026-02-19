---
tags:
  - frontend
---
# Projects Read - SSS Portal

Certainly, let's break down how to approach reading the Vue code within the given project structure.

**Understanding the Structure**

The directory layout suggests a typical Vue.js project setup, possibly utilizing Vue 3 and Vite. Let's analyze the key parts:

- **`src`**: This is the heart of your Vue application.

   - **`api`**: Likely contains modules responsible for making API calls to backend services or external data sources.

   - **`assets`**: Houses static resources like images, fonts, and stylesheets.

   - **`auth`**: Presumably handles authentication and authorization logic.

   - **`components`**: Holds reusable Vue components that constitute the building blocks of your application's UI.

   - **`config`**: Stores configuration files for various aspects like API endpoints, environment variables, etc.

   - **`languages`**: Might manage internationalization (i18n) or localization features if your app supports multiple languages.

   - **`router`**: Defines the navigation routes within your application and their associated components.

   - **`store`**: Implements the Vuex store, centralizing your application's state management.

   - **`views`**: Contains the top-level components representing different pages or sections of your application.

      - **`App.vue`**: The root component of your Vue application.

- **`main.js`**: The entry point of your application, responsible for creating the Vue instance and mounting it to the DOM.

- **`.env`, `.``[env.prod](env.prod)`**: Environment configuration files, holding variables that might differ between development and production environments.

- **`index.html`**: The main HTML file that serves as the container for your Vue application.

- **`package.json`**: Lists project dependencies and scripts for running various development tasks.

- **`vite.config.js`**: Configuration file for Vite, the build tool used in this project.

**Reading the Code**

1. **Start with `main.js`**: This file bootstraps your application. It's where you'll see how the Vue instance is created, plugins are integrated, and the root component (`App.vue`) is mounted.

2. **Explore `App.vue`**: This is the main component, usually responsible for the overall layout and structure. It often includes the main navigation or routing elements.

3. **Navigate through `router`**: Understand how different views are connected and accessible within your application.

4. **Delve into `views`**: Each component within this folder represents a major part of your application. Examine their structure, data fetching mechanisms, and how they interact with child components.

5. **Analyze `components`**: These are reusable building blocks. Understand their props (inputs), events (outputs), and how they contribute to the overall UI.

6. **Check `store` (if present)**: If Vuex is used, this is where your application's state is managed. Understand how data flows between components and the store.

7. **Inspect `api`**: Examine how data is fetched from external sources and how errors are handled.

**Additional Tips**

- **Use your IDE or code editor**: Features like code navigation, auto-completion, and debugging tools can greatly aid your understanding.

- **Refer to the official Vue.js documentation**: It's an invaluable resource for understanding the framework's concepts and best practices.

- **Run the application**: Seeing the application in action and interacting with it helps connect the code to the user interface.

Remember, the best way to learn is by doing. Start exploring the code, and don't hesitate to experiment and make changes.

Let me know if you have more questions or need further guidance on specific parts of the code!





## Flow

好的，讓我們一步一步來建構權限管理頁面。這份文件針對新手設計，提供清晰的指引，並加入一些實用的建議。

---

### 第一部分：規劃權限管理需求

在開始寫程式碼之前，我們需要先明確權限管理的需求。這包括：

- **角色有哪些？**\
   例如：管理員、一般用戶等。

- **每個角色有哪些權限？**\
   例如：管理員可以新增、刪除用戶，一般用戶只能查看自己的資料。

- **權限如何分配？**\
   例如：通過角色分配、直接分配給用戶。

---

### 第二部分：設定前後端 API 連接

本專案後端使用 C# .NET 建構 API，前端將通過這些 API 進行資料交換。以下是如何在前端承接 API 的簡單指引：

1. **安裝 Axios**\
   Axios 是一個流行的 HTTP 客戶端，用於與後端 API 通信。

   ```bash
   npm install axios
   ```

2. **建立 API 服務檔案**\
   在 `src/services` 資料夾下新增 `api.js`，並配置 Axios。

   ```javascript
   import axios from 'axios';
   
   const api = axios.create({
     baseURL: 'https://your-backend-api.com/api', // 替換為您的後端 API URL
   });
   
   export default api;
   ```

3. **在元件中使用 API**\
   在需要的元件中引入並使用 API 進行資料獲取和提交。

   ```vue
   <script>
   import api from '@/services/api';
   
   export default {
     data() {
       return {
         permissions: [],
         roles: [],
       };
     },
     created() {
       this.fetchPermissions();
       this.fetchRoles();
     },
     methods: {
       async fetchPermissions() {
         try {
           const response = await api.get('/permissions');
           this.permissions = response.data;
         } catch (error) {
           console.error('獲取權限失敗', error);
         }
       },
       async fetchRoles() {
         try {
           const response = await api.get('/roles');
           this.roles = response.data;
         } catch (error) {
           console.error('獲取角色失敗', error);
         }
       },
       // 其他方法...
     },
   };
   </script>
   ```

---

### 第三部分：新增 Vue 元件

根據您的專案結構，我們將在 `components/permissions` 資料夾下新增 Vue 元件。

- **PermissionManagement.vue**\
   這個元件將是權限管理的主要頁面，負責顯示權限列表、新增、編輯、刪除權限等功能。

- **RoleManagement.vue**\
   這個元件負責角色管理，包括顯示角色列表、新增、編輯、刪除角色，以及為角色分配權限。

---

### 第四部分：設計元件模板 (template)

我們將使用 **Tailwind CSS** 來設計樣式，並鼓勵使用 **daisyUI** 提供的資源來加快開發速度。

### 安裝 Tailwind CSS 和 daisyUI

1. **安裝 Tailwind CSS**

   ```bash
   npm install -D tailwindcss
   npx tailwindcss init
   ```

2. **配置 Tailwind CSS**\
   在 `tailwind.config.js` 中加入 daisyUI 插件。

   ```javascript
   module.exports = {
     content: ['./src/**/*.{vue,js,ts,jsx,tsx}'],
     theme: {
       extend: {},
     },
     plugins: [require('daisyui')],
   };
   ```

3. **引入 Tailwind CSS**\
   在 `src/assets/tailwind.css` 添加以下內容：

   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

4. **在主入口文件引入 Tailwind CSS**\
   在 `main.js` 或 `main.ts` 中引入：

   ```javascript
   import '@/assets/tailwind.css';
   ```

### PermissionManagement.vue

```vue
<template>
  <div class="p-4">
    <h2 class="text-2xl font-bold mb-4">權限管理</h2>

    <table class="table w-full">
      <thead>
        <tr>
          <th>權限名稱</th>
          <th>權限描述</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="permission in permissions" :key="permission.id">
          <td>{{ permission.name }}</td>
          <td>{{ permission.description }}</td>
          <td>
            <button class="btn btn-sm btn-primary mr-2" @click="editPermission(permission)">編輯</button>
            <button class="btn btn-sm btn-error" @click="deletePermission(permission)">刪除</button>
          </td>
        </tr>
      </tbody>
    </table>

    <button class="btn btn-success mt-4" @click="addPermission">新增權限</button>
  </div>
</template>
```

### RoleManagement.vue

```vue
<template>
  <div class="p-4">
    <h2 class="text-2xl font-bold mb-4">角色管理</h2>

    <table class="table w-full">
      <thead>
        <tr>
          <th>角色名稱</th>
          <th>角色描述</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="role in roles" :key="role.id">
          <td>{{ role.name }}</td>
          <td>{{ role.description }}</td>
          <td>
            <button class="btn btn-sm btn-primary mr-2" @click="editRole(role)">編輯</button>
            <button class="btn btn-sm btn-error mr-2" @click="deleteRole(role)">刪除</button>
            <button class="btn btn-sm btn-secondary" @click="assignPermissions(role)">分配權限</button>
          </td>
        </tr>
      </tbody>
    </table>

    <button class="btn btn-success mt-4" @click="addRole">新增角色</button>
  </div>
</template>
```

---

### 第五部分：添加元件邏輯 (script)

在 `<script>` 部分添加元件的邏輯，包括資料處理、方法定義等。

```vue
<script>
import api from '@/services/api';

export default {
  data() {
    return {
      permissions: [], // 存放權限列表
      roles: [], // 存放角色列表
    };
  },
  created() {
    this.fetchPermissions();
    this.fetchRoles();
  },
  methods: {
    async fetchPermissions() {
      try {
        const response = await api.get('/permissions');
        this.permissions = response.data;
      } catch (error) {
        console.error('獲取權限失敗', error);
      }
    },
    async addPermission() {
      // 實現新增權限的邏輯
    },
    async editPermission(permission) {
      // 實現編輯權限的邏輯
    },
    async deletePermission(permission) {
      // 實現刪除權限的邏輯
    },
    async fetchRoles() {
      try {
        const response = await api.get('/roles');
        this.roles = response.data;
      } catch (error) {
        console.error('獲取角色失敗', error);
      }
    },
    async addRole() {
      // 實現新增角色的邏輯
    },
    async editRole(role) {
      // 實現編輯角色的邏輯
    },
    async deleteRole(role) {
      // 實現刪除角色的邏輯
    },
    async assignPermissions(role) {
      // 實現為角色分配權限的邏輯
    },
  },
};
</script>
```

---

### 第六部分：配置路由

在 `router/index.js` 中配置路由，讓使用者可以訪問權限管理和角色管理頁面。

```javascript
import Vue from 'vue';
import VueRouter from 'vue-router';
import PermissionManagement from '@/components/permissions/PermissionManagement.vue';
import RoleManagement from '@/components/permissions/RoleManagement.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/permissions',
    name: 'PermissionManagement',
    component: PermissionManagement
  },
  {
    path: '/roles',
    name: 'RoleManagement',
    component: RoleManagement
  }
  // ...其他路由
];

const router = new VueRouter({
  routes
});

export default router;
```

---

### 第七部分：整合到主頁面

最後，在主頁面（如 `App.vue` 或其他佈局元件）中添加導航連結，讓使用者可以進入權限管理頁面。

```vue
<template>
  <div id="app">
    <nav class="bg-gray-800 p-4">
      <ul class="flex space-x-4">
        <li>
          <router-link to="/permissions" class="text-white hover:text-gray-300">權限管理</router-link>
        </li>
        <li>
          <router-link to="/roles" class="text-white hover:text-gray-300">角色管理</router-link>
        </li>
      </ul>
    </nav>
    <router-view/>
  </div>
</template>
```

---

### 接下來的步驟

- **實現元件邏輯**：在 `methods` 中實現獲取權限列表、新增、編輯、刪除權限、獲取角色列表、新增、編輯、刪除角色、為角色分配權限等方法。

- **前後端互動**：使用 Axios 與後端 API 進行互動，獲取和更新權限、角色資料。

- **權限控制**：在路由或元件中實現權限控制，確保只有授權的使用者才能訪問權限管理頁面和執行相關操作。

---

### 附加提示

- **使用 Tailwind CSS**：本專案鼓勵使用 Tailwind CSS 來快速建立響應式和美觀的介面。您可以參考 [Tailwind CSS 官方文件](https://tailwindcss.com/docs) 了解更多。

- **利用 daisyUI**：daisyUI 是基於 Tailwind CSS 的元件庫，提供許多現成的 UI 元件，能夠加快開發速度。建議您查閱 [daisyUI 資源](https://daisyui.com/) 以獲取更多元件範例和使用方法。

- **使用 Vue Devtools**：在開發過程中，您可以使用 Vue Devtools 等工具來調試和檢查元件的狀態和資料。

- **尋求幫助**：如果遇到困難，可以查閱 Vue.js 官方文件、網上教程或加入社群尋求幫助。

---



## 頁面規劃

### Vue 3 和 Tailwind CSS 開發指南：產品分類與功能管理頁面

這份指南將帶領您使用 Vue 3 和 Tailwind CSS 從零開始開發一個產品分類與功能管理的前端頁面。即使您是新手，也能通過逐步的說明和完整的範例，輕鬆完成開發。

---

## 目錄

1. [開發環境設置](#1-%E9%96%8B%E7%99%BC%E7%92%B0%E5%A2%83%E8%A8%AD%E7%BD%AE)

2. [項目結構概述](#2-%E9%A0%85%E7%9B%AE%E7%B5%90%E6%A7%8B%E6%A6%82%E8%BF%B0)

3. [安裝並配置 Tailwind CSS](#3-%E5%AE%89%E8%A3%9D%E4%B8%A6%E9%85%8D%E7%BD%AE-tailwind-css)

4. [建立主要組件](#4-%E5%BB%BA%E7%AB%8B%E4%B8%BB%E8%A6%81%E7%B5%84%E4%BB%B6)

   - [4\.1. 產品分類選單](#41-%E7%94%A2%E5%93%81%E5%88%86%E9%A1%9E%E9%81%B8%E5%96%AE)

   - [4\.2. 查詢按鈕](#42-%E6%9F%A5%E8%A9%A2%E6%8C%89%E9%88%95)

   - [4\.3. 產品分類列表](#43-%E7%94%A2%E5%93%81%E5%88%86%E9%A1%9E%E5%88%97%E8%A1%A8)

      - [4\.3.1. 表格標頭](#431-%E8%A1%A8%E6%A0%BC%E6%A8%99%E9%A0%AD)

      - [4\.3.2. 表格列](#432-%E8%A1%A8%E6%A0%BC%E5%88%97)

   - [4\.4. 新增分類按鈕](#44-%E6%96%B0%E5%A2%9E%E5%88%86%E9%A1%9E%E6%8C%89%E9%88%95)

   - [4\.5. 分頁功能](#45-%E5%88%86%E9%A0%81%E5%8A%9F%E8%83%BD)

   - [4\.6. 提示文字](#46-%E6%8F%90%E7%A4%BA%E6%96%87%E5%AD%97)

5. [整合後端 API](#5-%E6%95%B4%E5%90%88%E5%BE%8C%E7%AB%AF-api)

6. [完整範例代碼](#6-%E5%AE%8C%E6%95%B4%E7%AF%84%E4%BE%8B%E4%BB%A3%E7%A2%BC)

7. [結語](#7-%E7%B5%90%E8%AA%9E)

---

## 1\. 開發環境設置

在開始開發之前，您需要設置開發環境。這包括安裝 Node.js、Vue CLI 和初始化 Vue 3 項目。

### 1\.1. 安裝 Node.js

請從 [Node.js 官方網站](https://nodejs.org/) 下載並安裝最新的 LTS 版本。

### 1\.2. 安裝 Vue CLI

打開終端（Terminal）並執行以下命令安裝 Vue CLI：

```bash
npm install -g @vue/cli
```

確認安裝成功：

```bash
vue --version
```

### 1\.3. 初始化 Vue 3 項目

使用 Vue CLI 創建一個新的 Vue 3 項目：

```bash
vue create product-category-management
```

在提示中選擇以下選項：

- **Choose a preset**: Manually select features

- **Features to include**:

   - Choose **Vue 3** (預設)

   - Babel

   - Router

   - Vuex (如果需要狀態管理，這裡可以選擇)

   - Linter/Formatter (可選)

完成選擇後，等待項目初始化完成。

進入項目目錄：

```bash
cd product-category-management
```

## 2\. 項目結構概述

在這個項目中，我們將主要在 `src` 目錄下進行開發。以下是主要文件和目錄的簡要介紹：

- `src/main.js`: 項目入口文件

- `src/App.vue`: 根組件

- `src/components/`: 存放自定義組件

- `src/views/`: 存放不同頁面的組件

- `src/router/index.js`: 路由配置

- `src/assets/`: 靜態資源

- `tailwind.config.js`: Tailwind CSS 配置文件

## 3\. 安裝並配置 Tailwind CSS

### 3\.1. 安裝 Tailwind CSS

在項目目錄下運行以下命令安裝 Tailwind CSS 及其依賴：

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

這將生成 `tailwind.config.js` 和 `postcss.config.js` 文件。

### 3\.2. 配置 `tailwind.config.js`

打開 `tailwind.config.js`，並設置內容路徑：

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

### 3\.3. 添加 Tailwind 指令到 CSS

在 `src/assets/` 目錄下創建 `styles.css`（如果尚未存在），並添加以下內容：

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 3\.4. 引用 CSS

在 `src/main.js` 中引入 `styles.css`：

```javascript
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/styles.css' // 引入 Tailwind CSS

createApp(App).use(router).mount('#app')
```

### 3\.5. 驗證 Tailwind CSS

運行項目以確保 Tailwind CSS 配置正確：

```bash
npm run serve
```

在瀏覽器中打開 `http://localhost:8080`，並確保應用程序正常運行。

## 4\. 建立主要組件

我們將在 `src/views/` 目錄下創建一個名為 `ProductCategory.vue` 的頁面組件，該組件將包含所有需要的功能。

### 4\.1. 產品分類選單

首先，讓我們創建一個下拉選單，用於選擇產品分類進行篩選。這個選單的數據將從後端 API 獲取。

#### 4\.1.1. 創建 `ProductCategory.vue`

在 `src/views/` 目錄下創建 `ProductCategory.vue`，並添加基本結構：

```vue
<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">產品分類管理</h1>
    <!-- 其他元素將在後續添加 -->
  </div>
</template>

<script>
export default {
  name: 'ProductCategory',
  data() {
    return {
      categories: [], // 產品分類數據
      selectedCategory: null, // 選中的分類
      // 其他數據屬性
    };
  },
  mounted() {
    this.fetchCategories();
  },
  methods: {
    fetchCategories() {
      // 假設有一個 API 端點 /api/categories 返回分類數據
      fetch('/api/categories')
        .then(response => response.json())
        .then(data => {
          this.categories = data;
        })
        .catch(error => {
          console.error('Error fetching categories:', error);
        });
    },
  },
};
</script>

<style scoped>
/* 可選的樣式 */
</style>
```

#### 4\.1.2. 添加下拉選單到模板

更新 `<template>` 部分，添加下拉選單和查詢按鈕：

```vue
<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">產品分類管理</h1>
    <div class="flex justify-between mb-4">
      <div class="flex space-x-2">
        <select v-model="selectedCategory" class="border border-gray-300 rounded px-3 py-2">
          <option value="">全部分類</option>
          <option v-for="category in categories" :key="category.id" :value="category.id">
            {{ category.name }}
          </option>
        </select>
        <button @click="queryCategories" class="bg-blue-500 text-white px-4 py-2 rounded">
          查詢
        </button>
      </div>
      <button @click="addCategory" class="bg-green-500 text-white px-4 py-2 rounded">
        新增分類
      </button>
    </div>
    <!-- 其他元素將在後續添加 -->
  </div>
</template>
```

#### 4\.1.3. 添加查詢方法

在 `<script>` 部分添加 `queryCategories` 方法和 `addCategory` 方法：

```javascript
methods: {
  fetchCategories() {
    // 假設有一個 API 端點 /api/categories 返回分類數據
    fetch('/api/categories')
      .then(response => response.json())
      .then(data => {
        this.categories = data;
      })
      .catch(error => {
        console.error('Error fetching categories:', error);
      });
  },
  queryCategories() {
    // 根據選擇的分類來查詢數據
    // 這裡可以調用一個方法來獲取表格數據
    this.fetchCategoryData();
  },
  addCategory() {
    // 跳轉到新增分類頁面
    this.$router.push('/add-category');
  },
  fetchCategoryData(page = 1) {
    // 將根據選中的分類和頁碼來獲取數據
    const params = new URLSearchParams();
    if (this.selectedCategory) {
      params.append('category', this.selectedCategory);
    }
    params.append('page', page);
    fetch(`/api/categories?${params.toString()}`)
      .then(response => response.json())
      .then(data => {
        this.categoryData = data.items;
        this.pagination = data.pagination;
      })
      .catch(error => {
        console.error('Error fetching category data:', error);
      });
  },
},
```

### 4\.2. 查詢按鈕

查詢按鈕已在上一步中添加，並綁定了 `queryCategories` 方法。當用戶選擇分類並點擊查詢按鈕時，將根據選中的分類從後端獲取相應的數據。

### 4\.3. 產品分類列表

接下來，讓我們構建動態顯示產品分類的表格。

#### 4\.3.1. 表格標頭

在 `<template>` 中添加表格標頭：

```vue
<template>
  <div class="p-6">
    <!-- 上方元素 -->
    <table class="min-w-full bg-white border border-gray-200">
      <thead>
        <tr>
          <th class="py-2 px-4 border-b">產品分類</th>
          <th class="py-2 px-4 border-b">排序</th>
          <th class="py-2 px-4 border-b">創建時間</th>
          <th class="py-2 px-4 border-b">狀態</th>
          <th class="py-2 px-4 border-b">操作</th>
        </tr>
      </thead>
      <tbody>
        <!-- 表格列將在後續添加 -->
      </tbody>
    </table>
    <!-- 分頁功能 -->
  </div>
</template>
```

#### 4\.3.2. 表格列

在 `<tbody>` 中使用 `v-for` 指令迭代顯示每一行數據：

```vue
<tbody>
  <tr v-for="category in categoryData" :key="category.id" class="hover:bg-gray-100">
    <td class="py-2 px-4 border-b">{{ category.name }}</td>
    <td class="py-2 px-4 border-b">{{ category.sort_order }}</td>
    <td class="py-2 px-4 border-b">{{ formatDate(category.created_at) }}</td>
    <td class="py-2 px-4 border-b">
      <span
        :class="category.status === 'active' ? 'text-green-500' : 'text-red-500'"
      >
        {{ category.status === 'active' ? '啟用' : '停用' }}
      </span>
    </td>
    <td class="py-2 px-4 border-b">
      <button @click="editCategory(category.id)" class="text-blue-500 hover:underline">
        編輯
      </button>
    </td>
  </tr>
</tbody>
```

#### 4\.3.3. 添加表格數據和方法

在 `<script>` 中添加 `categoryData` 和 `pagination` 的數據屬性，並實現 `fetchCategoryData`、`formatDate` 和 `editCategory` 方法：

```javascript
data() {
  return {
    categories: [], // 產品分類數據
    selectedCategory: null, // 選中的分類
    categoryData: [], // 表格顯示的分類數據
    pagination: {
      currentPage: 1,
      totalPages: 1,
      // 其他分頁相關數據
    },
  };
},
mounted() {
  this.fetchCategories();
  this.fetchCategoryData();
},
methods: {
  fetchCategories() {
    // 假設有一個 API 端點 /api/categories 返回分類數據
    fetch('/api/categories')
      .then(response => response.json())
      .then(data => {
        this.categories = data;
      })
      .catch(error => {
        console.error('Error fetching categories:', error);
      });
  },
  queryCategories() {
    // 根據選擇的分類來查詢數據
    this.fetchCategoryData();
  },
  addCategory() {
    // 跳轉到新增分類頁面
    this.$router.push('/add-category');
  },
  editCategory(id) {
    // 跳轉到編輯分類頁面，傳遞分類ID
    this.$router.push(`/edit-category/${id}`);
  },
  fetchCategoryData(page = 1) {
    // 將根據選中的分類和頁碼來獲取數據
    const params = new URLSearchParams();
    if (this.selectedCategory) {
      params.append('category', this.selectedCategory);
    }
    params.append('page', page);
    fetch(`/api/categories?${params.toString()}`)
      .then(response => response.json())
      .then(data => {
        this.categoryData = data.items;
        this.pagination = data.pagination;
      })
      .catch(error => {
        console.error('Error fetching category data:', error);
      });
  },
  formatDate(dateStr) {
    const date = new Date(dateStr);
    return date.toLocaleString();
  },
},
```

### 4\.4. 新增分類按鈕

新增分類按鈕已在先前的 `<template>` 中添加，並綁定了 `addCategory` 方法，該方法將跳轉到新增分類的頁面。您需要根據路由配置添加相應的頁面。

### 4\.5. 分頁功能

最後，讓我們添加分頁功能，使用戶能夠瀏覽多頁數據。

#### 4\.5.1. 添加分頁模板

在 `<template>` 中添加分頁控制：

```vue
<!-- 在表格下方添加分頁 -->
<div class="flex justify-end mt-4">
  <nav class="flex items-center">
    <button
      :disabled="pagination.currentPage === 1"
      @click="changePage(pagination.currentPage - 1)"
      class="px-3 py-1 border rounded-l disabled:opacity-50"
    >
      上一頁
    </button>
    <span class="px-4 py-1 border-t border-b">
      第 {{ pagination.currentPage }} 頁 / 共 {{ pagination.totalPages }} 頁
    </span>
    <button
      :disabled="pagination.currentPage === pagination.totalPages"
      @click="changePage(pagination.currentPage + 1)"
      class="px-3 py-1 border rounded-r disabled:opacity-50"
    >
      下一頁
    </button>
  </nav>
</div>
```

#### 4\.5.2. 添加分頁方法

在 `<script>` 中添加 `changePage` 方法：

```javascript
methods: {
  // 之前的方法...
  changePage(page) {
    if (page < 1 || page > this.pagination.totalPages) return;
    this.fetchCategoryData(page);
  },
},
```

### 4\.6. 提示文字

在表格上方添加提示文字，提醒用戶點擊產品分類進行下一步操作。

#### 4\.6.1. 添加提示文字到模板

在 `<template>` 中添加提示文字：

```vue
<div class="mb-4">
  <span class="text-gray-600">
    點擊產品分類可進行下一步操作。
  </span>
</div>
```

將這段放在下拉選單和表格之間：

```vue
<div class="flex justify-between mb-4">
  <!-- 下拉選單和按鈕 -->
</div>
<div class="mb-4">
  <span class="text-gray-600">
    點擊產品分類可進行下一步操作。
  </span>
</div>
<table class="min-w-full bg-white border border-gray-200">
  <!-- 表格內容 -->
</table>
```

## 5\. 整合後端 API

在這個範例中，我們假設有以下 API 端點：

- `GET /api/categories`: 獲取所有產品分類

- `GET /api/categories?category=ID&page=1`: 根據分類和頁碼獲取分類數據

- `POST /api/categories`: 新增分類

- `PUT /api/categories/:id`: 編輯分類

為了使這個範例自包含，我們將使用 [JSON Server](https://github.com/typicode/json-server) 來模擬後端 API。

### 5\.1. 安裝 JSON Server

在項目目錄外或另一終端中安裝 JSON Server：

```bash
npm install -g json-server
```

### 5\.2. 創建 `db.json`

在項目根目錄外創建一個名為 `db.json` 的文件，並添加以下內容：

```json
{
  "categories": [
    {
      "id": 1,
      "name": "電子產品",
      "sort_order": 1,
      "created_at": "2023-01-01T10:00:00Z",
      "status": "active"
    },
    {
      "id": 2,
      "name": "家居用品",
      "sort_order": 2,
      "created_at": "2023-02-15T12:30:00Z",
      "status": "inactive"
    },
    {
      "id": 3,
      "name": "服裝",
      "sort_order": 3,
      "created_at": "2023-03-20T09:15:00Z",
      "status": "active"
    }
    // 可以添加更多測試數據
  ]
}
```

### 5\.3. 啟動 JSON Server

在終端中運行以下命令啟動 JSON Server：

```bash
json-server --watch db.json --port 3000
```

這將啟動一個假設的後端 API 服務，端口為 `3000`。

### 5\.4. 更新 Vue 項目的 API 路徑

在 `ProductCategory.vue` 中，更新 API 路徑以指向本地 JSON Server：

```javascript
methods: {
  fetchCategories() {
    fetch('http://localhost:3000/categories')
      .then(response => response.json())
      .then(data => {
        this.categories = data;
      })
      .catch(error => {
        console.error('Error fetching categories:', error);
      });
  },
  fetchCategoryData(page = 1) {
    const params = new URLSearchParams();
    if (this.selectedCategory) {
      params.append('category', this.selectedCategory);
    }
    params.append('_page', page);
    params.append('_limit', 5); // 每頁顯示 5 條數據
    fetch(`http://localhost:3000/categories?${params.toString()}`)
      .then(response => {
        const total = response.headers.get('X-Total-Count');
        this.pagination = {
          currentPage: page,
          totalPages: Math.ceil(total / 5),
        };
        return response.json();
      })
      .then(data => {
        this.categoryData = data;
      })
      .catch(error => {
        console.error('Error fetching category data:', error);
      });
  },
},
```

注意：

- JSON Server 支持分頁參數 `_page` 和 `_limit`。

- JSON Server 不支持根據分類 ID 過濾，您可能需要手動處理這部分或使用更強大的後端服務。

## 6\. 完整範例代碼

以下是 `ProductCategory.vue` 的完整代碼，結合了所有上述部分：

```vue
<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">產品分類管理</h1>
    <div class="flex justify-between mb-4">
      <div class="flex space-x-2">
        <select v-model="selectedCategory" class="border border-gray-300 rounded px-3 py-2">
          <option value="">全部分類</option>
          <option v-for="category in categories" :key="category.id" :value="category.id">
            {{ category.name }}
          </option>
        </select>
        <button @click="queryCategories" class="bg-blue-500 text-white px-4 py-2 rounded">
          查詢
        </button>
      </div>
      <button @click="addCategory" class="bg-green-500 text-white px-4 py-2 rounded">
        新增分類
      </button>
    </div>
    <div class="mb-4">
      <span class="text-gray-600">
        點擊產品分類可進行下一步操作。
      </span>
    </div>
    <table class="min-w-full bg-white border border-gray-200">
      <thead>
        <tr>
          <th class="py-2 px-4 border-b">產品分類</th>
          <th class="py-2 px-4 border-b">排序</th>
          <th class="py-2 px-4 border-b">創建時間</th>
          <th class="py-2 px-4 border-b">狀態</th>
          <th class="py-2 px-4 border-b">操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="category in categoryData" :key="category.id" class="hover:bg-gray-100">
          <td class="py-2 px-4 border-b">{{ category.name }}</td>
          <td class="py-2 px-4 border-b">{{ category.sort_order }}</td>
          <td class="py-2 px-4 border-b">{{ formatDate(category.created_at) }}</td>
          <td class="py-2 px-4 border-b">
            <span
              :class="category.status === 'active' ? 'text-green-500' : 'text-red-500'"
            >
              {{ category.status === 'active' ? '啟用' : '停用' }}
            </span>
          </td>
          <td class="py-2 px-4 border-b">
            <button @click="editCategory(category.id)" class="text-blue-500 hover:underline">
              編輯
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="flex justify-end mt-4">
      <nav class="flex items-center">
        <button
          :disabled="pagination.currentPage === 1"
          @click="changePage(pagination.currentPage - 1)"
          class="px-3 py-1 border rounded-l disabled:opacity-50"
        >
          上一頁
        </button>
        <span class="px-4 py-1 border-t border-b">
          第 {{ pagination.currentPage }} 頁 / 共 {{ pagination.totalPages }} 頁
        </span>
        <button
          :disabled="pagination.currentPage === pagination.totalPages"
          @click="changePage(pagination.currentPage + 1)"
          class="px-3 py-1 border rounded-r disabled:opacity-50"
        >
          下一頁
        </button>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductCategory',
  data() {
    return {
      categories: [], // 產品分類數據
      selectedCategory: '', // 選中的分類ID
      categoryData: [], // 表格顯示的分類數據
      pagination: {
        currentPage: 1,
        totalPages: 1,
      },
    };
  },
  mounted() {
    this.fetchCategories();
    this.fetchCategoryData();
  },
  methods: {
    fetchCategories() {
      fetch('http://localhost:3000/categories')
        .then(response => response.json())
        .then(data => {
          this.categories = data;
        })
        .catch(error => {
          console.error('Error fetching categories:', error);
        });
    },
    queryCategories() {
      this.fetchCategoryData();
    },
    addCategory() {
      this.$router.push('/add-category');
    },
    editCategory(id) {
      this.$router.push(`/edit-category/${id}`);
    },
    fetchCategoryData(page = 1) {
      const params = new URLSearchParams();
      if (this.selectedCategory) {
        params.append('category', this.selectedCategory);
      }
      params.append('_page', page);
      params.append('_limit', 5); // 每頁顯示 5 條數據
      fetch(`http://localhost:3000/categories?${params.toString()}`)
        .then(response => {
          const total = response.headers.get('X-Total-Count');
          this.pagination = {
            currentPage: page,
            totalPages: Math.ceil(total / 5),
          };
          return response.json();
        })
        .then(data => {
          this.categoryData = data;
        })
        .catch(error => {
          console.error('Error fetching category data:', error);
        });
    },
    changePage(page) {
      if (page < 1 || page > this.pagination.totalPages) return;
      this.fetchCategoryData(page);
    },
    formatDate(dateStr) {
      const date = new Date(dateStr);
      return date.toLocaleString();
    },
  },
};
</script>

<style scoped>
/* 可選的樣式 */
</style>
```

### 6\.1. 路由配置

確保您的路由配置包含 `ProductCategory.vue`，以及新增和編輯分類頁面的路由。

打開 `src/router/index.js`，並添加以下內容：

```javascript
import { createRouter, createWebHistory } from 'vue-router';
import ProductCategory from '../views/ProductCategory.vue';
// 假設您已經創建了 AddCategory.vue 和 EditCategory.vue
import AddCategory from '../views/AddCategory.vue';
import EditCategory from '../views/EditCategory.vue';

const routes = [
  {
    path: '/',
    name: 'ProductCategory',
    component: ProductCategory
  },
  {
    path: '/add-category',
    name: 'AddCategory',
    component: AddCategory
  },
  {
    path: '/edit-category/:id',
    name: 'EditCategory',
    component: EditCategory,
    props: true
  },
  // 其他路由
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
```

### 6\.2. 創建新增和編輯分類頁面

為了完成路由配置，我們需要創建 `AddCategory.vue` 和 `EditCategory.vue`。以下是簡單的範例：

#### 6\.2.1. `AddCategory.vue`

```vue
<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">新增產品分類</h1>
    <form @submit.prevent="submitForm" class="space-y-4">
      <div>
        <label class="block text-gray-700">名稱</label>
        <input v-model="name" type="text" class="w-full border border-gray-300 rounded px-3 py-2" required />
      </div>
      <div>
        <label class="block text-gray-700">排序</label>
        <input v-model.number="sort_order" type="number" class="w-full border border-gray-300 rounded px-3 py-2" required />
      </div>
      <div>
        <label class="block text-gray-700">狀態</label>
        <select v-model="status" class="w-full border border-gray-300 rounded px-3 py-2" required>
          <option value="active">啟用</option>
          <option value="inactive">停用</option>
        </select>
      </div>
      <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded">提交</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'AddCategory',
  data() {
    return {
      name: '',
      sort_order: 1,
      status: 'active',
    };
  },
  methods: {
    submitForm() {
      const newCategory = {
        name: this.name,
        sort_order: this.sort_order,
        created_at: new Date().toISOString(),
        status: this.status,
      };
      fetch('http://localhost:3000/categories', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(newCategory)
      })
        .then(response => response.json())
        .then(data => {
          alert('新增成功！');
          this.$router.push('/');
        })
        .catch(error => {
          console.error('Error adding category:', error);
        });
    },
  },
};
</script>

<style scoped>
/* 可選的樣式 */
</style>
```

#### 6\.2.2. `EditCategory.vue`

```vue
<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">編輯產品分類</h1>
    <form @submit.prevent="submitForm" class="space-y-4" v-if="category">
      <div>
        <label class="block text-gray-700">名稱</label>
        <input v-model="category.name" type="text" class="w-full border border-gray-300 rounded px-3 py-2" required />
      </div>
      <div>
        <label class="block text-gray-700">排序</label>
        <input v-model.number="category.sort_order" type="number" class="w-full border border-gray-300 rounded px-3 py-2" required />
      </div>
      <div>
        <label class="block text-gray-700">狀態</label>
        <select v-model="category.status" class="w-full border border-gray-300 rounded px-3 py-2" required>
          <option value="active">啟用</option>
          <option value="inactive">停用</option>
        </select>
      </div>
      <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">提交</button>
    </form>
    <div v-else>
      加載中...
    </div>
  </div>
</template>

<script>
export default {
  name: 'EditCategory',
  props: ['id'],
  data() {
    return {
      category: null,
    };
  },
  mounted() {
    this.fetchCategory();
  },
  methods: {
    fetchCategory() {
      fetch(`http://localhost:3000/categories/${this.id}`)
        .then(response => response.json())
        .then(data => {
          this.category = data;
        })
        .catch(error => {
          console.error('Error fetching category:', error);
        });
    },
    submitForm() {
      fetch(`http://localhost:3000/categories/${this.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.category)
      })
        .then(response => response.json())
        .then(data => {
          alert('更新成功！');
          this.$router.push('/');
        })
        .catch(error => {
          console.error('Error updating category:', error);
        });
    },
  },
};
</script>

<style scoped>
/* 可選的樣式 */
</style>
```

### 6\.3. 測試應用

確保 JSON Server 已經運行，然後啟動 Vue 應用：

```bash
npm run serve
```

在瀏覽器中打開 `http://localhost:8080`，您應該能看到產品分類管理頁面，並可以進行查詢、新增和編輯操作。

## 7\. 結語

通過本指南，您已經學會如何使用 Vue 3 和 Tailwind CSS 開發一個功能豐富的產品分類與功能管理頁面。這包括：

- 設置開發環境和配置 Tailwind CSS

- 構建動態的下拉選單和查詢按鈕

- 創建顯示產品分類的表格

- 添加狀態顯示和編輯操作

- 實現分頁功能

- 整合後端 API（使用 JSON Server 模擬）

這些基礎知識和技能將為您開發更多複雜的應用程序奠定堅實的基礎。隨著經驗的積累，您可以進一步優化界面、增加更多功能，如搜索、排序、刪除等，以及提升應用的性能和可用性。

祝您開發順利！