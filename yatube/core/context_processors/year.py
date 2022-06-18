from datetime import datetime


def year(request):
    """Добавляет переменную с текущим годом."""
    cur_year = int(datetime.now().strftime("%Y"))
    return {
        'year': cur_year
    }
