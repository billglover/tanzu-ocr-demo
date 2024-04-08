/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './ocr/templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms')({
      strategy: 'base',
    }),
    require('@tailwindcss/typography'),
  ],
}

