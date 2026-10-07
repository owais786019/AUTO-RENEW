import os
from camoufox import Camoufox

def run_scraper():
    print("Launching Camoufox in headless mode...")
    
    # headless=True is mandatory inside GitHub Actions environment
    # geoip=True activates the geoip extra package features
    with Camoufox(headless=True, geoip=True) as browser:
        page = browser.new_page()
        
        print("Navigating to target page...")
        page.goto("https://wikipedia.org")
        
        # Extract and print out data to prove it is functioning
        title = page.title()
        print(f"Successfully reached page! Title: {title}")
        
        # Optional: Save a screenshot to confirm it rendered perfectly fine headless
        page.screenshot(path="screenshot.png")
        print("Screenshot saved successfully as screenshot.png")

if __name__ == "__main__":
    run_scraper()
