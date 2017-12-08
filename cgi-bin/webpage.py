#!/usr/bin/env python3

def htmlTop(cssstyle=" "):
	print("Content-type: text/html\n\n",
				"<!doctype html>",
			 	"<html>"
			 	"<head>")
	print("{}".format(cssstyle))
	print("\t<meta charset='UTF-8' />",
					"\t<title>TITLE PAGE</title>",
				"</head>",
				"<body>")
	

def htmlBottom():
	print("</body>",
			 "</html>", sep='\n')

if __name__=="__main__":
	htmlTop()
	htmlBottom()
