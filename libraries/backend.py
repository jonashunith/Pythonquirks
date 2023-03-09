import sqlite3

def create_link():
    link = sqlite3.connect('../database/TDB.db')
    cur = link.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Tenant(tID INTEGER PRIMARY KEY AUTOINCREMENT, \
                TenantName VARCHAR,Gender VARCHAR,MobileNumber VARCHAR NOT NULL, \
                Address VARCHAR,EmailAddress VARCHAR,Nationality VARCHAR NOT NULL, \
                EmergencyContact VARCHAR NOT NULL,ContactPerson VARCHAR NOT NULL, MovedIn DATE NOT NULL,MovedOut DATE NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS Room(rID INTEGER PRIMARY KEY AUTOINCREMENT, \
                Block CHAR(1),ApartmentType VARCHAR,ApartmentNo VARCHAR, RoomStatus VARCHAR)")
    link.commit()
    link.close()

#-----------------------------------TENANT DATABASE-----------------------------------#

def t_insert(t_name,sex,mobileno,address,email,nationality,emgcontact,ct_name,movein,moveout):
    link = sqlite3.connect('../database/TDB.db')
    cur = link.cursor()
    cur.execute("INSERT INTO Tenant VALUES(NULL,?,?,?,?,?,?,?,?,?,?)",(t_name,sex,mobileno,address,email,nationality,emgcontact,ct_name,movein,moveout))
    link.commit()
    link.close()     

def t_delete(id):
    link = sqlite3.connect('../database/TDB.db')
    cur = link.cursor()
    cur.execute("DELETE FROM Tenant WHERE tID = ? ",(id,))
    cur.execute("DELETE FROM Room WHERE rID = ? ",(id,))
    link.commit()
    link.close()
    
def t_update(t_name,sex,mobileno,address,email,nationality,emgcontact,ct_name,movein,moveout,id):
    link = sqlite3.connect('../database/TDB.db')
    cur = link.cursor()
    cur.execute("UPDATE Tenant SET TenantName=?, Gender=?, MobileNumber=?, Address=?, \
                EmailAddress=?, Nationality=?, EmergencyContact=?, ContactPerson=?, MovedIn=?, MovedOut=? \
                WHERE tID = ?",(t_name,sex,mobileno,address,email,nationality,emgcontact,ct_name,movein,moveout,id))
    link.commit()
    link.close()    
    
def t_view():
    link = sqlite3.connect('../database/TDB.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM Tenant")
    rows = cur.fetchall()
    link.close()    
    return(rows)
    
def t_search(t_name='',sex='',mobileno='',address='',email='',nationality='', \
            emgcontact='',ct_name='',movein='',moveout=''):
    link = sqlite3.connect('../database/TDB.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM Tenant WHERE TenantName=? OR Gender=? OR MobileNumber=? \
    OR Address=? OR EmailAddress=? OR Nationality=? OR EmergencyContact=? OR ContactPerson=? \
    OR MovedIn=? OR MovedOut=?", (t_name,sex,mobileno,address,email,nationality,emgcontact,ct_name,movein,moveout))
    row = cur.fetchall()
    link.close()
    return row
    

    
#-----------------------------------ROOM DATABASE-----------------------------------#

def r_insert(blk,apt_t,apt_num,rms):
    link = sqlite3.connect('../database/TDB.db')
    cur = link.cursor()
    cur.execute("INSERT INTO Room VALUES(NULL,?,?,?,?)",(blk,apt_t,apt_num,rms))
    link.commit()
    link.close()     
    
def r_update(blk,apt_t,apt_num,rms,id):
    link = sqlite3.connect('../database/TDB.db')
    cur = link.cursor()
    cur.execute("UPDATE Room SET Block=?, ApartmentType=?, ApartmentNo=?, \
                RoomStatus=? WHERE rID=?",(blk,apt_t,apt_num,rms,id))
    link.commit()
    link.close()    
    
def r_view():
    link = sqlite3.connect('../database/TDB.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM Room")
    rows = cur.fetchall()
    link.close()    
    return(rows)
 
        
        
#-----------------------------------BACKUP DATABASE-----------------------------------#

def backup_link():
    link = sqlite3.connect('../database/BUP.db')
    cur = link.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS BACKUP (tID INTEGER PRIMARY KEY, \
                TenantName VARCHAR,Nationality VARCHAR,Gender VARCHAR,MobileNumber VARCHAR, \
                Address VARCHAR,EmailAddress VARCHAR, EmergencyContact VARCHAR, ContactPerson VARCHAR, \
                ApartmentType VARCHAR,ApartmentNo VARCHAR,MovedIn DATE,MovedOut DATE,BackupTime DATETIME)")
    link.commit()
    link.close()
         
def backup1():
    link = sqlite3.connect('../database/TDB.db')
    backuplink = sqlite3.connect('../database/BUP.db')
    with backuplink:
        link.backup(backuplink)
    backuplink.close()
    link.close()
    
def backup2():
    link = sqlite3.connect('../database/TDB.db')
    cur = link.cursor()
    cur.execute("ATTACH DATABASE ? AS BACKUP", ('../database/BUP.db',))
    cur.execute("ATTACH DATABASE ? AS ORIGIN", ('../database/TDB.db',))
    cur.execute("CREATE TABLE IF NOT EXISTS BACKUP.Backup (tID INTEGER PRIMARY KEY, \
                TenantName VARCHAR,Nationality VARCHAR,Gender VARCHAR,MobileNumber VARCHAR, \
                Address VARCHAR,EmailAddress VARCHAR, EmergencyContact VARCHAR, ContactPerson VARCHAR, \
                ApartmentType VARCHAR,ApartmentNo VARCHAR,MovedIn DATE,MovedOut DATE,BackupTime DATETIME)")
    try:
        cur.execute("INSERT OR REPLACE INTO BACKUP.Backup (tID,TenantName,Nationality,Gender, \
                    MobileNumber,Address,EmailAddress,EmergencyContact,ContactPerson,\
                    ApartmentType,ApartmentNo,MovedIn,MovedOut,MovedIn) \
                    SELECT tID,TenantName,Nationality,Gender,\
                    MobileNumber,Address,EmailAddress,EmergencyContact,ContactPerson,\
                    ApartmentType,ApartmentNo,MovedIn,MovedOut,MovedIn \
                    FROM ORIGIN.Tenant INNER JOIN ORIGIN.Room ON ORIGIN.Room.rID = ORIGIN.Tenant.tID")
    except: 
        cur.execute("DROP TABLE BACKUP")
        cur.execute("CREATE TABLE IF NOT EXISTS BACKUP.Backup (tID INTEGER PRIMARY KEY, \
                    TenantName VARCHAR,Nationality VARCHAR,Gender VARCHAR,MobileNumber VARCHAR, \
                    Address VARCHAR,EmailAddress VARCHAR, EmergencyContact VARCHAR, ContactPerson VARCHAR, \
                    ApartmentType VARCHAR,ApartmentNo VARCHAR,MovedIn DATE,MovedOut DATE,BackupTime DATETIME)")
    cur.execute("UPDATE BACKUP.Backup SET BackupTime = datetime('now') WHERE Backup.tID <= 80")
    link.commit()
    link.close()




create_link()   
backup_link()

backup2()


 
