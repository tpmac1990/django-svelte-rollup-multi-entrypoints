const production = process.env.NODE_ENV === 'production';

module.exports = {
  plugins: [
    require("tailwindcss"),
    require("autoprefixer"),
    production && require("cssnano"),
    // Brotli // for compression
    // npm install --save-dev rollup-plugin-brotli
  ],
}
