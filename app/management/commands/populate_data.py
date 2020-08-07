# Python imports
import json
import os
# Django imports
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.hashers import make_password
#import project files
from app.models import User,ActivityPeriods

class Command(BaseCommand):
	help = 'Displays current time'

	def add_arguments(self, parser):
		parser.add_argument('json_file', type=str)

	def store_activity_data(self,user_instance,data):
		'''This function will store activty logs for specific user
			Args: data[list], list of dict(activty log)
				user_instance
		'''
		if data:
			for index,value in enumerate(data):
				ActivityPeriods.objects.create(
					user = user_instance,
					start_time = value.get("start_time"),
					end_time = value.get("end_time")
					)


	def store_user_data(self,data):
		'''this function will store json data into database'''
		for index,value in enumerate(data):
			user_instance = User.objects.create(
				username=value.get("real_name"),
				real_name=value.get("real_name"),
				password=make_password('123'),
				tz=value.get('tz'),
				id=value.get('id'),
				)
			self.store_activity_data(user_instance,value.get("activity_periods"))


	def handle(self, *args, **options):
		total = options['json_file']
		with open(total) as f:
			data_list = json.load(f)

		# get only user data from json	
		user_data =  data_list.get("members")

		if user_data:
			self.store_user_data(user_data)


		