#!/usr/bin/env python3

import cgi
import mysql.connector
import getpass
import webpage

def get_data():

	default = ""
	fields = cgi.FieldStorage()
	cid = fields.getvalue("name", default)

	""" Query the database to gather data """
	login_name = getpass.getuser()  # Obtain user login name
	config = {"user": login_name, "database": login_name}
	connection = mysql.connector.connect(**config)
	
	sql = ("SELECT id, name FROM combatant WHERE id=%s;")
	cursor = connection.cursor()
	try:
		cursor.execute(sql,(cid,))

		names = [(row[0], row[1]) for row in cursor.fetchall()]
		#print(names[0][1])
		name = names[0][1]

		sql = ("SELECT c.Name, s.Name, s.Type, s.base_atk, s.base_dfn,"
				"s.base_hp FROM combatant AS c, species AS s "
				"WHERE c.id = s.id AND c.Name = %s;" )
		# print(sql)
		cursor.execute(sql, (name, ))	
		data = [row for row in cursor.fetchall()]
		
		print("<h2>Combatant Details</h2>")
	
		print("<div><table><tr><td>Combatant Name</td>")
		print("<td>Species</td><td>Species Type</td><td>Base Attack</td>")
		print("<td>Base Defense</td><td>Base Health Points</td></tr><tr>")
		#print(data)
		for item in data[0]:
			print("<td align='right'>",item,"</td>")
		print("</tr><tr>")
		print("</tr></table></div><br/><div>")
		print("<a href='/combatants/combatants_list.html'>BACK to Combatants</a><br/>")
		print("<a href='/cgi-bin/get_rankings.py'>BACK to Rankings</a><br/>")
		print("<a href='/index.html'>HOME</a>")
		
	
	except IndexError:
		print("<p>ERROR</p><br/>")
		print("<a href='/index.html'>HOME</a>")
	
	cursor.close()
	connection.close()

def main():
	stylesheets = ("<link rel='stylesheet' type='text/css' href='/css/tablestyle.css'>")
	webpage.htmlTop(stylesheets)
	get_data()
	webpage.htmlBottom()

if __name__=="__main__":
	try:
		main()
	except:
		cgi.print_exception()
