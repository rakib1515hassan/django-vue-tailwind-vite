<template>
    <div class="dashboard-container">
        <!-- Sidebar -->
        <aside class="sidebar">
            <h2 class="logo">VueAdmin</h2>
            <nav class="nav">
                <ul>
                    <li><a href="#">Dashboard</a></li>
                    <li><a href="#">Users</a></li>
                    <li><a href="#">Reports</a></li>
                    <li><a href="#">Settings</a></li>
                </ul>
            </nav>
        </aside>

        <!-- Main Content -->
        <div class="main-content">
            <header class="header">
                <h1 class="text-3xl font-bold underline bg-red-500">
                    Hello world!
                </h1>

                <h1 class="bg-blue-500 text-white p-4 rounded-lg text-center">Item 1</h1>

                <h1>Welcome to Vue Dashboard 🚀</h1>
                <p class="text-2xl font-sans text-center text-red-200">Test Tailwend CSS</p>
                <p class="raw_css">Test RAW CSS</p>
                <p>Hello, {{ user.name }} — Age: {{ user.age }}</p>
            </header>

            <section class="cards">
                <div class="card" v-for="stat in stats" :key="stat.label">
                    <h3>{{ stat.label }}</h3>
                    <p>{{ stat.value }}</p>
                </div>
            </section>

            <footer class="footer">
                <p>© 2025 {{ user.name }} — {{ user.city }}</p>
            </footer>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DashboardComponent',
    data() {
        return {
            user: {
                name: 'Md Rakib Hassan',
                age: 29,
                city: 'Dhaka'
            },
            stats: [
                { label: 'Total Users', value: 0 },
                { label: 'Sales Today', value: '$0' },
                { label: 'New Signups', value: 0 }
            ]
        };
    },
    mounted() {
        console.log("Dashboard mounted!");
        // Simulate async data fetch
        setTimeout(() => {
            this.stats = [
                { label: 'Total Users', value: 1245 },
                { label: 'Sales Today', value: '$1,350' },
                { label: 'New Signups', value: 38 }
            ];
        }, 1000);
    },
    watch: {
        'user.age'(newAge, oldAge) {
            console.log(`Age changed from ${oldAge} to ${newAge}`);
        }
    },
    methods: {
        updateAge(newAge) {
            this.user.age = newAge;
        }
    }
};
</script>

<style scoped></style>
