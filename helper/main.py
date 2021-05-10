import os
import time
from snag import snagCourse

while(True):
	print("Checking course status:")
	result = snagCourse(os.environ["COURSESUBJECT"], os.environ["COURSENUMBER"], os.environ["COURSESECTION"], os.environ["EMAIL"])
	if(result == True):
		break;
	time.sleep(3600)

print("Done")