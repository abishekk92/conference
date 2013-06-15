def get_appid(plivo_api,app_name="Conference Call"):
	for application in plivo_api.get_applications()[1]['objects']:
		if application['app_name'] == app_name:
			app_id=application['app_id']
	return app_id

def rent_number(plivo_api,app_name="Conference Call"):
	app_id=get_appid(plivo_api,app_name)
	response=plivo_api.get_number_group({"country_iso":"US","region":"california"})
	group_id=response[1]["objects"][0]["group_id"]
	response=plivo_api.rent_from_number_group({"group_id":group_id,"app_id":app_id})
	number=response[1]["numbers"][0]["number"]
	return number
def generate_pin(conference_number):
	numbers=list(conference_number)
	conference_pin="".join(map(lambda pair: str(reduce(lambda pair_a,pair_b:int(pair_a)+int(pair_b),pair)),zip(numbers[::2],numbers[1::2])))[:4]
	return conference_pin


