#!/usr/bin/env python3

import gitlab
import sys
import getpass


# private token or personal token authentication
gl = gitlab.Gitlab('http://host_ip', private_token='***************')

count_of_user = int(input("Please enter count of users which you wont to create: "))

for i in range(count_of_user):
    Email    = input("Enter email of user (example: john@doe.com): ")
    Password = getpass.getpass(prompt='Enter password of user (example: s12cuq4af8Hr9): ', stream=None)
    Username = input("Enter username of user (example: jdoe): ")
    Name     = input("Enter name of user (example: John Doe): ")
    try:
        user = gl.users.create({'email': Email,
                        'password': Password,
                        'username': Username,
                        'name': Name})
    except:
        print("User is alredy exsist")

users = gl.users.list()
for user in users:
    print("User={0}\nUsername={1}\nEmail={2}".format(user.name, user.username, user.email))
