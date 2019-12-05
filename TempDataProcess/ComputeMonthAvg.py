import psycopg2

#Connects to db
con = psycopg2.connect(
            host = "localhost",
            database = "tempdata",
            user = "jack",
            password = "lozfiresword")

#Create Cursor
cur = con.cursor()
#Execute Query
cur.execute("select distinct(country) from temperatures;")
#Catch all results as countries
countries = cur.fetchall()

#Create second cursor for averages query
cur2 = con.cursor()
#Create third cursor for insertion into monthavg
cur3 = con.cursor()
avgmonth = 0.0
for i in countries:
    for c in i:
        for j in range(1,13):
            cur2.execute("select avg(temp) from temperatures where country = %s and month = %s;",(c,j))
            avgmonth = cur2.fetchall()
            for avg in avgmonth:
                cur3.execute("insert into monthavg(country, month, avgtemp) values(%s,%s,%s);",(c,j,avg))

#Commit any changes
con.commit()

#Close Cursor
cur.close()
cur2.close()
cur3.close()
#Closes Connection
con.close()