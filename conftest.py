from pages.adminpage import AdminPage
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    # Register a command line option
    parser.addoption("--browser",
                     action="store",
                     default="firefox",
                     help="web driver type")
    parser.addoption("--executor", action="store", default="192.168.1.44")
    parser.addoption("--bversion", action="store", default="84.0")

@pytest.fixture(scope="module")
def browser(request):
    # setup
    name = request.config.getoption("--browser")
    version = request.config.getoption("--bversion")
    executor = request.config.getoption('--executor')
    executor_url = f"http://{executor}:4444/wd/hub"

    capabilities = {
        "browserName": name,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=capabilities)

    yield driver
    # teardown
    driver.quit()


@pytest.fixture()
def admin_page(browser):
    page = AdminPage(browser)
    page.go_to("https://demo.opencart.com/admin/")
    return page
