# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 20:08:14 2020

@author: Karan
"""


import xml.etree.ElementTree as ET
import sqlite3

conn=sqlite3.connect('tracks.sqlite')
cur=conn.cursor()

cur.executescript('''
    
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    name TEXT UNIQUE );

CREATE TABLE Genre(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    name TEXT UNIQUE );

CREATE TABLE Album(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    artist_id INTEGER,
    title TEXT UNIQUE );

CREATE TABLE Track(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER);
            ''')
    
file='Library.xml'
def lookup(d,key):
    found=False
    for child in d:
        if found : 
            return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff=ET.parse(file)
all=stuff.findall('dict/dict/dict')

for x in all:
    if lookup(x,'Track ID') is None:
        continue
    name=lookup(x,'Name')
    artist = lookup(x, 'Artist')
    album = lookup(x, 'Album')
    count = lookup(x, 'Play Count')
    rating = lookup(x, 'Rating')
    length = lookup(x, 'Total Time')
    genre=lookup(x,'Genre')
    
    if name is None or artist is None or album is None or genre is None or length is None or count is None:
        continue
    
    cur.execute('INSERT or IGNORE into Artist(name) VALUES (?)',(artist,))
    cur.execute('SELECT id from Artist WHERE name= ? ',(artist,))
    artist_id=cur.fetchone()[0]
    
    cur.execute('INSERT or IGNORE into Genre(name) VALUES (?)',(genre,))
    cur.execute('SELECT id from Genre WHERE name= ? ',(genre,))
    genre_id=cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id,genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id,length, rating, count ) )
    
    conn.commit()
    
curr.execute('SELECT * from ')
    