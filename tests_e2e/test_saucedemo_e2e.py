from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

PRODUCTS = {
    "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
    "Sauce Labs Bike Light": "add-to-cart-sauce-labs-bike-light",
}


def item_names(wait):
    items = wait.until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
    )
    return sorted(item.text for item in items)


def test_purchase_flow(driver):
    wait = WebDriverWait(driver, 10)

    driver.get(BASE_URL)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory.html"))

    for button_id in PRODUCTS.values():
        wait.until(EC.element_to_be_clickable((By.ID, button_id))).click()

    wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "2")
    )

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("cart.html"))
    assert item_names(wait) == sorted(PRODUCTS)

    driver.find_element(By.ID, "checkout").click()
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Byron")
    driver.find_element(By.ID, "last-name").send_keys("Carvajal")
    driver.find_element(By.ID, "postal-code").send_keys("170150")
    driver.find_element(By.ID, "continue").click()

    wait.until(EC.url_contains("checkout-step-two.html"))
    assert item_names(wait) == sorted(PRODUCTS)

    driver.find_element(By.ID, "finish").click()
    header = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert "THANK YOU FOR YOUR ORDER" in header.text.upper()
