import hashlib
import hmac
import base64
import datetime
from time import sleep


class Mac(object):
    def __init__(self, username):
        self.username = username
        self.key = b'\x4d\xe6\xbc\x49\xa2\x09\x32\x8a\x36\x85\x52\xb0\x7a\xdb\x28\xe2'

    def getHMac(self):
        message_username = (32 - len(self.username)) * b'\x00' + self.username.encode(encoding='UTF-8')
        now_time = datetime.datetime.now()
        # print(type(now_time))
        # now_time=datetime.datetime(2022-12-03 15:33:38)
        set_time = datetime.datetime(now_time.year, now_time.month, now_time.day, now_time.hour, now_time.minute,
                                     (30 if now_time.second > 30 else 0))
        message = message_username + set_time.year.to_bytes(2, byteorder='big') + set_time.month.to_bytes(1,
                                                                                                          byteorder='big') + set_time.day.to_bytes(
            1, byteorder='big') + set_time.hour.to_bytes(1, byteorder='big') + set_time.minute.to_bytes(1,
                                                                                                        byteorder='big') + set_time.second.to_bytes(
            1, byteorder='big')
        code = hmac.new(self.key, message, digestmod=hashlib.sha256)
        code_string = base64.b64encode(code.digest()).decode('UTF-8')
        return code_string

#
# if __name__ == "__main__":
#     cid = "aabb"
#     # key = b'\x4d\xe6\xbc\x49\xa2\x09\x32\x8a\x36\x85\x52\xb0\x7a\xdb\x28\xe2'
#     while (1):
#         print(datetime.datetime.now())
#         mac = Mac(cid)  # 在Cryp的类Mac()
#         macResult = mac.getHMac()
#         print(macResult)

        # print(getHMac(username,key))
        sleep(1)
