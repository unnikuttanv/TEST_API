import requests
from json import dumps
import lib_logger as log
import sys

class ApiTest(object):

    def __init__(self, url, log_file):
        self.url = url
        self.logger = log_file

    def get_method(self):
        self.logger.info("Testing get")
        try:
            response = requests.get(self.url)
            return response
        except requests.exceptions.ConnectionError as err:
            self.logger.info(("OOps: Something Else%s\nMake sure your internet connection is proper "%err))
            sys.exit(1)

    def post_method(self, data):
        self.logger.info("Testing post")
        try:
            response = requests.post(self.url, dumps(data), timeout=3)
            return response
        except requests.exceptions.ConnectionError as err:
            self.logger.info(("OOps: Something Else%s\nMake sure your internet connection is proper "%err))
            sys.exit(1)

    def delete_method(self, user_id):
        self.logger.info("Testing delete")
        self.url + str(user_id)
        try:
            response = requests.post(self.url, timeout=3)
            return response
        except requests.exceptions.ConnectionError as err:
            self.logger.info(("OOps: Something Else%s\nMake sure your internet connection is proper " % err))
            sys.exit(1)
        
    def patch_method(self, data, user_id):
        self.logger.info("Testing patch")
        self.url + str(user_id)
        try:
            response = requests.post(self.url, dumps(data), timeout=3)
            return response
        except requests.exceptions.ConnectionError as err:
            self.logger.info(("OOps: Something Else%s\nMake sure your internet connection is proper " % err))
            sys.exit(1)

    def put_method(self, data, user_id):
        self.logger.info("Testing put")
        self.url + str(user_id)
        try:
            response = requests.post(self.url, dumps(data), timeout=3)
            return response
        except requests.exceptions.ConnectionError as err:
            self.logger.info(("OOps: Something Else%s\nMake sure your internet connection is proper " % err))
            sys.exit(1)






