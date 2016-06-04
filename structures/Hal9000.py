#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telepot
from private_data import data


class Hal9000:
    def __init__(self, token, ids):
        self.ids = ids
        self.bot = telepot.Bot(token)
        self.bot.message_loop(self.handle)
        self.running = True

    def handle(self, msg):
        msg_type, chat_type, chat_id = telepot.glance(msg)
        print msg_type, chat_type, chat_id
        if msg_type != 'text':
            return

        if chat_id not in self.ids:
            return

        command = msg['text'].strip().lower()
        who = msg['from']['id']
        if command == '/clima' or command == '/clima@hal_butler_bot':
            self.weather_message(chat_id)
        elif command == '/eventos' or command == '/eventos@hal_butler_bot':
            self.events_message(chat_id)
        elif command == '/start':
            self.bot.sendMessage(chat_id, 'Un gusto. Mi nombre es HAL-9000 pero me pueden decir Hal, '
                                     'seré su mayordomo virtual')
        elif who == data.master_id and command == '/reboot':
            self.running = False

    def weather_message(self, id_receiver):
        self.bot.sendMessage(id_receiver, 'Hoy es un bello día')

    def events_message(self, id_receiver):
        self.bot.sendMessage(id_receiver, 'También me gustaría ir a eventos!')

    def send_master_message(self, msg):
        self.bot.sendMessage(data.master_id, msg)


