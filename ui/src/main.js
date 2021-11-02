import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import urql from '@urql/vue'


const app = createApp(App).use(router);

app.use(urql, {
    url: 'http://localhost:3000/graphql',
});


app.mount('#app');
