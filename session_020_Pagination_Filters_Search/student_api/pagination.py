from rest_framework.pagination import PageNumberPagination


class SmallPageNumberPagination(PageNumberPagination):
    page_size = 8
    page_query_param ="sayfa"

from rest_framework.pagination import LimitOffsetPagination


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'adet'  # Defaults to 'limit'.



from rest_framework.pagination import CursorPagination


class MycursorPagination(CursorPagination):
    page_size=10
    ordering = "-id"






