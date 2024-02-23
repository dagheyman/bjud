import json
from dataclasses import dataclass
from playwright.sync_api import sync_playwright


@dataclass
class FbEvent:
    title: str
    description: str
    organiser: str
    address: str


class Bjud:

    def __init__(self):
        pass

    def get_event(self, url):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(locale="en-US")
            page.goto(url)

            try:
                page.get_by_role("button", name="Allow all cookies").click(timeout=100)
            except Exception as e:
                pass

            try:
                page.get_by_label("Close").click(timeout=100)
            except Exception as e:
                pass

            try:
                page.get_by_role("button", name="See more").first.click(timeout=100)
            except Exception as e:
                pass

            for l in page.locator("//body/script").all():
                try:
                    d = json.loads(l.text_content())
                    event = d["require"][0][3][0]["__bbox"]["require"][7][3][1][
                        "__bbox"
                    ]["result"]["data"]["event"]
                    description = event["event_description"]["text"]
                    location = event["location"]["reverse_geocode"]["city_page"]["name"]
                    address = event["one_line_address"]
                    organiser = event["event_creator"]["name"]
                    return FbEvent(
                        title="TODO",
                        description=description,
                        organiser=organiser,
                        address=address,
                    )
                except Exception as e:
                    pass
            browser.close()
