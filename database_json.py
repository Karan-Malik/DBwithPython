# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:12:23 2020

@author: Karan
"""

import sqlite3
import json

conn=sqlite3.connect('roster2.sqlite')
cur=conn.cursor()

cur.executescript('''
            
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    name TEXT UNIQUE);

CREATE TABLE Course(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    title TEXT UNIQUE);

CREATE TABLE Member(
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY(user_id,course_id));
            
            ''')

file=open('roster_data.json').read()
f=json.loads(file)

for entry in f:
    name=entry[0]
    title=entry[1]
    role=entry[2]
    
    cur.execute(' INSERT OR IGNORE into User(name) VALUES(?)',(name,))
    user_id= cur.execute('SELECT id from User where name= ?',(name,))
    user_id=cur.fetchone()[0]

    cur.execute(' INSERT OR IGNORE into Course(title) VALUES(?)',(title,))
    course_id= cur.execute('SELECT id from Course where title= ?',(title,))
    course_id=cur.fetchone()[0]
    
    cur.execute('INSERT OR REPLACE INTO Member(user_id,course_id,role) VALUES(?,?,?)',(user_id,course_id,role))

    conn.commit()

cur.execute('''
            SELECT User.name,Course.title,Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ''')

print(cur.fetchall())    
    
    
    
    
    
    
    