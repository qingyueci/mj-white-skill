const { chromium } = require('playwright');
const path = require('node:path');
const { pathToFileURL } = require('node:url');

async function main() {
  const dir = __dirname;
  const launchOptions = { headless: true, args: ['--disable-gpu', '--no-sandbox'] };
  if (process.env.CHROME_PATH) launchOptions.executablePath = process.env.CHROME_PATH;
  const browser = await chromium.launch(launchOptions);
  try {
    const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
    await page.goto(pathToFileURL(path.join(dir, 'posters.html')).href);
    await page.evaluate(() => document.fonts.ready);
    for (let i = 1; i <= 6; i++) {
      await page.locator(`#p${i}`).screenshot({ path: path.join(dir, `${String(i).padStart(2, '0')}.png`) });
      console.log('POSTER', i);
    }
  } finally {
    await browser.close();
  }
}

main().catch((error) => { console.error(error); process.exit(1); });