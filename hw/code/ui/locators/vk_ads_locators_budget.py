from selenium.webdriver.common.by import By

class BudgetPageLocators:
    RECHARGE_BUTTON = (By.XPATH, '//button[.//span[text()="Пополнить счёт"]]')
    AMOUNT_INPUT = (By.CSS_SELECTOR, 'input[name="amount"]')  # Первый инпут
    AMOUNT_WITHOUT_VAT_INPUT = (By.CSS_SELECTOR, 'input[name="amountWithoutVat"]')  # Второй инпут
    BUDGET_LINK = (By.CSS_SELECTOR, '[data-entityid="budget"]')  # Ссылка на страницу бюджета

