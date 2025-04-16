import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

import path from "path";

import { fileURLToPath, URL } from "node:url";

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
      vue: "vue/dist/vue.esm-bundler.js", 
    },
  },

  build: {
    outDir: path.resolve(__dirname, "../static/vue"),   // <-- output in Django static
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
