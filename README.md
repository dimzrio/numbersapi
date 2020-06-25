# numbersapi

Aplikasi sederhana (frontend dan backend) yang dibuat menggunakan golang (gin-gonic). Backend merupakan REST API akan menggunakan current date sebagai data request ke http://numbersapi.com. Frontend akan mengambil data dari backend secara private.

# How to works?

Request:

frontend ----[GET]----> backend ----[GET]----> numbersapis.com

Response:

frontend <----[JSON]---- backend <----[PlainText]---- numbersapi.com

