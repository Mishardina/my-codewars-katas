#https://www.codewars.com/kata/52fefe6cb0091856db00030e

from datetime import datetime

class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        """returns True if s is a valid MongoID; otherwise False"""
        pass
    
    @classmethod
    def get_timestamp(cls, s):
        """if s is a MongoID, returns a datetime object for the timestamp; otherwise False"""
        pass