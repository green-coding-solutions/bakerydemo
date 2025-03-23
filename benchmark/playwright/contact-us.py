from playwright.sync_api import sync_playwright
import os

from gmt_helpers import log_note

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(ignore_https_errors=True, viewport={"width": 1280, "height": 1600})
    page = context.new_page()
    page.set_default_timeout(5000)

    page.goto(os.environ['USAGE_SCENARIO_DOMAIN'] + "/contact-us/", wait_until="networkidle")
    log_note(page.title())
    print("GMT_SCI_R=1")

    page.wait_for_timeout(3000)
    page.locator('footer').scroll_into_view_if_needed()
    page.wait_for_load_state("networkidle")

    page.fill('#id_subject', 'Enquiring about bread')
    page.fill('#id_your_name', 'Testing tester')
    page.select_option('#id_purpose', 'Question')
    page.fill('#id_body', 'Is this is for demo purposes only?')

    with page.expect_navigation(wait_until='networkidle'):
        page.locator('[type="submit"]').press('Enter')
    print("GMT_SCI_R=1")

    page.wait_for_timeout(3000)
    page.locator('footer').scroll_into_view_if_needed()
    page.wait_for_load_state("networkidle")

    log_note(page.title())
    intro_text = page.locator('.index-header__body-introduction').inner_text().replace("\n", "--")
    log_note(intro_text)

    page.wait_for_timeout(3000)
    page.locator('footer').scroll_into_view_if_needed()
    page.wait_for_load_state("networkidle")

    browser.close()
