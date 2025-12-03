const { defineConfig } = require('@vue/cli-service')
const CopyWebpackPlugin = require('copy-webpack-plugin')

module.exports = defineConfig({
  transpileDependencies: true,
  
  // Configuración para producción
  publicPath: process.env.NODE_ENV === 'production' ? '/' : '/',
  
  // Optimizaciones para producción
  productionSourceMap: false,
  
  // Configuración del servidor de desarrollo
  devServer: {
    port: 8080,
    historyApiFallback: true, // ← IMPORTANTE: Agrega esto
    proxy: {
      '/api': {
        target: process.env.VUE_APP_API_BASE_URL || 'http://127.0.0.1:8000',
        changeOrigin: true
      }
    }
  },

  // Asegurar que _redirects se copie al build
  configureWebpack: {
    plugins: [
      new CopyWebpackPlugin({
        patterns: [
          {
            from: 'public/_redirects',
            to: '_redirects',
            toType: 'file',
            noErrorOnMissing: true
          }
        ]
      })
    ]
  }
})