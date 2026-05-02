#!/usr/bin/python3
""" User class """

class User:
    def __init__(self):
        self.__password = None

    def set_password(self, pwd):
        self.__password = pwd

    def is_valid_password(self, pwd):
        return self.__password == pwd
