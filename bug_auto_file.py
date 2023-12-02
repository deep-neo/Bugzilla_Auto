from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def file_bug(bugzilla_url, username, password, product, component, version, severity, hardware, os, category, summary, description):
    # Initialize the web driver (Make sure to replace 'path/to/chromedriver' with the path to your ChromeDriver executable)
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')

    try:
        # Navigate to the Bugzilla login page
        driver.get(f"{bugzilla_url}/enter_bug.cgi")

        # Log in to Bugzilla
        driver.find_element(By.ID, "Bugzilla_login").send_keys(username)
        driver.find_element(By.ID, "Bugzilla_password").send_keys(password)
        driver.find_element(By.ID, "log_in").click()

        # Fill out the bug report form
        driver.find_element(By.ID, "product").send_keys(product)
        driver.find_element(By.ID, "component").send_keys(component)
        driver.find_element(By.ID, "version").send_keys(version)
        driver.find_element(By.ID, "bug_severity").send_keys(severity)
        driver.find_element(By.ID, "rep_platform").send_keys(hardware)
        driver.find_element(By.ID, "op_sys").send_keys(os)
        driver.find_element(By.ID, "cf_category").send_keys(category)
        driver.find_element(By.ID, "short_desc").send_keys(summary)
        driver.find_element(By.ID, "comment").send_keys(description)

        # Submit the bug
        driver.find_element(By.ID, "commit").click()

        # Wait for the bug ID to be displayed after submission
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Bug')]")))

        # Get the bug ID from the confirmation page
        bug_id = driver.find_element(By.XPATH, "//*[contains(text(), 'Bug')]").text.split()[-1]
        print(f"Bug filed successfully. Bug ID: {bug_id}")

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    # Bugzilla configuration
    bugzilla_url = "<Bugzilla_URL>"
    username = "<Your_Username>"
    password = "<Your_Password>"

    # Bug details
    product = "<Product>"
    component = "<Component>"
    version = "<Version>"
    severity = "<Severity>"
    hardware = "<Hardware>"
    os = "<Operating_System>"
    category = "<Category>"
    summary = "<Summary>"
    description = "<Description>"

    # File a bug using Selenium
    file_bug(bugzilla_url, username, password, product, component, version, severity, hardware, os, category, summary, description)
