---
tags:
  - frontend
---
# CSS 

## \[ 學習素材 \]

### 100 Days CSS Challenge

- URL : <https://100dayscss.com/>

- Why recommand ?

   - 很多想要提升自己 CSS 能力的人，不論是前端工程師、設計師，或者介於兩者之間的設計工程師，都非常推薦 100 Days CSS Challenge 這個免費學習素材。

   - 最推薦這個素材有幾個原因

      - 實作導向：想把 CSS 學精通，最有效的方式，不是看很多素材或課程，而是要實際動手下去做

      - 類型多元：連續 100 天，每天一個 CSS 挑戰，會練到各種你可能甚至沒想過存在的 CSS 寫法。假如每題都練過，基本上工作會遇到的 CSS 都不會是難題

      - 社群學習：這個挑戰結合了社群分享，如果你寫不出來，也不用擔心除了有官方參考的答案，也可以看社群中其他人寫的成果。甚至同一個題目，每個人的寫法不同，看別人寫的能學到很多



## \[ Tailwind CSS \]

### 1\. How Tailwind Work :

- Scanning all of your HTML files, JavaScript components, and any other templates for class names

   - Scanning process is typically done during the **build process** using tools like **PurgeCSS**

   - **PurgeCSS** in Tailwind CSS project : 

      - eliminate unused CSS styles from your final production build 

      - analyzes codebase and removes any styles that are not applied in your HTML or JavaScript

      - resulting in a smaller and more optimized stylesheet for better performance

- zero-runtime

   - Generating styles and writing them to a static CSS file

   - All styles are compiled beforehand at build time

   - Not rely on JavaScript during page rendering or interaction to dynamically generate or manipulate styles

   - Makes it **fast and efficient** because the browser doesn't need to run any CSS-in-JS code or perform extra work to apply styles



### 2\. How to Use

- **[Tailwind CLI](https://tailwindcss.com/docs/installation) : **The simplest and fastest way

- **[Using PostCSS](https://tailwindcss.com/docs/installation/using-postcss) : i**nstalling Tailwind CSS as a PostCSS plugin is the most seamless way to integrate it with build tools like webpack, Rollup, Vite, and Parcel 

   - **PostCSS** is a powerful tool for transforming CSS with JavaScript-based plugins.









## \[ Bootstrap \]

### What is Bootstrap

- Purpose: 開發響應式、移動優先的 Web

- Front-End Framework : A widely-used, open-source front-end framework that simplifies and accelerates the development of responsive websites and web applications.

- Pre-Designed Components : offers a comprehensive collection of pre-designed HTML, CSS, and JavaScript components

- Responsive Grid Dystem : making it easier to create visually appealing and user-friendly web pages that adapt seamlessly to different screen sizes and devices

- Basic Concept:

   - **Responsive Design**: 

      - mobile-first approach: it is designed to create websites that look good on all devices, from smartphones to large desktop monitors. 

      - The framework includes a responsive grid system that allows for flexible layouts.  It divides the screen into 12 columns, and components can be placed within these columns to create adaptable layouts

   - **Pre-designed Components**: Bootstrap comes with a variety of pre-styled components, such as navigation bars, buttons, forms, modals, and carousels. These components can be easily integrated into web projects, saving developers time and effort. 

   - **Customization**: While Bootstrap provides a robust set of default styles, it also allows for customization through its Sass variables and mixins. This flexibility enables developers to tailor the framework to meet specific design needs.

      



### 1\. Bootstrap - Basic Grid

- Bootstrap's grid system allows up to 12 columns across the page.

- The Bootstrap grid system has several screen size classes:

   - 

      ![image 57.png](./CSS%20-assets/image%2057.png)

      

      

### 1\. Basic Rule:

- **Containers** 

   - are the most basic layout element in Bootstrap and are required when using the grid system. 

   - Basically used to wrap content with some padding. 

   - also used to align the content horizontally center on the page in case of fixed width layout.

   - `.container`, which has a max-width at each responsive breakpoint.

   - `.container-fluid`, which has 100% width at all breakpoints.

   - `.container-{breakpoint}`, which has 100% width until the specified breakpoint.

- **Rows** : 

   - must be placed within a `.container` (fixed-width) or `.container-fluid` (full-width) for proper alignment and padding

   - Use rows to create horizontal groups of columns

- **columns**: 

   - Content should be placed within columns

   - only columns may be immediate children of rows

   - **Gap** :Columns create gutters (gaps between column content) via padding. That padding is offset in rows for the first and last column via negative margin on `.rows`

   - Column widths are in percentage, so they are always fluid and sized relative to their parent element





## \[ Advanced CSS \]

### Customization by Sass

- **Sass (Syntactically Awesome Style Sheets)** is a CSS preprocessor that introduces powerful features to enhance the efficiency and maintainability of CSS code

- What Preprocessor Mean:

   - you cannot directly write Sass code in a normal CSS file. 

   - Sass is a preprocessor, which means it needs to be compiled or converted into standard CSS before a web browser can understand and apply the styles.

- How to use :

   - **Write your Sass code** in files with the `.scss` extension.

   - **Use a Sass compiler** (like Dart Sass, node-sass, or others) to compile your `.scss` files into `.css` files.

      - npm install sass --save-dev

      - npx sass input.scss output.css

      - "scripts": {

           "build:css": "sass src/styles.scss dist/styles.css"

         }

- Two key concepts in Sass are variables and mixins

   - **Variables**

      - Purpose: Variables allow you to store reusable values (colors, font sizes, spacing units, etc.) that can be referenced throughout your stylesheet.   

      - Syntax: Variables are declared using the $ symbol followed by the variable name and its value.  `$primary-color: #007bff;`

   - **Mixins**

      - Purpose: Mixins are reusable code blocks that group CSS declarations, acting like functions for your styles.   

      - Syntax:

         - Declaration: `@mixin mixin-name($argument1, $argument2...) { ... }`

         - Usage: `@include mixin-name(value1, value2...);`