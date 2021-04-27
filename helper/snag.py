import requests
from sendEmail import send_email

def snagCourse(courseSubject, courseNumber, courseSection, email):
	r = requests.get('https://api.ubccourses.com/sectionInfo/{}/{}/{}?realtime=1'.format(courseSubject, courseNumber, courseSection))

	r_dict = r.json()

	if(r_dict['general_seats_remaining'] > 0):
		print("Sending email")
		send_email("Test", "Your course {}{} {} has an open spot!".format(courseSubject, courseNumber, courseSection), email)