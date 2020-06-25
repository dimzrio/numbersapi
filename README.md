# Numbersapi

Aplikasi sederhana (frontend & backend) yang dibuat menggunakan golang (gin-gonic). Backend merupakan REST API akan menggunakan current date sebagai data request ke http://numbersapi.com. Frontend akan mengambil data dari backend secara private. 

# How to works
Aplikasi (frontend & backend) di build menjadi docker images yang kemudian di deploy ke lingkungan kubernates cluster menggunakan helm chart.

# How to deploy
Script deploy.py adalah aplikasi sederhana yang dibuat menggunakan python3 untuk mempermudah proses deployment.

Help:
~~~~
usage: deploy.py [-h] -e ENVIRONMENT -s STACK

Deployment CLI

optional arguments:
  -h, --help            show this help message and exit
  -e ENVIRONMENT,       --env ENVIRONMENT
                        options: [development, staging, production]
  -s STACK,             --stack STACK
                        options: [frontend, backend]
~~~~

Example:
~~~~
Deploy Frontend:
$ python3 deploy.py -e production -s frontend

Deploy Backend:
$ python3 deploy.py -e production -s backend
~~~~