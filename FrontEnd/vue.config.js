const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  
  publicPath: '/',
  
  productionSourceMap: false,
  
  devServer: {
    port: 8080,
    historyApiFallback: true,
    proxy: {
      '/api': {
        target: process.env.VUE_APP_API_BASE_URL || 'http://127.0.0.1:8000',
        changeOrigin: true
      }
    }
  }
})