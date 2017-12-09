#!/usr/bin/env python3

import getpass
import mysql.connector

def htmlTop(cssstyle):
	""" Create template for top of HTML page """
	print("Content-type: text/html\n\n"
				"<!doctype html>"
			 	"<html>"
			 	"<head>")
	print("{}".format(cssstyle))
	print("<meta charset='UTF-8'/><title>TITLE PAGE</title>",
		  "</head><body>")
	load_views()


def htmlBottom():
	print("</body>",
			 "</html>", sep='\n')

def load_views():
	""" Load views to ensure all are created prior to use """
	login_name = getpass.getuser()  # Obtain user login name
	config = {"user": login_name, "database": login_name}
	connection = mysql.connector.connect(**config)
	
	sql_c1 = ("CREATE OR REPLACE VIEW c1 AS SELECT c.id, c.Name "
			"FROM combatant c, fight f WHERE c.id = f.combatant_one;")
	sql_c2 = ("CREATE OR REPLACE VIEW c2 AS SELECT c.id, c.Name "
			  "FROM combatant AS c, fight AS f WHERE c.id = f.combatant_two;")
	sql_c3 = ("CREATE OR REPLACE VIEW c3 AS SELECT DISTINCT "
			  " c1.id AS c1_id,c1.Name AS Name1, c2.id AS c2_id, "
			  "c2.Name AS Name2, f.winner_id, f.start, f.finish "
			  "FROM fight AS f, c1, c2 "
			  "WHERE f.combatant_one = c1.id AND f.combatant_two = c2.id;")
	sql_c4 = ("CREATE OR REPLACE VIEW c4 AS "
			  "SELECT Name1 AS Name, COUNT(Name1) AS Wins FROM "
			  "((SELECT Name1 FROM c3 WHERE c1_id=winner_id) "
			  "UNION ALL "
			  "(SELECT Name2 FROM c3 WHERE c1_id=winner_id)) AS t1 "
			  "GROUP BY Name1;")

	cursor = connection.cursor()
	cursor.execute(sql_c1)
	cursor.execute(sql_c2)
	cursor.execute(sql_c3)
	cursor.execute(sql_c4)
	cursor.close()
	connection.close()


if __name__=="__main__":
	htmlTop()
	htmlBottom()
