import mysql.connector

f = mysql.connector.connect(host = "localhost", user = "root", passwd = "")
mycur = f.cursor()

mycur.execute("use MyHome;")
mycur.execute("insert into residents(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO, ISADMIN)values('{}','{}','{}','{}','{}','{}')".format("Rahul", "rahul123", "G509", "rahul@yahoo.com", "5372849103", "No"))
mycur.execute("insert into residents(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO, ISADMIN)values('{}','{}','{}','{}','{}','{}')".format("Joseph", "joseph123", "H002", "joseph@hotmail.com", "6351883920", "No"))
mycur.execute("insert into residents(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO, ISADMIN)values('{}','{}','{}','{}','{}','{}')".format("Emily", "emily123", "H107", "emily@yahoo.com", "9620183728", "No"))
mycur.execute("insert into residents(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO, ISADMIN)values('{}','{}','{}','{}','{}','{}')".format("Clark", "clark123", "Y501", "clark@gmail.com", "5462739167", "No"))
mycur.execute("insert into residents(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO, ISADMIN)values('{}','{}','{}','{}','{}','{}')".format("Ruby", "ruby123", "L809", "ruby@gmail.com", "7193726301", "No"))
mycur.execute("insert into residents(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO, ISADMIN)values('{}','{}','{}','{}','{}','{}')".format("George", "george123", "W100", "george@hotmail.com", "6572948273", "No"))
mycur.execute("insert into residents(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO, ISADMIN)values('{}','{}','{}','{}','{}','{}')".format("Vienna", "vienna123", "U707", "vienna@gmail.com", "5481038294", "No"))
mycur.execute("insert into residents(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO, ISADMIN)values('{}','{}','{}','{}','{}','{}')".format("Admin", "admin123", "N/A", "admin@yahoo.com", "0387149113", "Yes"))


mycur.execute("insert into PendingApprovals(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO)values('{}','{}','{}','{}','{}')".format("Chandan", "chandan123", "G719", "chandan@yahoo.com", "5372849103"))
mycur.execute("insert into PendingApprovals(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO)values('{}','{}','{}','{}','{}')".format("Joshua", "joshua123", "H002", "joshua@hotmail.com", "6351883920"))
mycur.execute("insert into PendingApprovals(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO)values('{}','{}','{}','{}','{}')".format("Sam", "sam123", "I107", "sam@yahoo.com", "6921180028"))
mycur.execute("insert into PendingApprovals(USERNAME, PASSWORD, UNITNO, EMAIL, PHONENO)values('{}','{}','{}','{}','{}')".format("Arvind", "arvind123", "E501", "arvind@gmail.com", "1235139167"))

mycur.execute("insert into facilities(NAME, DESCRIPTION)values('{}','{}')".format("Badminton", "Please remember to wear non-marking shoes while playing."))
mycur.execute("insert into facilities(NAME, DESCRIPTION)values('{}','{}')".format("Table Tennis", "Please remember to bring your own paddle and table tennis ball."))
mycur.execute("insert into facilities(NAME, DESCRIPTION)values('{}','{}')".format("Tennis", "Remember to handle the nets with care"))
mycur.execute("insert into facilities(NAME, DESCRIPTION)values('{}','{}')".format("Billiards", "Please keep the billiard sticks back to the holder after playing."))
#mycur.execute("insert into facilities(NAME, DESCRIPTION)values('{}','{}')".format("", ""))

mycur.execute("insert into bookings(FACILITYNAME, EMAIL, DATE, TIME)values('{}','{}','{}','{}')".format("Badminton", "clark@gmail.com", "2020-11-12", "5PM to 6PM"))
mycur.execute("insert into bookings(FACILITYNAME, EMAIL, DATE, TIME)values('{}','{}','{}','{}')".format("Tennis", "ruby@gmail.com", "2020-11-7", "4PM to 5PM"))
mycur.execute("insert into bookings(FACILITYNAME, EMAIL, DATE, TIME)values('{}','{}','{}','{}')".format("Billiards", "george@hotmail.com", "2020-11-10", "5PM to 6PM"))
mycur.execute("insert into bookings(FACILITYNAME, EMAIL, DATE, TIME)values('{}','{}','{}','{}')".format("Badminton", "emily@yahoo.com", "2020-11-1", "7PM to 8PM"))