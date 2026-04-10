import { createApp } from './vue.esm-browser.prod.js'
import db from '../fonts/db.js'

createApp({
    data() {
        return {
            fontSizes: db,
            fontSize: 8,
            input: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n0123456789 !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~￥\n\n我们度过的每个平凡的日常，也许就是连续发生的奇迹。',
        }
    },
    computed: {
        fontStyle() {
            return {
                fontFamily: `xiaodianzhen-${this.fontSize}px`,
                fontSize: `${this.fontSize * 2}px`,
            }
        },
    },
}).mount('#app')
