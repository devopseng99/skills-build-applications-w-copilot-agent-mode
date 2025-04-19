import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  define: {
    'process.env': {},
  },
  server: {
    port: 3000,
  },
  envPrefix: 'VITE_', // Ensure environment variables with 'VITE_' prefix are loaded
});
