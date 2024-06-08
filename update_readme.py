from playwright.sync_api import sync_playwright

def main(): 
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={'width': 1280, 'height': 764},
            device_scale_factor=2,
        )
        page = context.new_page()
        page.goto('https://github.com/LimMengShin')
        page.screenshot(path="screenshot.jpg", type="jpeg", quality=100)
        context.close()

if __name__ == "__main__":
    main()
