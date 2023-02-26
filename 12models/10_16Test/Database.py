

import pymysql


class Sign(object):
    def __init__(self):
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'abc123',
            'database': 'fraudpreventionsystem',
            'charset': 'utf8mb4',
            # 'cursorclass': pymysql.cursors.Cursor,
        }

        # connection = pymysql.connect(**config)
        # self.db = pymysql.connect(db='store', user='shiboyao', passwd='1234')
        self.db = pymysql.connect(**config)
        self.cursor = self.db.cursor()
        self.CID = None

    def login(self, cid, password):
        self.cursor.execute("SELECT * FROM CUSTOMER WHERE CID = %s AND PASSWORD = %s", (cid, password))
        count = len(self.cursor.fetchall())
        if (count > 0):
            print("Congratulation! Login Success!")
            self.CID = cid
            return True
        else:
            print("Username or Password incorrect.")
            return False

    def signup(self, fname, lname, email, address, phone, password):
        self.cursor.execute("SELECT MAX(CID) FROM CUSTOMER")
        cid = str(int(self.cursor.fetchall()[0][0]) + 1)
        try:
            self.cursor.execute("INSERT INTO CUSTOMER VALUES('%s','%s','%s','%s','%s','%s', '%d', '%s')" % (
            cid, fname, lname, email, address, phone, 0, password))
            self.db.commit()

            print("Sucess.\n UserID:'%s'\n Email:'%s'\n" % (cid, email))
            return cid
        except:
            self.db.rollback()
            print("Failed.\n")
            return False

    def delete(self, cid):
        sql = "DELETE FROM CUSTOMER WHERE CID = '%s'" % cid
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def revise(self):
        pass

    def closedb(self):
        self.db.close()




class Admin(object):
    def __init__(self):
        self.db = pymysql.connect(db='store', user='shibo', passwd='1234')
        self.cursor = self.db.cursor()
        # self.CID = Sign.CID

    def viewbystatus(self, status):
        self.cursor.execute("SELECT C.CARTID, C.TSTATUS, C.TDATE FROM CART C WHERE C.TSTATUS = %s", (status))
        result = self.cursor.fetchall()
        print(result)
        return result

    def processorder(self, cartid, status):
        try:
            self.cursor.execute("UPDATE CART SET TSTATUS = '%s' WHERE CARTID = '%s'" % (status, cartid))
            self.db.commit()
            return True
        except:
            print("Failed to process.\n")
            return False

    def mostsold(self, date1, date2):
        '''
        most frequent products
        '''
        self.cursor.execute(
            "SELECT SUM(A.QUANTITY), P.PNAME FROM CART C, APPEARS_IN A, PRODUCT P WHERE C.CARTID = A.CARTID AND C.TDATE BETWEEN '%s' AND '%s' AND A.PID = P.PID GROUP BY A.PID ORDER BY SUM(A.QUANTITY) DESC" % (
            date1, date2))
        result = self.cursor.fetchall()
        if len(result) != 0:
            return result[0]
        else:
            return result

    def mostsold2(self, date1, date2):
        '''
        most popular to distinct customers
        '''
        self.cursor.execute(
            "SELECT COUNT(C.CID), P.PNAME FROM CART C, APPEARS_IN A, PRODUCT P WHERE C.CARTID = A.CARTID AND C.TDATE BETWEEN '%s' AND '%s' AND A.PID = P.PID GROUP BY A.PID ORDER BY COUNT(C.CID) DESC" % (
            date1, date2))
        result = self.cursor.fetchall()
        if len(result) != 0:
            return result[0]
        else:
            return result

    def ten_customer(self, date1, date2):
        '''
        spent most money
        '''
        self.cursor.execute(
            "SELECT C.CID, CUSTOMER.FNAME, SUM(A.PRICESOLD*A.QUANTITY) FROM CUSTOMER, CART C, APPEARS_IN A, PRODUCT P WHERE C.CID = CUSTOMER.CID AND C.CARTID = A.CARTID AND C.TDATE BETWEEN '%s' AND '%s' AND A.PID = P.PID GROUP BY C.CID ORDER BY SUM(A.PRICESOLD*A.QUANTITY) DESC" % (
            date1, date2))
        result = self.cursor.fetchall()
        return result[:min(10, len(result))]

    def five_zip(self, date1, date2):
        '''
        shipments made
        '''
        self.cursor.execute(
            "SELECT S.ZIP, COUNT(*) FROM CART C, SHIP_ADDRESS S WHERE C.SANAME = S.SANAME  AND C.TDATE BETWEEN '%s' AND '%s' GROUP BY S.ZIP ORDER BY COUNT(*) DESC" % (
            date1, date2))
        result = self.cursor.fetchall()
        return result[:min(5, len(result))]

    def avg_price(self, date1, date2):
        '''
        per product type, desktop, laptop, printer
        '''
        self.cursor.execute(
            "SELECT P.PTYPE, AVG(A.PRICESOLD) FROM CART C, PRODUCT P, APPEARS_IN A WHERE C.CARTID = A.CARTID AND A.PID = P.PID AND C.TDATE BETWEEN '%s' AND '%s' GROUP BY P.PTYPE" % (
            date1, date2))
        result = self.cursor.fetchall()
        return result


def tupleMsg(t):
    if t == False or len(t) == 0:
        return "Nothing."
    else:
        msg = str()
        if t[0] != tuple:
            for m in t:
                msg = msg + '\n\n' + str(m)
        else:
            for m in t:
                line = str()
                for n in m:
                    line = line + ' ' + str(n)
                msg = msg + '\n\n' + line

        return msg



