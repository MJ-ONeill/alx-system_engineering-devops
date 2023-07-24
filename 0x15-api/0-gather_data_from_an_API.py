poes
#!/usr/bin/python3
"""
write a python script using this REST API for a employe ID"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + "users/{}".format(sys.argv[1])
    todo_url
