import lib_logger as log
from lib_urllib import ApiTest
import yamlordereddictloader
import yaml
import random
import os
import httplib
import re


class RestApi(object):

    def __init__(self):
        self.config_dict = {}
        self.test_dict = {}
        self.load_stability_commands()
        self.log_file = self.config_dict['Log_file']
        self.logger = log.setup_custom_logger (self.log_file)
        if os.path.exists (os.path.join(os.getcwd (), self.config_dict['Log_file'])+".log"):
            os.remove (os.path.join(os.getcwd (), self.config_dict['Log_file'])+".log")
            self.logger.info ("removing the logger file")
        self.logger.info("Configuration parameters %s" % self.config_dict)

    def load_stability_commands(self):
        try:
            self.config_dict = yaml.load (open ('settings/config.yml'), Loader=yamlordereddictloader.Loader)
        except IOError as e:
            "I/O error({0}): {1}".format(e.errno, e.strerror)

    def load_test(self):
        try:
            self.test_dict = yaml.load (open ('settings/test.yml'), Loader=yamlordereddictloader.Loader)
            self.logger.info("Test cases and pass criteria %s" % self.test_dict)
        except IOError as e:
            "I/O error({0}): {1}".format(e.errno, e.strerror)

    def run_test(self):
        album_obj = ApiTest(self.config_dict['Url_albums'], self.logger)
        users_obj = ApiTest(self.config_dict['Url_users'], self.logger)
        album_data ={
                "id": 1,
                "name": "Leanne Graham",
                "username": "Bret",
                "email": "Sincere@april.biz",
                "address": {
                    "street": "Kulas Light",
                    "suite": "Apt. 556",
                    "city": "Gwenborough",
                    "zipcode": "92998-3874",
                    "geo": {
                        "lat": "-37.3159",
                        "lng": "81.1496"
                    }
                },
                "phone": "1-770-736-8031 x56442",
                "website": "hildegard.org",
                "company": {
                    "name": "Romaguera-Crona",
                    "catchPhrase": "Multi-layered client-server neural-net",
                    "bs": "harness real-time e-markets"
                }
            }

        user_id = random.randint(1, 10)
        for key, elem in self.test_dict.iteritems():
            if re.match('Test01', key, re.IGNORECASE):
                self.logger.info("Executing Test01 : %s" % self.test_dict[key])
                in_data=album_obj.get_method()
                if 'OK' == (httplib.responses[in_data.status_code]):
                    self.logger.info("TEST01: PASSED")
                else:
                    self.logger.info("TEST02: FAILED as %s"%(httplib.responses[in_data.status_code]))

            elif re.match('Test02', key, re.IGNORECASE):
                self.logger.info("Executing Test02 : %s" % self.test_dict[key])
                in_data=album_obj.get_method()
                if 'OK' == (httplib.responses[in_data.status_code]):
                    self.logger.info("TEST02: PASSED")
                else:
                    self.logger.info("TEST02: FAILED as %s" % (httplib.responses[in_data.status_code]))

            elif re.match('Test03', key, re.IGNORECASE):
                self.logger.info("Executing Test03 : %s" % self.test_dict[key])
                if '201' in str(album_obj.delete_method(user_id=user_id)):
                    self.logger.info("TEST03: PASSED")
                else:
                    self.logger.info("TEST02: FAILED as %s" % (httplib.responses[in_data.status_code]))

            elif re.match('Test04', key, re.IGNORECASE):
                self.logger.info("Executing Test04 : %s" % self.test_dict[key])
                if '201' in str(album_obj.patch_method(data=album_data,user_id=user_id)):
                    self.logger.info("TEST04: PASSED")
                else:
                    self.logger.info("TEST02: FAILED as %s" % (httplib.responses[in_data.status_code]))

            elif re.match('Test05', key, re.IGNORECASE):
                self.logger.info("Executing Test05 : %s" % self.test_dict[key])
                if '201' in str(album_obj.put_method(data=album_data,user_id=user_id)):
                    self.logger.info("TEST05: PASSED")
                else:
                    self.logger.info("TEST02: FAILED as %s" % (httplib.responses[in_data.status_code]))

            elif re.match('Test06', key, re.IGNORECASE):
                self.logger.info("Executing Test06: %s" % self.test_dict[key])
                in_data_album= album_obj.get_method()
                in_data_album_json = in_data_album.json()
                user_ids = [data['id'] for data in in_data_album_json]
                for i in range(0,100):
                    if user_ids[i] == i+1:
                        self.logger.info("PASSED album data %s" % i)
                    else:
                        self.logger.info("FAIL album data %s"%i)

            elif re.match('Test07', key, re.IGNORECASE):
                self.logger.info("Executing Test07: %s" % self.test_dict[key])
                in_data_user= users_obj.get_method()
                in_data_user_json = in_data_user.json()
                user_ids = [data['id'] for data in in_data_user_json]
                for i in range(0,10):
                    if user_ids[i] == i + 1:
                        self.logger.info("PASSED user data %s" % i)
                    else:
                        self.logger.info("FAIL user data %s" % i)

            elif re.match('Test08', key, re.IGNORECASE):
                self.logger.info("Executing Test08: %s" % self.test_dict[key])
                in_data_album = album_obj.get_method()
                in_data_user = users_obj.get_method()
                if float(in_data_album.elapsed.total_seconds()) < 2.0 and float(in_data_user.elapsed.total_seconds()) < 2.0:
                    self.logger.info("TEST08: PASSED")
                else:
                    self.logger.info("TEST08: FAILED %s seconds"%in_data_album.elapsed.total_seconds())

            elif re.match('Test09', key, re.IGNORECASE):
                self.logger.info("Executing Test09: %s" % self.test_dict[key])
                in_data_user = users_obj.get_method()
                in_data_user_json = in_data_user.json()
                email_ids = [data['email'] for data in in_data_user_json]
                for email_id in email_ids:
                    self.logger.info("PASSED for email id %s"%email_id)
                else:
                    self.logger.info("FAILED for email id %s"%email_id)
            else:
                pass

if __name__ == '__main__':
    x = RestApi()
    x.load_stability_commands()
    x.load_test()
    x.run_test()
