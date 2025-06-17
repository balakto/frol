import { defineConfig } from 'vite';

export default defineConfig({
  root: 'фрол/templates',           // корневая папка с main.html
  build: {
    rollupOptions: {
      input: 'фрол/templates/main.html',  // входной html
    }
  }
});
