#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from datetime import date, datetime


class EventDatabase:
    def __init__(self, db_name):
        self.db = db_name
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        sql = 'create table if not exists Events (id INTEGER PRIMARY KEY, ' \
              'event text, description text, event_date date, event_hour date)'
        c.execute(sql)
        conn.commit()
        c.close()
        conn.close()

    def add_event(self, name, description, year, month, day, hour, minutes):
        event_date = date(year, month, day)
        event_hour = datetime(year, month, day, hour, minutes, 0)
        conn = sqlite3.connect(self.db)
        conn.execute("INSERT INTO Events(event, description, event_date, event_hour) values (?, ?, ?, ?)",
                     (name, description, event_date, event_hour))
        conn.commit()

    def get_all_events(self):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute('select * from Events')
        rows = cur.fetchall()
        return rows

    def get_events_from_day(self, year, month, day):
        event_date = date(year, month, day)
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute('select * from Events where event_date=?', (event_date,))
        rows = cur.fetchall()
        return rows
