import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def choose_material(payment):
    """Функция для выбора продукта для оплаты"""

    if payment.paid_lesson:
        return payment.paid_lesson
    elif payment.paid_course:
        return payment.paid_course
    else:
        raise ValueError('Необходимо выбрать курс или урок для оплаты')


def create_stripe_product(material):
    return stripe.Product.create(name=f'Оплата за курс/урок "{material}"')


def create_stripe_price(amount, product):
    """Создает цену в страйпе"""
    return stripe.Price.create(
        currency='rub',
        unit_amount=amount * 100,
        product_data=product,
    )


def create_stripe_session(price):
    """Создает сессию на оплату в страйпе"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
