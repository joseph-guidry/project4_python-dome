#!/usr/bin/env python3

import cgi
import getpass
import mysql.connector
import webpage

def get_data():
	pass

def main():
	""" Driver for this webpage """
	stylesheets = ""
	webpage.htmlTop(stylesheets)
	get_data()
	print("hello")
	webpage.htmlBottom()

if __name__=="__main__":
	try:
		main()
	except:
		cgi.print_exception()
