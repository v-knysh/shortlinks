import datetime

from api.models import Link
from api.views import random_string

for i in range(10):
    l = Link(
        short_url=random_string(),
        redirect_location=f"http://127.0.0.1:8000/{i}",
        expiration_date=datetime.datetime.now(),
        created=datetime.datetime.now(),
        author_ip=f"127.0.0.{int(i / 2)}",
        is_active=True,
    )
    l.save()
