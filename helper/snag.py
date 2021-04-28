import requests
import os
from sendEmail import send_email
import time

def snagCourse(courseSubject, courseNumber, courseSection, email):
	r = requests.get('https://api.ubccourses.com/sectionInfo/{}/{}/{}?realtime=1'.format(courseSubject, courseNumber, courseSection))

	r_dict = r.json()

	if(r_dict['general_seats_remaining'] > 0):
		print("Sending email")
		send_email("Test", "Your course {}{} {} has an open spot!".format(courseSubject, courseNumber, courseSection), email)
		return True;
	else:
		return False;

while(True):
	print("Checking course status:")
	result = snagCourse(os.environ["COURSESUBJECT"], os.environ["COURSESUBJECT"], os.environ["COURSENUMBER"], os.environ["COURSESECTION"])
	if(result == True):
		break;
	time.sleep(3600)

print("Done")