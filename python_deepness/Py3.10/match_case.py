
# match response.status:
#     case 200:
#         do_something(response.data)  # OK
#     case 301 | 302:
#         retry(response.location)  # Redirect
#     case 401:
#         retry(auth=get_credentials())  # Login first
#     case 426:
#         sleep(DELAY)  # Server is swamped, try after a bit
#         retry()
#     case _:
#         raise RequestError("we couldn't get the data")
#
