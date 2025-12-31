from datetime import datetime, timedelta

def tomorrow_date():
    return datetime.now() + timedelta(days=1)


def tomorrow_str():
    return tomorrow_date().strftime("%d-%m-%Y")

def tomorrow_str2(format="%d-%m-%Y"):
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


def first_day_of_month_from_date(date_obj: datetime) -> str:
    """
    Retorna el primer día del mes de la fecha recibida (dd-mm-yyyy)
    """
    first_day = date_obj.replace(day=1)
    return first_day.strftime("%d-%m-%Y")
 

def today_str(format="%d-%m-%Y"):
    """
    Devuelve la fecha de hoy
    """
    return datetime.now().strftime(format)