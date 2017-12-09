#!/usr/bin/env python3

import cgi
import getpass
import mysql.connector
import webpage

def get_data():
	default = ""
	fields = cgi.FieldStorage()
	species_id = int(fields.getvalue("species_id", default))
	name = fields.getvalue("name", default)

	if len(name) == 0:
		name = "'Blank'"

	""" Query the database to gather data """
	login_name = getpass.getuser()  # Obtain user login name
	config = {"user": login_name, "database": login_name}
	connection = mysql.connector.connect(**config)

	sql = ("INSERT INTO combatant VALUES(0, %s, %s, 0, 0, 0);")
	cursor = connection.cursor()
	try:
		cursor.execute(sql,( name, species_id,))
		connection.commit()
		print("<h3>Combatant Inserted</h3>")
		print("<a href='/combatants/combatants_list.html'>BACK</a>")
		print("<a href='/index.html'> HOME</a>")
	

	except IndexError:
		print("<p>ERROR</p><br/>")
		print("<a href='/index.html'>HOME</a>")

	cursor.close()
	connection.close()

def main():
	""" Driver for this webpage """
	stylesheets = "<link rel='stylesheet' href='/css/tablestyle.css'>"
	webpage.htmlTop(stylesheets)
	get_data()
	webpage.htmlBottom()


if __name__=="__main__":
	try:
		main()
	except:
		cgi.print_exception()
