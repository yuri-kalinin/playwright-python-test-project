import pytest
import yaml
from pathlib import Path
from playwright.sync_api import sync_playwright

def get_config():
    path = Path(__file__).parent / "../config.yaml"
    with open(path) as config_file:
        data = yaml.load(config_file, Loader=yaml.FullLoader)
    return data

class TestBase:

    @pytest.fixture(scope="session", autouse=True)
    def init_test(self):
        config = get_config()
        p = sync_playwright().start()
        browser_type = p[config['browser']]
        browser = browser_type.launch(timeout=10_000, headless=False, args=[f"--base-url {config['url']}"])
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        context.set_default_timeout(10_000)
        page = context.new_page()

        self.config = config
        self.url = config['url']
        self.page = page

        yield self

        if browser is not None:
            browser.close()
