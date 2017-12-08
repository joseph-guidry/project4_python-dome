#!/usr/bin/env python3

# Retrieve a list of battles that can be selected.
import cgi
import getpass
import mysql.connector
import webpage

def get_data():
	""" Query database for battle data """
	login_name = getpass.getuser()  # Obtain user login name
	config = {"user": login_name, "database": login_name}
	connection = mysql.connector.connect(**config)

	sql1 = ("DROP VIEW IF EXISTS c1, c2, c3;")
	sql2 = ("CREATE VIEW c1 AS SELECT c.id, c.Name FROM combatant c, fight f WHERE c.id = f.combatant_one;")
	sql3 = ("CREATE VIEW c2 AS SELECT c.id, c.Name FROM combatant c, fight f WHERE c.id = f.combatant_two;")
	sql4 = ("CREATE VIEW c3 AS SELECT DISTINCT c1.Name AS Name1, c2.Name AS Name2, f.winner_id, f.start, f.finish FROM fight f, c1, c2 WHERE f.combatant_one = c1.id AND f.combatant_two = c2.id;")
	sql5 = ("SELECT * FROM c3;")

	cursor = connection.cursor()
	cursor.execute(sql1, "")
	cursor.execute(sql2, "")
	cursor.execute(sql3, "")
	cursor.execute(sql4, "")
	cursor.execute(sql5, "")
	

	print("<p>")
	names = [row for row in cursor.fetchall()]

	#This needs to take the data form the data base and output it with HTML.
	print("<table><form action='/cgi-bin/select_battle.py'>")
	print("<p>Select a Battle to view more details</p>\n<div>")

	for number, name in enumerate(names):
		print("<input type='radio' id='battle" + str(number) +"' checked ")
		value = [name[2], str(name[4])]
		print("name='name'  value=\"",str(name[2]), ",", str(name[4]),"\">")
		print("<label for='combatant"+ str(number) + "'>", "Battle", str(number),"</label><br/>")
	print("</div><div><br/><input type='submit'><input type='reset'></div></form></table>")
	cursor.close()
	connection.close()
	print("</p>")

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
