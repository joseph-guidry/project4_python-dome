#!/usr/bin/env python3

import cgi
import mysql.connector
import getpass
import webpage

def get_data():
	""" Build the battle details html page """
	fields = cgi.FieldStorage()

	cid = fields.getvalue("name", "")
	input_data = cid.split(",")
	winner_id = input_data[0]
	date = input_data[1].strip()

	""" Query the database to gather data """
	login_name = getpass.getuser()  # Obtain user login name
	config = {"user": login_name, "database": login_name}
	connection = mysql.connector.connect(**config)

	sql1 = ("SELECT id, name FROM combatant WHERE id=%s;")
	cursor = connection.cursor()
	try:
		cursor.execute(sql1,(input_data[0],))

		winner_name = [row[1] for row in cursor.fetchall()]

		print("<h1>WINNER: ", winner_name[0], "</h1>")
		print("<table>")
		print("<tr><h3>Battle Details</h3></tr>")

		sql2 = ("SELECT * FROM c3 WHERE winner_id=%s AND finish=%s;")
		cursor.execute(sql2, ( winner_id, date,) )

		# Unpack the data 
		something = [row for row in cursor.fetchall()]
		pid1, pname1, pid2, pname2, wid, start, end = something[0]

		print("<tr><td>Match</td><td>", pname1, "vs",pname2,"</td></tr>" )
		print("<tr><td>Start Time</td><td>", start ,"</td></tr>" )
		print("<tr><td>End Time</td><td>", end ,"</td></tr>" )
		print("</table>")

		cursor.close()
		connection.close()


		print("<div><a href='/index.html'>HOME</a>")
		print("<a href='/battle/battle_list.html'>BACK</a></div>")

	except IndexError:
		print("<p>ERROR</p><br/>")
		print("<a href='/index.html'>HOME</a>")


def main():
	""" Driver to build battles detail html page """
	stylesheets = "<link rel='stylesheet' href='/css/tablestyle.css'>"
	webpage.htmlTop(stylesheets)
	get_data()
	webpage.htmlBottom()

if __name__=="__main__":
	try:
		main()
	except:
		cgi.print_exception()
