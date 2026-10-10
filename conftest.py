import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # sin esto Chrome abre el aviso de contraseña filtrada al loguearse con secret_sauce
    options.add_experimental_option(
        "prefs", {"profile.password_manager_leak_detection": False}
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    yield driver
    driver.quit()
