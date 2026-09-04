// Render /cv/ of a built site to a PDF with headless Chrome, using the page's
// print stylesheet (see the `@media print` block in _sass/layout/_skin.scss).
//
//   BASE_URL=http://localhost:4000 OUT=files/yu-han-wu-cv.pdf node .github/scripts/cv-pdf.js
//
// In CI `puppeteer` (which brings its own Chrome) is installed; locally the
// script falls back to `puppeteer-core` plus CHROME_PATH.
const path = require('path');

async function launch() {
  try {
    const puppeteer = require('puppeteer');
    return puppeteer.launch({ headless: true, args: ['--no-sandbox', '--disable-gpu'] });
  } catch (e) {
    const puppeteer = require('puppeteer-core');
    const executablePath = process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
    return puppeteer.launch({ executablePath, headless: true, args: ['--no-first-run', '--disable-gpu'] });
  }
}

(async () => {
  const base = process.env.BASE_URL || 'http://localhost:4000';
  const out = path.resolve(process.env.OUT || 'files/yu-han-wu-cv.pdf');
  const browser = await launch();
  const page = await browser.newPage();
  // everything the page needs is served by the site itself; block the rest
  await page.setRequestInterception(true);
  page.on('request', (r) => (r.url().startsWith(base) ? r.continue() : r.abort()));
  // paper is light: ask for the light scheme before load, then pin the theme
  // attribute the site's own script sets, and switch to the print stylesheet
  await page.emulateMediaFeatures([{ name: 'prefers-color-scheme', value: 'light' }]);
  await page.goto(base + '/cv/', { waitUntil: 'networkidle0' });
  await page.evaluate(() => {
    document.documentElement.setAttribute('data-theme', 'light');
    document.documentElement.style.colorScheme = 'light';
  });
  await page.emulateMediaType('print');
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: out,
    format: 'A4',
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: false,
  });
  await browser.close();
  console.log('wrote', out);
})().catch((e) => { console.error(e); process.exit(1); });
