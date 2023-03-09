import sqlite3
#import backend

#---------BLOCK A QUERIES--------#    
def A1_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='A1' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row

def A2_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='A2' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row

def A3_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='A3' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row

def A4_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='A4' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row
    

#---------BLOCK B QUERIES--------#    
def B1_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='B1' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row
    
def B2_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='B2' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row
    
def B3_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='B3' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row
    
def B4_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='B4' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row


#---------BLOCK C QUERIES--------#    
def C1_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='C1' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row
    
def C2_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='C2' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row
    
def C3_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='C3' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row
    
def C4_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='C4' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row


#---------BLOCK D QUERIES--------#    
def D1_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='D1' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row
    
def D2_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='D2' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row
    
def D3_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='D3' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row
    
def D4_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='D4' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row


#---------BLOCK E QUERIES--------#    
def E1_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='E1' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row
    
def E2_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='E2' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row
    
def E3_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='E3' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row
    
def E4_query():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT TenantName,Nationality,Room.ApartmentType,Room.ApartmentNo, \
                MobileNumber,EmailAddress,EmergencyContact,ContactPerson,Room.RoomStatus,MovedIn,MovedOut FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID WHERE ApartmentType='E4' \
                ORDER BY ApartmentNo")
    row = cur.fetchall()
    link.close()
    return row


#---------VIEW AND SEARCH QUERIES--------# 
def t_rview():
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT Room.rID,TenantName,Gender,MobileNumber,Address,EmailAddress,Nationality, \
                EmergencyContact,ContactPerson,MovedIn,MovedOut,Room.Block,Room.ApartmentType,Room.ApartmentNo, \
                Room.RoomStatus FROM Tenant \
                INNER JOIN Room ON Room.rID = Tenant.tID  \
                ORDER BY Room.rID")
    row = cur.fetchall()
    link.close()
    return row

def t_rsearch(t_name='',sex='',mobileno='',address='',email='',nationality='', \
            emgcontact='',ct_name='',movein='',moveout='',blk='',apt_t='',apt_num='',rms=''):
    link = sqlite3.connect('TDB.db')
    cur = link.cursor()
    cur.execute("SELECT Room.rID,TenantName,Gender,MobileNumber,Address,EmailAddress,Nationality, \
                EmergencyContact,ContactPerson,MovedIn,MovedOut,Room.Block,Room.ApartmentType,Room.ApartmentNo, Room.RoomStatus FROM Tenant INNER JOIN Room ON Room.rID = Tenant.tID WHERE Tenant.TenantName=? OR Tenant.Gender=? OR Tenant.MobileNumber=? \
                OR Tenant.Address=? OR Tenant.EmailAddress=? OR Tenant.Nationality=? OR Tenant.EmergencyContact=? OR Tenant.ContactPerson=? OR Tenant.MovedIn=? OR Tenant.MovedOut=? OR Room.Block= ? OR Room.ApartmentType=? OR Room.ApartmentNo=? OR Room.RoomStatus=?",(t_name,sex,mobileno,address,email,nationality,emgcontact,ct_name,movein,moveout,blk,apt_t,apt_num,rms))
    row = cur.fetchall()
    link.close()
    return row
    
    
from datetime import datetime as dt
#---------PREVIOUS TENANT QUERIES--------# 
def a1a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A1' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

def a1a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A1' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def a1a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A1' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

def a1a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A1' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
#-------------------------------------A2
def a2a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A2' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

def a2a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A2' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def a2a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A2' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

def a2a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A2' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
#-------------------------------------A3
def a3a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A3' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

def a3a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A3' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def a3a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A3' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

def a3a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A3' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
#-------------------------------------A4
def a4a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A4' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

def a4a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A4' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def a4a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A4' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

def a4a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='A4' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
#-------------------------------------B1

def b1a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B1' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def b1a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B1' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def b1a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B1' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def b1a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B1' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
#-------------------------------------B2
def b2a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B2' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def b2a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B2' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def b2a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B2' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def b2a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B2' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

#-------------------------------------B3
def b3a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B3' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def b3a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B3' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def b3a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B3' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def b3a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B3' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
#-------------------------------------B4
def b4a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B4' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def b4a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B4' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def b4a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B4' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def b4a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='B4' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

#-------------------------------------C1
def c1a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C1' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def c1a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C1' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def c1a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C1' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def c1a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C1' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
#-------------------------------------C2
def c2a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C2' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def c2a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C2' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def c2a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C2' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def c2a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C2' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

#-------------------------------------C3
def c3a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C3' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def c3a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C3' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def c3a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C3' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def c3a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C3' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

#-------------------------------------C4
def c4a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C4' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def c4a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C4' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def c4a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C4' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def c4a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='C4' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
#-------------------------------------D1
def d1a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D1' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def d1a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D1' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def d1a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D1' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def d1a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D1' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

#-------------------------------------D2
def d2a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D2' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def d2a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D2' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def d2a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D2' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def d2a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D2' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

#-------------------------------------D3
def d3a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D3' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def d3a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D3' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def d3a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D3' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def d3a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D3' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
#-------------------------------------D4
def d4a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D4' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def d4a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D4' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def d4a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D4' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def d4a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='D4' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
#-------------------------------------E1
def e1a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E1' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def e1a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E1' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def e1a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E1' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def e1a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E1' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

#--------------------------------------E2
def e2a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E2' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def e2a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E2' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def e2a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E2' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def e2a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E2' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

#-------------------------------------E3
def e3a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E3' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def e3a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E3' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def e3a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E3' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def e3a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E3' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row

#-------------------------------------E4
def e4a1Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E4' AND ApartmentNo='1'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def e4a2Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E4' AND ApartmentNo='2'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def e4a3Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E4' AND ApartmentNo='3'",(movein,))
    row = cur.fetchall()
    link.close()
    return row
    
def e4a4Query(movein):
    link = sqlite3.connect('BUP.db')
    cur = link.cursor()
    cur.execute("SELECT * FROM BACKUP WHERE MovedOut < ? AND ApartmentType='E4' AND ApartmentNo='4'",(movein,))
    row = cur.fetchall()
    link.close()
    return row


