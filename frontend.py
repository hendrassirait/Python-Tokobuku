from tkinter import *
import backend

def get_selected_row(event):
	try:
		global selected_item
		index=list1.curselection()[0]
		selected_item=list1.get(index)
		e1.delete(0,END)
		e1.insert(END,selected_item[1])
		e2.delete(0,END)
		e2.insert(END,selected_item[3])
		e3.delete(0,END)
		e3.insert(END,selected_item[2])
		e4.delete(0,END)
		e4.insert(END,selected_item[4])
	except IndexError:
		pass


def com_lihat():
	# to delete remaining item on list box before click lihat semua
	list1.delete(0,END)
	for row in backend.lihat():	
		list1.insert(END,row)

def com_cari():
	list1.delete(0,END)
	for row in backend.cari(Judul_text.get(),Penulis_text.get(),Tahun_text.get(),ISBN_text.get()):
		list1.insert(END,row)

def com_tambah():
	backend.tambah(Judul_text.get(),Penulis_text.get(),Tahun_text.get(),ISBN_text.get())
	list1.delete(0,END)
	list1.insert(END,(Judul_text.get(),Penulis_text.get(),Tahun_text.get(),ISBN_text.get()))

def com_hapus():
	backend.hapus(selected_item[0])
	# to make it automatically reset list
	list1.delete(0,END)
	for row in backend.lihat():	
		list1.insert(END,row)

def com_ubah():
	backend.ubah(selected_item[0],Judul_text.get(),Penulis_text.get(),Tahun_text.get(),ISBN_text.get())
	# to make it automatically reset list
	list1.delete(0,END)
	for row in backend.lihat():	
		list1.insert(END,row)

window=Tk()

window.wm_title("Tokobuku")

l1=Label(window,text="Judul")
l1.grid(row=0,column=0)

l2=Label(window,text="Tahun")
l2.grid(row=1,column=0)

l3=Label(window,text="Penulis")
l3.grid(row=0,column=2)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

Judul_text=StringVar()
e1=Entry(window,textvariable=Judul_text)
e1.grid(row=0,column=1)

Tahun_text=StringVar()
e2=Entry(window,textvariable=Tahun_text)
e2.grid(row=1,column=1)

Penulis_text=StringVar()
e3=Entry(window,textvariable=Penulis_text)
e3.grid(row=0,column=3)

ISBN_text=StringVar()
e4=Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)


b1=Button(window,text="Lihat Semua", width=12,command=com_lihat)
b1.grid(row=2,column=3)

b2=Button(window,text="Cari", width=12,command=com_cari)
b2.grid(row=3,column=3)

b3=Button(window,text="Tambah", width=12,command=com_tambah)
b3.grid(row=4,column=3)

b4=Button(window,text="Ubah", width=12,command=com_ubah)
b4.grid(row=5,column=3)

b5=Button(window,text="Hapus", width=12,command=com_hapus)
b5.grid(row=6,column=3)

b6=Button(window,text="Tutup", width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
