from celery import shared_task


@shared_task
def updating_mail():
    print('Hello, World!')
