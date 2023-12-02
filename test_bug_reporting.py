# test_bug_reporting.py
import pytest
from pages.login_page import LoginPage
from pages.bug_report_page import BugReportPage
from utils.config import BUGZILLA_URL, SCREENSHOTS_PATH

@pytest.mark.usefixtures("driver")
class TestBugReporting:
    def test_report_bug(self, driver):
        driver.get(BUGZILLA_URL)
        login_page = LoginPage(driver)
        bug_report_page = BugReportPage(driver)

        login_page.login(username="<Your_Username>", password="<Your_Password>")
        # Navigate to the bug reporting page or perform other actions if needed
        bug_report_page.report_bug(
            product="RAID",
            component="Controller Card",
            version="1.3x",
            severity="Normal",
            hardware="Dell Server",
            os="Windows",
            category="Build",
            description="Unable to expand virtual volume"
        )
        screenshot_filename = SCREENSHOTS_PATH + "bug_report.png"
        bug_report_page.take_screenshot(screenshot_filename)
        # Additional assertions or validations if needed
