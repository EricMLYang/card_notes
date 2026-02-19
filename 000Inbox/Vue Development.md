---
tags:
  - frontend
---
# Vue Development

- <https://vuejs.org/guide/introduction.html?ref=madewithvuejs.com>



## other resource

- daisyUI

- tailwind CSS



## **Applications and Components**

In Vue.js, the application is made up of **components**. Components are the building blocks of a Vue app. You can think of each component as a small, self-contained piece of the user interface (UI) that has its own data, logic, and layout.

- An application instance won't render anything until its `.mount()` method is called

- `Refs`

   ```python
   <script setup>
   import { ref } from 'vue'
   
   const count = ref(0)
   
   function increment() {
     count.value++
   }
   </script>
   
   <template>
     <button @click="increment">
       {{ count }}
     </button>
   </template>
   
   ```

   - When you use a ref in a template, and change the ref's value later, Vue automatically detects the change and updates the DOM accordingly.

   - This is made possible with a dependency-tracking based reactivity system.

   - **Deep Reactivity : **Refs can hold any value type, including deeply nested objects, arrays, or JavaScript built-in data structures like `Map`.

   - When you mutate reactive state, the DOM is updated automatically. However, it should be noted that the DOM updates are not applied synchronously. Instead, Vue buffers them until the "next tick" in the update cycle to ensure that each component updates only once no matter how many state changes you have made.

- **`reactive()`**

   ```python
   import { reactive } from 'vue'
   const state = reactive({ count: 0 })
   
   <button @click="state.count++">
     {{ state.count }}
   </button>
   ```



- `computed`

```python
<script setup>
import { reactive, computed } from 'vue'

const author = reactive({
  name: 'John Doe',
  books: [
    'Vue 2 - Advanced Guide',
    'Vue 3 - Basic Guide',
    'Vue 4 - The Mystery'
  ]
})

// a computed ref
const publishedBooksMessage = computed(() => {
  return author.books.length > 0 ? 'Yes' : 'No'
})
</script>

<template>
  <p>Has published books:</p>
  <span>{{ publishedBooksMessage }}</span>
</template>
```





## Template

- Think of the template as a JavaScript function declared in the same scope - it naturally has access to everything declared alongside it.

### **Computed Properties**

- In-template expressions are very convenient, but they are meant for simple operations. Putting too much logic in your templates can make them bloated and hard to maintain. For example, if we have an object with a nested array: