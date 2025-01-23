from playwright.sync_api import Page, expect, BrowserContext, Dialog


def test_alert(page: Page):
    def accept(alert: Dialog):
        print(alert.type)
        alert.accept('Ok')

    page.on('dialog', accept)
    page.goto('https://www.qa-practice.com/elements/alert/confirm#')
    click_button = page.locator("//*[@class='a-button']")
    click_button.click()
    result_text = page.locator("[id = 'result-text']")
    expect (result_text).to_have_text('Ok')


def test_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    click_button = page.locator('[id = "new-page-button"]')
    with context.expect_page() as new_page_event:
        click_button.click()
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    new_page.close()
    expect(click_button).to_be_enabled()

def test_color(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_change_button = page.get_by_text('Color Change')
    expect (color_change_button).to_have_css("color", "rgb(220, 53, 69)")
    color_change_button.click()
