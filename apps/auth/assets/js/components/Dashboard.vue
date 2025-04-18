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

            <h1 class="bg-red-500 text-6xl text-center">Md Rakib Hassan</h1>

            <!-- Tailwind CSS Class -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 p-4 bg-white rounded-lg shadow-lg">
                <div class="bg-blue-500 text-white p-4 rounded-lg text-center">Item 1</div>
                <div class="bg-green-500 text-white p-4 rounded-lg text-center">Item 2</div>
                <div class="bg-red-500 text-white p-4 rounded-lg text-center">Item 3</div>
                <div class="bg-yellow-500 text-white p-4 rounded-lg text-center">Item 4</div>
                <div class="bg-purple-500 text-white p-4 rounded-lg text-center">Item 5</div>
                <div class="bg-pink-500 text-white p-4 rounded-lg text-center">Item 6</div>
            </div>

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

<style scoped>
.dashboard-container {
    display: flex;
    min-height: 100vh;
    font-family: 'Segoe UI', sans-serif;
}

/* Sidebar */
.sidebar {
    background-color: #2c3e50;
    color: white;
    width: 220px;
    padding: 20px;
}

.logo {
    font-size: 24px;
    margin-bottom: 30px;
}

.nav ul {
    list-style: none;
    padding: 0;
}

.nav li {
    margin: 15px 0;
}

.nav a {
    color: white;
    text-decoration: none;
    font-weight: 500;
}

/* Main content */
.main-content {
    flex: 1;
    background-color: #f5f7fa;
    padding: 30px;
}

.header h1 {
    font-size: 28px;
    margin-bottom: 10px;
}

.header p {
    font-size: 18px;
    color: #444;
}

.cards {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    margin-top: 20px;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    flex: 1;
    min-width: 200px;
}

.card h3 {
    margin-bottom: 10px;
    color: #333;
}

.card p {
    font-size: 24px;
    color: #2c3e50;
    font-weight: bold;
}

.footer {
    margin-top: 40px;
    text-align: center;
    font-size: 14px;
    color: #888;
}
</style>