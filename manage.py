import os
from flask.ext.script import Manager

from finder.models import Bootcamp
from finder.database import session

from finder import app

manager = Manager(app)

@manager.command
def run():
	list_of_all_bootcamps = Bootcamp(name="devbootcamp", description="sdfsdfdfssdfsdf alksdjflasdjf asdjkfasd ")
	session.add(list_of_all_bootcamps)
	session.commit()
	return list_of_all_bootcamps

    # list_of_all_bootcamps = ["dev bootcamps", "Metis", "makersquare"]

if __name__ == "__main__":
    manager.run()