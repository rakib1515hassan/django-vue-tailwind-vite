# Vue 3 + Vite 

## Project create

```bash
npm create vite@latest frontend -- --template vue
```
### use TypeScript
```bash
npm create vite@latest my-vue-app -- --template vue-ts
```

### Stracture 

```bash
frontend/
├── node_modules/
├── public/
├── src/
│   ├── assets/
│   ├── components/
│   ├── App.vue
│   └── main.js
├── index.html
├── package.json
├── vite.config.js
```


## vite.config.js

```bash
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()]
})
```



## main.js

```bash
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```



## index.html

```bash
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vite App</title>
</head>
<body>
  <div id="app"></div>
  <script type="module" src="/src/main.js"></script>
</body>
</html>
```



## To add Vue Router

```bash
npm install vue-router@4
```



## To add Pinia (state management):
```bash
npm install pinia
```