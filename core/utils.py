from django.contrib.gis.geoip2 import GeoIP2
from django.conf import settings
from math import radians, cos, sin, asin, sqrt


def is_float(str_num: str) -> bool:
    try:
        float(str_num)
        return True
    except ValueError:
        return False


def get_client_ip(request):
    """
    Получение IP адреса клиента из request.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_geoip_from_request(request):
    """
    Получение геолокации клиента из request по IP.
    """
    g = GeoIP2()
    ip = get_client_ip(request)
    try:
        if settings.DEBUG:
            # Тестовый ip для Москвы
            return g.city('83.220.236.105')
        return g.city(ip)
    except Exception:
        return None


def calc_autoservice_distance_for_user(la1, la2, lo1, lo2):
    """
    Расчет растояние между двумя точками на карте.
    la - latitude, lo - longitude.
    """
    lo1 = radians(lo1)
    lo2 = radians(lo2)
    la1 = radians(la1)
    la2 = radians(la2)

    D_Lo = lo2 - lo1
    D_La = la2 - la1
    P = sin(D_La / 2)**2 + cos(la1) * cos(la2) * sin(D_Lo / 2) ** 2

    Q = 2 * asin(sqrt(P))
    R_km = 6371
    return Q * R_km
