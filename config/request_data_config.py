# -*- coding:utf-8 -*-

class RequestData:
    phone = "13716203166"
    password = "123456"
    stateFilter = ["enabled,paused,archived", "paused,enabled", "archived,paused", "archived,enabled", "archived",
                   "enabled", "paused"]
    count = [10, 20, 30]
    startIndex = [0, 5, 10]
    storeId = ["f530bb36-3c4f-49ed-8821-909e8b94023c"]
    marketplace = ["DE"]
    CACHE_REFRESH = [True, False]
    CACHE_DETAIL = [True, False]
    ADVERTISING_REPORTS__BY_DATES = [True, False]
    ADVERTISING_REPORTS = [True, False]
    ADVERTISING_PARENTS = [True, False]
    adGroupIdFilter = ["222103830924374"]


"""
{
    "propsData": {
        "stateFilter": "enabled,paused",
        "count": 10,
        "startIndex": 10
    },
    "ADVERTISING_PARENTS": false,
    "ADVERTISING_REPORTS": false,
    "ADVERTISING_REPORTS__BY_DATES": false,
    "CACHE_DETAIL": true,
    "CACHE_REFRESH": true,
    "marketplace": "DE",
    "storeId": "f530bb36-3c4f-49ed-8821-909e8b94023c",
    "accessTokenCookie": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MjIxODQ4MzIsIm5iZiI6MTYyMjE4NDgzMiwianRpIjoiZDVlYTk0MWQtMDMwYy00MWU0LTgxOGEtNzliNWEyZTEwOTY0IiwiZXhwIjoxNjI0Nzc2ODMyLCJpZGVudGl0eSI6IktYSHRVeE1RYUlsUFFucU5hM2pUIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.2eJyV55iJxs1BnZhxN2f4fXCzslbmZ2X2moLFiDK9hY"
}
"""
