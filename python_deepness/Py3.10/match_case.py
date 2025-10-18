
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

# Konstrukcja match / case (tzw. Structural Pattern Matching) została wprowadzona w Pythonie 3.10 (wydanym w październiku 2021).
# Źródłem jest PEP 634, który opisuje dokładnie zasady działania tego mechanizmu.
# For the full specification see PEP 634. Motivation and rationale are in PEP 635, and a longer tutorial is in PEP 636.
