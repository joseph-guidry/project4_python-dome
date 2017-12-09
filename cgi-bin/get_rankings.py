#!/usr/bin/env python3

import cgi
import getpass
import mysql.connector
import webpage

def get_data():
	""" Query the database to gather data """
	login_name = getpass.getuser()  # Obtain user login name
	config = {"user": login_name, "database": login_name}
	connection = mysql.connector.connect(**config)

	sql = ("SELECT SUM(id) AS id, Name, SUM(wins) AS Wins FROM (SELECT id, Name, 0 AS wins "
		   "FROM combatant UNION ALL SELECT 0, Name, wins FROM c4 ) AS t1 "
		   "GROUP BY Name ORDER BY Wins DESC;")

	cursor = connection.cursor()
	cursor.execute(sql)

	
	data = [(row[0], row[1], row[2]) for row in cursor.fetchall()]
	#print(data)
	cursor.close()
	connection.close()
	
	print("<table><tr><h2>RANKINGS</h2></tr>"
		  "<tr><form action='/cgi-bin/select_combatant.py'>")
	print("<tr><td style='text-align:center;'><b>Combatant</b></td><td>Wins</td></tr>")
	for item in data:
		print("<tr><td><input type='radio' id='combatant" + str(item[0]) +"'")
		print("name='name' value='"+ str(item[0]) + "' checked>")
		print("<label for='combatant"+ str(item[0]) + 
              "'>", item[1],"</label></td>")
		print("<td>", item[2], "</td></tr>")
		

	print("<tr width=100%><td><input type='submit'>",
		  "<input type='reset'></form></td></tr>")
	
	print("</tr></table>")
	print("<a href='/index.html'>BACK</a>")

def main():
	""" Driver for this webpage """
	stylesheets = "<link rel='stylesheet' href='/css/tablestyle.css'"
	webpage.htmlTop(stylesheets)
	get_data()
	webpage.htmlBottom()

if __name__=="__main__":
	try:
		main()
	except:
		cgi.print_exception()
