import json
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.facebook.com/events/1828636217581951/")
    #page.goto("https://www.facebook.com/events/317911824550706/")
    page.get_by_role("button", name="Allow all cookies").click()
    page.get_by_role("button", name="See more").first.click()
    for l in page.locator("//body/script").all():
        try:
            d = json.loads(l.text_content())
            event = d['require'][0][3][0]['__bbox']['require'][7][3][1]['__bbox']['result']['data']['event']
            description = event['event_description']['text']
            location = event['location']['reverse_geocode']['city_page']['name']
            address = event['one_line_address']
            organiser = event['event_creator']['name']
            print(description)
            print(location)
            print(address)
            print(organiser)

        except Exception as e:
            pass
    browser.close()

    
