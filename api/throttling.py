from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class customanaonthrotling(AnonRateThrottle):
    scope = 'useranon'
    
class customuserSthrotling(UserRateThrottle):
    scope = 'userreg'
