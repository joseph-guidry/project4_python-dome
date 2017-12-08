#!/usr/bin/env python3

import mysql.connector
import getpass
import webpage


def get_data():
	""" Query the database to gather data """
	login_name = getpass.getuser()  # Obtain user login name
	config = {"user": login_name, "database": login_name}
	connection = mysql.connector.connect(**config)

	sql = "SELECT id, name FROM combatant ORDER BY name;"
	cursor = connection.cursor()
	cursor.execute(sql)

	names = [(row[0], row[1]) for row in cursor.fetchall()]
	cursor.close()
	connection.close()

	#This needs to take the data form the data base and output it with HTML.
	
	print("<table><form action='/cgi-bin/select_combatant.py'>")
	print("<p>Select a combatant to view more details</p>\n<div>")
	for item in names:
		print("<input type='radio' id='combatant" + str(item[0]) +"' checked ")
		print("name='name' value='"+ str(item[0]) + "'>")
		print("<label for='combatant"+ str(item[0]) + "'>", item[1],"</label><br/>")
	print("</div><div><input type='submit'><input type='reset'></div></form></table>")
	print("<a href='/index.html'>HOME</a>")

def main():
	webpage.htmlTop()
	get_data()
	webpage.htmlBottom()


if __name__=="__main__":
	try:
		main()
	except:
		cgi.print_exception()
