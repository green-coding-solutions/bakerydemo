from playwright.sync_api import sync_playwright
import os

from gmt_helpers import log_note

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(ignore_https_errors=True, viewport={"width": 1280, "height": 1600})
    page = context.new_page()

    page.set_default_timeout(5000)

    page.goto(f"{os.environ['USAGE_SCENARIO_DOMAIN']}/admin/login/", wait_until="networkidle")
    log_note(page.title())
    print("GMT_SCI_R=1")

    page.fill('#id_username', 'admin')
    page.fill('#id_password', 'changeme')

    page.press('[type="submit"]', 'Enter')

    page.wait_for_load_state('networkidle')

    log_note(page.title())
    print("GMT_SCI_R=1")

    page.click('[href="/admin/pages/60/"]')
    page.wait_for_load_state('networkidle')
    log_note(page.title())

    page.click('[href="/admin/pages/61/"]')
    page.wait_for_load_state('networkidle')
    log_note(page.title())
    print("GMT_SCI_R=1")

    page.click('[href="/admin/pages/77/edit/"]')
    page.wait_for_load_state('load', timeout=15000)
    log_note(page.title())

    page.fill('#id_title', '(new) ')

    preview_toggle = page.wait_for_selector('[aria-label="Toggle preview"]', timeout=10000)
    preview_toggle.click()

    page.wait_for_selector('iframe[title="Preview"]', state='visible')

    # Optional screenshot:
    # page.screenshot(path="admin.png")

    browser.close()
