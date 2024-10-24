from rest_framework.serializers import ValidationError


class LessonsVideoValidator:

    def __init__(self, field):
        allowed_links = [
            "https://www.youtube.com/",
            "https://youtube.com/",
        ]
        self.field = field
        self.allowed_links = allowed_links

    def call(self, value):
        """Проверяем введенную ссылку на соответсвие с ссылками в списке разрешенных ресурсов"""
        if any(link in value for link in self.allowed_links):
            return True
        else:
            raise ValidationError(
                f"Допустимо использовать только ссылки на следующие ресурсы: {*allowed_links,}"
            )
