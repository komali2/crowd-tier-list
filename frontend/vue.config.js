module.exports = {
  devServer: {
    proxy: {
      // proxy all requests starting with /api to jsonplaceholder
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
}
