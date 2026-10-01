from rest_framework.pagination import PageNumberPagination


class KraftPagination(PageNumberPagination):
    """Отображение колличества страниц."""
    page_size = 5
    page_size_query_param = 'limit'