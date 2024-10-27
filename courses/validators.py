from rest_framework.serializers import ValidationError


class LessonsVideoValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """Проверяем введенную ссылку на соответсвие с ссылками в списке разрешенных ресурсов"""
        url = "http://youtube.com"
        if value.get("url_video"):
            if url not in value.get("url_video"):
                raise ValidationError("Необходимо присутствие ссылки на youtube.")
        return None
