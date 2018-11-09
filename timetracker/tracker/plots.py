import datetime
from .models import TimeBlock


class PieChart:

    def __init__(self, *args, **kwargs):
        self.today = datetime.date.today()
        self.past_week = [
            datetime.date.today() - datetime.timedelta(days=x) for x in range(7)
        ]
