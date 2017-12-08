#!/usr/bin/env python3

def htmlTop():
	print("Content-type: text/html\n\n",
				"<!doctype html>",
			 	"<html>"
			 	"<head>",
					"\t<meta charset='UTF-8' />",
					"\t<title>TITLE PAGE</title>",
				"</head>",
				"<body>", sep="\n")

def htmlBottom():
	print("</body>",
			 "</html>", sep='\n')


