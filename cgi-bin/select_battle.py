#!/usr/bin/env python3

import cgi
import mysql.connector
import getpass
import webpage

def get_data():

	# Retrieve the details of a battle that can be selected.
	sql1 = ("SELECT id, name FROM combatant WHERE id=%s;")
	sql2 = ("SELECT * from fight WHERE winner_id=%s AND finish=%s;")


	fields = cgi.FieldStorage()
	print("<p>")

	#print(fields)
	default =""

	cid = fields.getvalue("name", default)
	#print("<br/>", cid, "<br/>")
	input_data = cid.split(",")
	winner_id = input_data[0]
	date = input_data[1].strip()


	#print("<br/><br/><br/>")
	#print(winner_id)
	#print(date)
	#print("<br/><br/><br/>")
	""" Query the database to gather data """
	login_name = getpass.getuser()  # Obtain user login name
	config = {"user": login_name, "database": login_name}
	connection = mysql.connector.connect(**config)

	sql1 = ("SELECT id, name FROM combatant WHERE id=%s;")
	cursor = connection.cursor()
	cursor.execute(sql1,(input_data[0],))

	winner_name = [row[1] for row in cursor.fetchall()]

	print("<h1>WINNER: ", winner_name[0], "</h1>")
	print("<table>")
	print("<tr><th><h3>Battle Details</h3></th></tr>")

	sql2 = ("SELECT * FROM c3 WHERE winner_id=%s AND finish=%s;")
	#print(winner_id)
	#print(repr(date))

	#print("<br/><br/><br/>")
	cursor.execute(sql2, ( winner_id, date,) )
	something = [row for row in cursor.fetchall()]
	#print("word")
	#print(something)
	#print("<br/><br/><br/>")

	print("<tr><td>Match</td><td>", something[0][0] , "vs", something[0][1],"</td></tr>" )
	print("<tr><td>Start Time</td><td>", something[0][3] ,"</td></tr>" )
	print("<tr><td>End Time</td><td>", something[0][4] ,"</td></tr>" )
	print("</table>")

	cursor.close()
	connection.close()

	print("</p>")

	print("<a href='/index.html'>HOME</a>")
	print("<a href='/battle/battle_list.html'>BACK</a>")


def main():
	""" Driver to build battles detail html page """
	webpage.htmlTop()
	get_data()
	webpage.htmlBottom()

if __name__=="__main__":
	try:
		main()
	except:
		cgi.print_exception()
