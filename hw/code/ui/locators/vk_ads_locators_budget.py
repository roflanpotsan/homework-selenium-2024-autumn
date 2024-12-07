from selenium.webdriver.common.by import By

class BudgetPageLocators:
    RECHARGE_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="recharge"]')  # Локатор кнопки "Пополнить счет"
    AMOUNT_INPUT = (By.CSS_SELECTOR, 'input[name="amount"]')  # Первый инпут
    AMOUNT_WITHOUT_VAT_INPUT = (By.CSS_SELECTOR, 'input[name="amountWithoutVat"]')  # Второй инпут
    BUDGET_LINK = (By.CSS_SELECTOR, '[data-entityid="budget"]')  # Ссылка на страницу бюджета
