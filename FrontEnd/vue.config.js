const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  
  // Configuración para producción
  publicPath: process.env.NODE_ENV === 'production' ? '/' : '/',
  
  // Optimizaciones para producción
  productionSourceMap: false,
  
  // Configuración del servidor de desarrollo
  devServer: {
    port: 8080,
    proxy: {
      '/api': {
        target: process.env.VUE_APP_API_BASE_URL || 'http://127.0.0.1:8000',
        changeOrigin: true
      }
    }
  }
})