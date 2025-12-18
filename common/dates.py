from datetime import datetime, timedelta


def tomorrow_str(format="%d-%m-%Y"):
    """
    Devuelve la fecha de mañana como string
    """
    return (datetime.now() + timedelta(days=1)).strftime(format)


def first_day_of_current_month(format="%d-%m-%Y"):
    """
    Devuelve el día 1 del mes en curso
    """
    now = datetime.now()
    first_day = now.replace(day=1)
    return first_day.strftime(format)


def today_str(format="%d-%m-%Y"):
    """
    Devuelve la fecha de hoy
    """
    return datetime.now().strftime(format)