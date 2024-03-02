import json
import datetime
from datetime import datetime
from dataclasses import dataclass
from playwright.sync_api import sync_playwright


@dataclass
class FbEvent:
    title: str
    description: str
    organiser: str
    street_address: str
    post_address: str
    country: str
    start_time: datetime
    stop_time: datetime


class Bjud:

    def __init__(self):
        pass

    def get_event(self, url):

        # Default values
        title = ""
        description = ""
        organiser = ""
        street_address = ""
        post_address = ""
        country = ""
        start_time = None
        stop_time = None

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

            title = page.locator(
                "//head/meta[contains(@property, 'og:title')]"
            ).get_attribute("content")

            if title == None:
                raise ValueError("No title")

            for l in page.locator("//body/script").all():
                try:
                    d = json.loads(l.text_content())
                    data = d["require"][0][3][0]["__bbox"]["require"][1][3][1][
                        "__bbox"
                    ]["result"]["data"]
                    start_time = data["start_timestamp"]
                    stop_time = data["end_timestamp"]
                except Exception as e:
                    pass

            for l in page.locator("//body/script").all():
                try:
                    d = json.loads(l.text_content())
                    candidates = d["require"][0][3][0]["__bbox"]["require"]
                    for c in candidates:
                        try:
                            event = c[3][1]["__bbox"]["result"]["data"]["event"]
                            description = event["event_description"]["text"]
                            address = event["one_line_address"]
                            if address:
                                street_address = address.split(",")[0]
                                post_address = address.split(",")[1]
                                country = address.split(",")[2]
                            organiser = event["event_creator"]["name"]
                            return FbEvent(
                                title=title,
                                description=description,
                                organiser=organiser,
                                street_address=street_address,
                                post_address=post_address.strip(),
                                country=country.strip(),
                                start_time=datetime.fromtimestamp(start_time),
                                stop_time=datetime.fromtimestamp(stop_time),
                            )
                        except Exception as e:
                            pass
                except Exception as e:
                    pass
            raise ValueError("Loop failed")
