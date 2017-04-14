#!/usr/bin/env python
# coding: utf-8
#

from wxbot import *


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:#代表是个人用户 且为文本
            self.send_msg_by_uid(u'hi', msg['user']['id'])
            #self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])
        elif msg['msg_type_id'] == 3 and msg['content']['type'] == 0:#群消息 文本 想找到特定群
            print "group----------"
            #print group_list[msg['to_user_id']]
'''
    def schedule(self):
        self.send_msg(u'李四', u'测试')
        time.sleep(1)
'''


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
