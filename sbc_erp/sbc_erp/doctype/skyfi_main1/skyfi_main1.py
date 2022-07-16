# Copyright (c) 2022, Surebiz Corporation and contributors
# For license information, please see license.txt


#from json import dump, load
import json
import os
from frappe import whitelist
# import frappe
from frappe.model.document import Document
import pyodbc
import itertools
server = "tcp:10.1.1.3"
database = "SWMGL_BE"
username = "sa"
password = "lipatko123!"
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

class SkyfiMain1(Document):
	def db_insert(self):
		d = self.get_valid_dict(convert_dates_to_str=True)
		#print(d)
		with open("data_file.json", "w+") as read_file:
			json.dump(d, read_file)
			print(json.dump(d, read_file))

	def load_from_db(self):
		#tsql="SELECT * from [dbo].[tblMain1] order by [VDate] DESC offset 10 ROWS fetch next 10 rows only FOR JSON AUTO"
		#cursor.execute(tsql)
		#listdata=cursor.fetchall()
		#desc = cursor.description
		#column_names = [col[0] for col in desc]
		#data = [dict(zip(column_names, row)) for row in cursor.fetchall()]
		#return  [listdata]
		with open("data_file.json", "r") as read_file:
			#print(os.path.abspath(read_file))
			#print(read_file)
			return json.load(read_file)

	def db_update(self):
		d = self.get_valid_dict(convert_dates_to_str=True)
		with open("data_file.json", "w+") as read_file:
			print(read_file)
			json.dump(d, read_file)

	@whitelist
	def get_list(self, args):
		with open("data_file.json", "r") as read_file:
			print(os.path.abspath(read_file))
			print(read_file)
			return [json.load(read_file)]

	def get_count(self, args):
		return [{'total_count':2}]
		#pass

	def get_stats(self, args):
		pass
