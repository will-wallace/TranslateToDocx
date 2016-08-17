import sqlite3
import os
import fnmatch
import re
from subprocess import check_call
from docx import Document
from docx.shared import Inches
import datetime

from bs4 import BeautifulSoup, Tag
import urllib.request
from optparse import OptionParser
import csv, json


#def write_to_doc(content, document, documentName=1):
#    p = document.addParagraph(content)


#    document.save(documentName)


def get_resources(conn):
    sql = 'SELECT * FROM Resources'
    c = conn.cursor()
    c.execute(sql)
    all_rows = c.fetchall()
    return all_rows


def get_Path_Settings(conn):
    sql = 'select PathSettingsId,PathSettingsName,LastChange from PathSettings;'
    c = conn.cursor()
    c.execute(sql)
    all_rows = c.fetchall()
    return all_rows


def get_Security_Envs(conn):
    sql = 'select SecurityEnvironmentId,SecurityEnvironmentName,LastChange from SecurityEnvironments;'
    c = conn.cursor()
    c.execute(sql)
    all_rows = c.fetchall()
    return all_rows

def parse_Path_Settings(conn):
    sql2 = 'select PathSettings from PathSettings;'
    c = conn.cursor()
    c.execute(sql2)
    all_rows = [item[0] for item in c.fetchall()]
    file = open('sqlresult.txt', 'rw')
    file.write(all_rows[0])
    xml = file.read()
    soup = BeautifulSoup(xml)
    items = soup.findAll("item")
    for item in items:
        second = item.findAll("second")
        if "first" in item.attrs:
            first = item.attrs["first"]
            if "which" in second.attrs:
                which = second.attrs["which"]
                value = second.attrs["value"]
                if which == 0 and value == 0:
                    value = False





def open_db(db_file):
    conn = sqlite3.connect(db_file)

    return conn


def main():
    db_file = "/Users/williamwallace/All_DoD_Approved.sdb"
    conn = open_db(db_file)
    print(get_resources(conn))
    print(get_Path_Settings(conn))
    print(get_Security_Envs(conn))
    print(parse_Path_Settings(conn))
    resources = get_resources(conn)
    doc = Document()
    #write_to_doc(resources, doc, "/Users/williamwallace/Documents/docx-test.docx")

main()

#start with resources

