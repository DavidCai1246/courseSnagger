import requests
from helper.sendEmail import send_email

def snagCourse(courseSubject, courseNumber, courseSection, email):
	url = 'https://api.ubccourses.com/sectionInfo/{}/{}/{}?realtime=1'.format(courseSubject, courseNumber, courseSection)
	r = requests.get(url)
	print("Calling: {}".format(url))
	r_dict = r.json()
	print("The current total seats remaining is: {}", r_dict['total_seats_remaining'])

	if(r_dict['total_seats_remaining'] > 0):
		print("Sending email")
		send_email("Test", "Your course {}{} {} has an open spot!".format(courseSubject, courseNumber, courseSection), email)
		return True;
	else:
		return False;
