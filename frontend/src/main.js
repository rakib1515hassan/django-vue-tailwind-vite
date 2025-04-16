import { createApp } from 'vue'
import './style.css'


const app = createApp({});

import { DashboardComponent } from "../../apps/auth/assets/js/app.js";
app.component("admin-dashboard", DashboardComponent);

app.mount("#app");