from flask import Flask,request,Response,render_template,redirect,url_for,make_response
import plivo

from models import get_all_conference,create_conference,get_mobile,get_record

from helper import rent_number,generate_pin

from config_parser import get_config

configs=get_config()

app=Flask(__name__)

app.debug=True

CALLER_ID="19095002259"

BASE_URL='http://conference-call.herokuapp.com'

plivo_api=plivo.RestAPI(configs["AUTH_ID"],configs["AUTH_TOKEN"])



def notify(message,mobile):
	response=plivo_api.send_message({'src':CALLER_ID,
				'dst':mobile,
				'text':message,
				'type':'sms'
				})
	return response

@app.route('/')

def index():
	return render_template('index.html',
			conferences=get_all_conference()
				)


@app.route('/create')

def create():
	subject=request.args.get('subject','')
	phone=request.args.get('phone','')
	record_value=request.args.get('record','')
	record=False
	members=[]
	try:
		members.append(int(request.args.get('member0','')))
		members.append(int(request.args.get('member1','')))
	except:
		pass
	if record_value=="on":
		record=True
	print members
	conference_number=rent_number(plivo_api)
	conference_pin=generate_pin(conference_number)
	create_conference(subject,phone,members,record,conference_number,conference_pin)
	message="Hi, you can join the conference by dialing %s and the pin number being %s" %(conference_number,conference_pin)
	for member in members:
		response=notify(message,member)
		print response

	return "Conference created and members notified"




@app.route('/conference')

def conference():
	response=plivo.Response()
	response.addSpeak("Welcome to conference,Please enter your four digit pin code")

    	getdigits = response.addGetDigits(
    	    action=BASE_URL+url_for('verify_pin'),
	    method="GET",
    	    timeout='15',
    	    finishOnKey='#'
    	)
    	response.addSpeak(body="Input not received. Thank you.")
    	xml_response = make_response(response.to_xml())
    	xml_response.headers["Content-type"] = "text/xml"
    	return xml_response

@app.route('/verify_pin')

def verify_pin():
	pin=request.args.get('Digits','')
	conference_number=request.args.get('To','')
	response=plivo.Response()
	record_value=False
	if pin!=generate_pin(conference_number):

		response.addSpeak("Such a conference does not exist, please try again with a valid conference pin")
		response.addHangup()
	else:
		if get_record(conference_number):
			record_value=True
		response.addConference(body='plivo',
				       action= BASE_URL+url_for('submit_recording'),
				       method='GET',
				       record=record_value)
	xml_response=make_response(response.to_xml())
	xml_response.headers["Content-type"]="text/xml"
	return xml_response 
@app.route('/submit/record')

def submit_recording():
	record_url=request.args.get('RecordUrl','')
	conference_number=request.args.get('To','')
	print record_url
	message="The recording of your conference call is available at %s. Thanks for using Plivo" %(record_url)
	mobile=get_mobile(conference_number)
	response=notify(message,mobile)
	print response
	return "Success"


if __name__=='__main__':
	app.run()
