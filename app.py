from flask import Flask,request,Response,render_template,redirect,url_for,make_response
import plivo
app=Flask(__name__)
app.debug=True
CONFERENCE_PIN='1235'
BASE_URL='http://conference-call.herokuapp.com'
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
	response=plivo.Response()
	if pin != CONFERENCE_PIN:
		response.addSpeak("Such a conference does not exist, please try again with a valid conference pin")
		response.addHangup()
	else:
		response.addConference(body='plivo')
	xml_response=make_response(response.to_xml())
	xml_response.headers["Content-type"]="text/xml"
	return xml_response 











if __name__=='__main__':
	app.run()
