import sqlite3

def connect():
	conn=sqlite3.connect("buku.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS buku (id INTEGER PRIMARY KEY, judul text, penulis text, tahun integer, isbn integer)")
	conn.commit()
	conn.close()

def tambah(judul,penulis,tahun,isbn):
	conn=sqlite3.connect("buku.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO buku VALUES (NULL,?,?,?,?)",(judul,penulis,tahun,isbn))
	conn.commit()
	conn.close()

def lihat():
	conn=sqlite3.connect("buku.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM buku")
	rows=cur.fetchall()
	conn.close()
	return rows

def cari(judul="",penulis="",tahun="",isbn=""):
	conn=sqlite3.connect("buku.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM buku WHERE judul=? OR penulis=? OR tahun=? OR isbn=?", (judul,penulis,tahun,isbn))
	rows=cur.fetchall()
	conn.close()
	return rows

def hapus(id):
	conn=sqlite3.connect("buku.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM buku WHERE id=?", (id,))
	conn.commit()
	conn.close()

def ubah(id,judul,penulis,tahun,isbn):
	conn=sqlite3.connect("buku.db")
	cur=conn.cursor()
	cur.execute("UPDATE buku SET judul=?, penulis=?, tahun=?, isbn=? WHERE id=?", (judul,penulis,tahun,isbn,id))
	conn.commit()
	conn.close()

connect()
# testing connection to db :
# connect()
# # tambah("The Sea 4","John Tablet",1925,909090331)
# # hapus(2)
# # print(lihat())
# print(cari(judul="The Sea 4"))
# ubah(8,"The Moon","Jono",2012,02000234124)
# print(cari(judul="The Moon"))






