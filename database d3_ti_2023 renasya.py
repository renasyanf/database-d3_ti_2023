#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

database = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd =""

)

cursorObject = database.cursor()


cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[2]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE Mahasiswa (
                    NIM VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA VARCHAR(30) NOT NULL,
                    ALAMAT VARCHAR(255),
                    MATKUL_YANG_DIIKUTI VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)

dataBase.close()


# In[3]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Mahasiswa (NIM, NAMA, ALAMAT, MATKUL_YANG_DIIKUTI) VALUES (%s, %s, %s, %s)"
val = [("V3922018",  "ARCHIE", "JEBRES", "PRAKTIK PYTHON"),
       ("V3922019",  "ABIAN", "BANJARSARI", "PRAKTIK MIKROKONTOLEER"),
       ("V3922023",  "BIANAKA", "LAWIYAN", "PEMROGRAMAN WEB"),
       ("V3922034",  "JUAN", "BANJARSARI", "BASIS DATA"),
       ("V3922015",  "KHAIZURE", "SERENGAN", "STATITISKA")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

#Disconnect
dataBase.close()


# In[4]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE Dosen (
                    NIP VARCHAR(20) NOT NULL PRIMARY KEY,
                    NAMA_DOSEN VARCHAR(50) NOT NULL,
                    MATKUL_YANG_DIAJAR VARCHAR(50)
                    )"""

cursorObject.execute(studentRecord)

dataBase.close()


# In[5]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Dosen (NIP, NAMA_DOSEN, MATKUL_YANG_DIAJAR) VALUES (%s, %s, %s)"
val = [("18705642",  "YUSUF FADHIKA", "PRAKTIK PYTHON"),
       ("18706748",  "FENDI", "PRAKTIK MIKROKONTROLER"),
       ("18709839",  "MASBAHAH", "PEMROGRAMAN WEB"),
       ("18709021",  "MASBAHAH", "BASIS DATA"),
       ("18702470",  "TRISNA", "STATITISKA")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

#Disconnect
dataBase.close()


# In[6]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

query = "SELECT NAMA_MATKUL, NAMA_DOSEN FROM Mata_Kuliah"
cursorObject.execute (query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)
    
dataBase.close()


# In[7]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="d3_ti_2023"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE Mata_Kuliah (
                    KODE_MATKUL VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA_MATKUL VARCHAR(50) NOT NULL,
                    NAMA_DOSEN VARCHAR(20),
                    WAKTU DATE,
                    RUANGAN VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)

dataBase.close()


# In[8]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Mata_kuliah (KODE_MATKUL, NAMA_MATKUL, NAMA_DOSEN, WAKTU, RUANGAN) VALUES (%s, %s, %s, %s, %s)"
val = [("22114488",  "PRAKTIK PYTHON", "YUSUF FADHIKA", "2023-3-1", "Lab 2"),
       ("44668899",  "PRAKTIK MIKROKONTROLER", "FENDI", "2023-3-1", "Lab 1"),
       ("11332266",  "PEMROGRAMAN WEB", "MASBAHAH", "2023-3-1", "R. Mikro"),
       ("55994477",  "BASIS DATA", "MASBAHAH", "2023-3-2", "R. Mikro"),
       ("22447766",  "STATITISKA", "TRISNA", "2023-3-2", "Lab 2")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

#Disconnect
dataBase.close()


# In[9]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "d3_ti_2023"
)

#preparing cursor
cursorObject = dataBase.cursor()

query = "SELECT NAMA_MATKUL, NAMA_DOSEN FROM Mata_Kuliah"
cursorObject.execute (query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)
    
dataBase.close()


# In[ ]:




