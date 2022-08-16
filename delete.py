import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="kiran1415@A",
  database= "pk_bank"
)

mycursor = mydb.cursor()

def delete():
    a=input("Are You Sure You Want To Delete Your Account(Y/N): ")
    if a=='Y'or a=='y':
        b=int(input("Enter Account Number: "))
        c=int(input("Enter Phone Number: "))
        sql="SELECT * from customer;"
        mycursor.execute(sql)
        rows=mycursor.fetchall()

        for row in rows:
            if b==row[1]:
                if c==row[2]:
                    sql = """delete from customer where AccountNumber=%s and PhoneNo=%s;"""
                    valus=(b,c)
                    mycursor.execute(sql,valus)
                    mydb.commit()
                    # mydb.close()
                    print("Hey, {0} You are Deleted Your Account ...........".format(row[0]))
        pass
    elif a=='N' or a=='n':
        print("Thank You")
    else:
        print("Enter Correct Option")