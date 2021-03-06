import csv, sqlite3

conn = sqlite3.connect("uidai.db")
curs = conn.cursor()
curs.execute("CREATE TABLE uidai (Registrar TEXT, Agency TEXT, State TEXT, District TEXT, SubDistrict TEXT, PinCode TEXT, Gender TEXT, Age TEXT, AadhaarGenerated TEXT ,EnrollmentRejected TEXT, email TEXT, mobile TEXT);")

reader = csv.reader(open('UIDAI-ENR-DETAIL-20130520.csv', 'r'))

for row in reader:
    to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8"), unicode(row[3], "utf8"), unicode(row[4], "utf8"), unicode(row[5], "utf8"), unicode(row[6], "utf8"), unicode(row[7], "utf8"), unicode(row[8], "utf8"), unicode(row[9], "utf8"), unicode(row[10], "utf8"), unicode(row[11], "utf8")]
    curs.execute("INSERT INTO uidai (Registrar, Agency, State, District, SubDistrict, PinCode, Gender, Age, AadhaarGenerated ,EnrollmentRejected, email, mobile) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
conn.commit()
