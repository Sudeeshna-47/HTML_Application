from selenium import webdriver
from pathlib import Path

driver = webdriver.Chrome()

file_path = Path(__file__).with_name("index.html").resolve()
print("HTML file path:", file_path)
print("File exists:", file_path.exists())

driver.get(file_path.as_uri())
print("SELENIUM TEST")

print("Page title:", driver.title)
print("Page source:", driver.page_source)

input("Press Enter to close browser...")
driver.quit()