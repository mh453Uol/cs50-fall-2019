from datetime import datetime

class Prayer():

    def __init__(self, name):
        self.name = name
        self.time = datetime.now()
        self.is_displayed = True
        self.display_name = name

    def is_displayed_to_user(self, hidden):
        self.is_displayed = hidden

    def set_display_name(self, name):
        self.display_name = name

    def set_time(self, time):
        if not time:
            self.time = None
        else:
            self.time = datetime.strptime(time,"%H:%M")

    def get_time(self):
        if hasattr(self,"time"):
            if self.time is not None:
                return self.time.strftime("%H:%M")
        else:
            return None

    def __str__(self):
        return "name: {0} \n time: {1} \n is_displayed: {2} \n display_name: {3}".format(
            self.name,
            self.time,
            self.is_displayed,
            self.display_name
        )




