from playwright.sync_api import Page, expect, Route
import json


def test_phone(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 16 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route('**/step0_iphone/**', handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator("//button[@data-index='1']").click()
    expect(page.locator('.rf-digitalmat-overlay-header.typography-manifesto#rf-digitalmat-overlay-label-0'
                        '[data-autom="DigitalMat-overlay-header-0-0"]')).to_have_text('яблокофон 16 про')
