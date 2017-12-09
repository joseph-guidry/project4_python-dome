#!/usr/bin/env python3

import cgi
import getpass
import mysql.connector
import webpage

def get_data():
	""" Query database for battle data """
	login_name = getpass.getuser()  # Obtain user login name
	config = {"user": login_name, "database": login_name}
	connection = mysql.connector.connect(**config)
	
	sql_c1 = ("CREATE OR REPLACE VIEW c1 AS SELECT c.id, c.Name "
			"FROM combatant c, fight f WHERE c.id = f.combatant_one;")
	sql_c2 = ("CREATE OR REPLACE VIEW c2 AS SELECT c.id, c.Name "
			  "FROM combatant AS c, fight AS f WHERE c.id = f.combatant_two;")
	sql_c3 = ("CREATE OR REPLACE VIEW c3 AS SELECT DISTINCT c1.Name AS Name1,"
			  "c2.Name AS Name2, f.winner_id, f.start, f.finish "
			  "FROM fight AS f, c1, c2 "
			  "WHERE f.combatant_one = c1.id AND f.combatant_two = c2.id;")
	sql = ("SELECT * FROM c3;")

	cursor = connection.cursor()
	cursor.execute(sql_c1)
	cursor.execute(sql_c2)
	cursor.execute(sql_c3)
	cursor.execute(sql)

	#This needs to take the data form the data base and output it with HTML.
	names = [row for row in cursor.fetchall()]
	print("<p>")
	print("<table><form action='/cgi-bin/select_battle.py'>")
	print("<p>Select a Battle to view more details</p>\n<div>")

	for number, name in enumerate(names, 1):
		number = str(number)
		pid, date = [str(name[2]), name[4]]
		print("<input type='radio' id='battle", number,"' checked ")
		print("name='name'  value=\"",pid, ",", date,"\">")
		print("<label for='combatant", number, "'>", 
			  "Battle",number,"</label><br/>")

	print("</div><div><br/><input type='submit'>",
		  "<input type='reset'></div></form></table>",
		  "<a href='/battle/battle_list.html'>BACK</a>")
	print("</p>")
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
