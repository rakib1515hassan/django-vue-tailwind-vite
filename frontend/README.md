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
│   ├── style.css
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



## npm Cache clean:
```bash
npm cache clean --force
```




# Tailwind CSS Install 

## 1. Install Tailwind CSS 

#### Using Vite
```base
npm install tailwindcss @tailwindcss/vite
```

## 2. Configure the Vite plugin

```base
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

import path from "path";

import { fileURLToPath, URL } from "node:url";


// https://vite.dev/config/
export default defineConfig({
  // base: "/static/vue/", // এটা দিলে vue http://localhost:5173/static/vue/ এই ভাবে run হবে।

  plugins: [vue()],

  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
      vue: "vue/dist/vue.esm-bundler.js",
    },
  },

  css: {
    postcss: "./postcss.config.js",
  },

  build: {
    outDir: path.resolve(__dirname, "../static/vue"), // <-- output in Django static
    emptyOutDir: true,
    cssCodeSplit: false,
    assetsDir: "assets",
    manifest: true,
    rollupOptions: {
      input: path.resolve(__dirname, "src/main.js"),
      output: {
        entryFileNames: "assets/main.js",
        chunkFileNames: "assets/[name].js",
        assetFileNames: (assetInfo) => {
          if (assetInfo.name && assetInfo.name.endsWith(".css")) {
            return "assets/style.css";
          }
          return "assets/[name][extname]";
        },
      },
    },
  },
});
```




## 3. Import Tailwind CSS

```base
@import "tailwindcss" source(none);

@source "../src/**/*.vue";
@source "../src/**/*.js";

@source "../../templates/**/*.html";
@source "../../**/templates/**/*.html";
@source "../../**/*.vue";
```




# Note: Tailwind Sugenst in VS Code Editor

#### VS Code এর settings.json ফাইলের files.associations এর "*html": "html", নিচের কনফিগারেশন যুক্ত করুন:

```base
"files.associations": {
  "*html": "html",
  "*.css": "tailwindcss"
},
```

#### VS Code এর settings.json ফাইলে নিচের কনফিগারেশন যুক্ত করুন:
```base
"tailwindCSS.includeLanguages": {
  "vue": "html"
},
"editor.quickSuggestions": {
  "strings": true
},
"editor.inlineSuggest.enabled": true
```