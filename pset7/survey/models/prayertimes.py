from datetime import datetime
import time
import pytz
import jsonpickle

class PrayerTimes():
    def __init__(self, organisationId, year, month, day):
        self.organisationId = organisationId
        self.date = datetime(year, month, day)

    def getFajr(self):
        if hasattr(self,"fajr"):
            if self.fajr is not None:
                return self.fajr.strftime("%H:%M")
        else:
            return None

    def setFajr(self, time):
        if not time:
            self.fajr = None
        else:
            self.fajr = self.stringToTime(time)
    #------------------------
    def getZuhr(self):
        if hasattr(self,"zuhr"):
            if self.zuhr is not None:
                return self.zuhr.strftime("%H:%M")
        else:
            return None

    def setZuhr(self, time):
        if not time:
            self.zuhr = None
        else:
            self.zuhr = self.stringToTime(time)
    #------------------------
    def getAsr(self):
        if hasattr(self,"magrib"):
            if self.asr is not None:
                return self.asr.strftime("%H:%M")
        else:
            return None

    def setAsr(self, time):
        if not time:
            self.asr = None
        else:
            self.asr = self.stringToTime(time)
    #------------------------
    def getMagrib(self):
        if hasattr(self,"magrib"):
            if self.magrib is not None:
                return self.magrib.strftime("%H:%M")
        else:
            return None

    def setMagrib(self, time):
        if not time:
            self.magrib = None
        else:
            self.magrib = self.stringToTime(time)
    #------------------------
    def getIsha(self):
        if hasattr(self,"isha"):
            if self.isha is not None:
                return self.isha.strftime("%H:%M")
        else:
            return None

    def setIsha(self, time):
        if not time:
            self.isha = None
        else:
            self.isha = self.stringToTime(time)

    # convert 12:00 to datetime
    def stringToTime(self, textualTimeString):
        if not textualTimeString:
            return None
        else:
            return datetime.strptime(textualTimeString,"%H:%M")

    def __str__(self):
        return " OrganisationId: {0} \n Date: {1} \n Fajr: {2} \n Zuhr: {3} \n Asr: {4} \n Magrib: {5} \n Isha: {6} \n".format(
            self.organisationId,
            self.date,
            self.getFajr(),
            self.getZuhr(),
            self.getAsr(),
            self.getMagrib(),
            self.getIsha()
        )