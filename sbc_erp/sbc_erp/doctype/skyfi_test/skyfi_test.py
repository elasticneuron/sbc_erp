# Copyright (c) 2022, Surebiz Corporation and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import json

class skyfi_test(Document):
	
	def db_insert(self):
		pass

	def load_from_db(self):
		pass

	def db_update(self):
		pass

	def get_list(self, args):
		with open("data_file.json", "r") as read_file:
			return [json.load(read_file)]
		#pass

	def get_count(self, args):
		pass

	def get_stats(self, args):
		pass
