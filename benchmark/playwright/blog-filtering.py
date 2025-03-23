from playwright.sync_api import sync_playwright
import os

from gmt_helpers import log_note

def main():
    domain = os.environ.get("USAGE_SCENARIO_DOMAIN")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(ignore_https_errors=True, viewport={"width": 1280, "height": 1600})
        page = context.new_page()
        page.set_default_timeout(5000)

        page.goto(f"{domain}/blog/", wait_until="networkidle")
        log_note(page.title())
        print("GMT_SCI_R=1")

        page.wait_for_timeout(3000)
        page.locator("footer").scroll_into_view_if_needed()
        page.wait_for_load_state("networkidle")

        page.click('[href="/blog/tags/dessert/"]')
        page.wait_for_load_state("networkidle")
        log_note(page.title())
        print("GMT_SCI_R=1")

        page.wait_for_timeout(3000)
        page.locator("footer").scroll_into_view_if_needed()
        page.wait_for_load_state("networkidle")

        page.click('[href="/blog/desserts-benefits/"]')
        page.wait_for_load_state("networkidle")
        log_note(page.title())
        print("GMT_SCI_R=1")

        page.wait_for_timeout(3000)
        page.locator("footer").scroll_into_view_if_needed()
        page.wait_for_load_state("networkidle")

        browser.close()

if __name__ == "__main__":
    main()
