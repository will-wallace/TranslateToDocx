import sqlite3
from docx import Document

def write_to_document(content, document):

    p = document.add_paragraph(content)


def save_document(document):
    document.save("/Users/ericweiner/Documents/test.docx")

def get_path_settings(conn):
    sql = 'SELECT * FROM Resources;'
    c = conn.cursor()
    c.execute(sql)
    all_rows = c.fetchall()
    return all_rows

def open_db(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def main():
    db_file = "/Users/ericweiner/Downloads/All_DoD_Approved.sdb"
    conn = open_db(db_file)
    resources = get_path_settings(conn)
    document = Document()

    write_to_document(resources, document, "/Users/ericweiner/Documents/test.docx")

main()

#start with resources

