import json

from django.shortcuts import render
from django.http import JsonResponse

from app.models import User,ActivityPeriods


def add_activities(userid):
	
	activty_list = []
	activities_qs = ActivityPeriods.objects.filter(user__id=userid)
	for single_activity in activities_qs:
		single_activity_dict = {
					"start_time": "",
					"end_time": ""
				}
		single_activity_dict["start_time"] =  single_activity.start_time
		single_activity_dict["end_time"] = single_activity.end_time
		activty_list.append(single_activity_dict)
	return activty_list

def make_format(data):
	final_format = {
			"ok": True,
			"members": []
	}
	for single_user in data:
		single_user_dict = {
				"id":'',
				"real_name":'',
				"tz":'',
				"activity_periods":'',
		}

		single_user_dict["id"] = single_user.id
		single_user_dict["real_name"] = single_user.real_name
		single_user_dict["tz"] = single_user.tz
		activty_list = add_activities(single_user.id)
		single_user_dict["activity_periods"] = activty_list
		final_format["members"].append(single_user_dict)

	return final_format


def get_data(request):
	data = {"succes":True}
	user_instance = User.objects.all().exclude(is_superuser=True)
	final_format = make_format(user_instance)
	return JsonResponse(final_format,safe=False)