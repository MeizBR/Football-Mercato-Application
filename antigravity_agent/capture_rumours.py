
from pathlib import Path
from playwright.sync_api import sync_playwright

current_dir = Path.home() / "Desktop" / "Football-Mercato-Application"

html_file = current_dir / "rumours_data.html"
image_file = current_dir / "rumours_data.png"

if not html_file.exists():
    raise FileNotFoundError(f"HTML report not found: {html_file}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(
        viewport={"width": 1200, "height": 900},
        device_scale_factor=1,
    )

    page.goto(html_file.resolve().as_uri(), wait_until="load")
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(1000)

    page.screenshot(
        path=str(image_file),
        full_page=True,
    )

    browser.close()

print(f"Screenshot saved to: {image_file}")