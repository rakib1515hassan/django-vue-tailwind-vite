/** @type {import('tailwindcss').Config} */
// frontend/tailwind.config.js


module.exports = {
  content: [
    "../../**/*.{html,js,vue}", // এটি পুরো Django-Vue project জুড়ে খুঁজবে
    "./index.html",
    "./src/**/*.{js,ts,vue}",
    "../templates/**/*.html",
  ],

  theme: {
    extend: {},
  },

  plugins: [],

  safelist: [
    "text-red-500",
    "bg-green-200",
    "hidden",
    "block", // Dynamic class গুলা যেগুলা template থেকে detect হয় না
  ],
};
