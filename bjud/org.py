import json
from dataclasses import dataclass
from playwright.sync_api import sync_playwright

@dataclass

class Org:
	def __init__(self):
		pass

	def get_events(self, url):
		events = list()
	
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
			
			for l in page.locator("//body/script").all():
				try:
					d = json.loads(l.text_content())
					data = d["require"][0][3][0]["__bbox"]["require"][5][3][1][
						"__bbox"
					]["result"]["data"]["node"]["all_collections"]["nodes"][0]["style_renderer"]["collection"]["pageItems"]["edges"]
					for n in data:
						events.append(n["node"]["node"]["url"])
				except Exception as e:
					pass
				
			return events
			
		raise ValueError("Loop failed")