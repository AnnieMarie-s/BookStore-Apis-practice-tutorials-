from rest_framework.pagination import PageNumberPagination, CursorPagination, LimitOffsetPagination

class  custompagepagination(PageNumberPagination):
     page_size = 1
     page_query_param ='p'
     

class  customcursoepagination(CursorPagination):
     page_size = 1
     page_query_param ='p'
     

class  customlimitpagination(LimitOffsetPagination):
     default_limit = 1
