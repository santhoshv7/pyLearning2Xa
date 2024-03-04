class Students():
    name = None
    phone_no = None

    def watch_recordings(self):
        print("recording watching")

    def do_assignments(self):
        print("do assignments")

class Course():
    title = None
    duration = None

    def daily_telecast(self):
        print("daily telecasting")
        
    def course_completion(self):
        print("certificates provided")

santhosh = Students()
pytat = Course()

santhosh.watch_recordings()
pytat.daily_telecast()