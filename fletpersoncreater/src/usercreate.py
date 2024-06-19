from mimesis import Person, Address, Internet, Code, Payment
from mimesis.enums import Gender
from mimesis.locales import Locale


class Character:
    def __init__(self, locale=Locale.RU):
        self.person = Person(locale)
        self.address = Address(locale)
        self.finance = Payment()
        self.internet = Internet()
        self.code = Code()

        self.gender = self.person.gender()
        self.first_name = self.person.first_name(gender=Gender.MALE if self.gender == 'male' else Gender.FEMALE)
        self.last_name = self.person.last_name()
        self.full_name = self.person.full_name()
        self.email = self.person.email()
        self.phone = self.person.telephone()
        self.birth_date = self.person.birthdate()

        self.country = self.address.country()
        self.city = self.address.city()
        self.address_line = self.address.address()
        self.zip_code = self.address.postal_code()

        self.credit_card_number = self.finance.credit_card_number()
        self.credit_card_expiry = self.finance.credit_card_expiration_date(minimum=25, maximum=30)
        self.cvc = self.finance.cvv()

        self.website = self.internet.url()
        self.ip_address = self.internet.ip_v4()
        self.job = self.person.occupation()
        self.passport = self.code

    def __str__(self):
        return (f"Имя и фамилия: {self.full_name}\n"
                f"Пол: {self.gender}\n"
                f"Дата рождения: {self.birth_date}\n"
                f"Почта: {self.email}\n"
                f"Телефон: {self.phone}\n"
                f"Адрес: {self.address_line}, {self.city}, {self.country}, {self.zip_code}\n"
                f"Работа: {self.job}\n"
                f"Сайт: {self.website}\n"
                f"IP: {self.ip_address}\n"
                f"Кредитная карта: {self.credit_card_number} (Expiry: {self.credit_card_expiry}, CVC: {self.cvc})\n")

