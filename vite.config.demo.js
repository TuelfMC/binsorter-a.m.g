import { mergeConfig } from 'vite'
import base from './vite.config.js'

const servidor = {
host: true,
allowedHosts: ['.trycloudflare.com'],
proxy: {
    '/api': {
    target: 'http://127.0.0.1:8000',
    changeOrigin: true,
    rewrite: (path) => path.replace(/^\/api/, ''),
    },
},
}

export default mergeConfig(base, { server: servidor, preview: servidor })