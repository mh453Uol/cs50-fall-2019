from os import path
from datetime import datetime
import calendar
import jsonpickle

from models.prayertimes import PrayerTimes
from models.display_board import DisplayBoard

def save_prayertimes(organisation, monthIndex, prayerTimes):
    file = "prayer-times/{0}.json".format(organisation)
    month = calendar.month_name[monthIndex]

    exists = path.isfile(file)
    data = {
        month: prayerTimes
    }

    if not exists:
        # just write all month prayer times to file
        with open(file, "w") as wfile:
            rawJsonString = jsonpickle.encode(data);
            wfile.write(rawJsonString)
    else:
        # have to update prayer time so read, update then write
        # we read all the content of the file into memory however thats fine since
        # at most it can be 40 KB
        yearPrayerTimes = {}
        rawJsonString = ''

        with open(file, "r") as rfile:
            rawJsonString = rfile.read()
            yearPrayerTimes = jsonpickle.decode(rawJsonString)

        yearPrayerTimes[month] = data[month]

        #print(yearPrayerTimes)

        with open(file, "w") as wfile:
            rawJsonString = jsonpickle.encode(yearPrayerTimes)
            wfile.write(rawJsonString)


def get_prayertimes(organisation, monthIndex):
    now = datetime.now()

    file = "db/prayer-times/{0}.json".format(organisation)
    exists = path.isfile(file)

    prayerTimes = []

    if not exists:
        # return prayer times for the month
        daysInMonth = calendar.monthrange(now.year, monthIndex)[1]

        for day in range(daysInMonth):
            prayerTimes.append(PrayerTimes(1, now.year, monthIndex, day + 1))
    else:
        # deserialize json to prayertime object
        month = calendar.month_name[monthIndex]

        with open(file, "r") as rfile:
            rawJsonString = rfile.read()
            prayerTimes = jsonpickle.decode(rawJsonString)

            # if we dont have prayer times for the month just create them
            if month in prayerTimes:
                prayerTimes = prayerTimes[month]
            else:
                daysInMonth = calendar.monthrange(now.year, monthIndex)[1]

                prayerTimes = []

                for day in range(daysInMonth):
                    prayerTimes.append(PrayerTimes(1, now.year, monthIndex, day + 1))

    return prayerTimes

def save_display_board(organisationId, displayBoard):

    # if path doesnt exist then:
    #   - create a file i.e {organisation}-board
    #   - add the times, is displayed for each of the prayers
    #       - so DisplayBoard.prayers.foreach
    # if path exists:
    #   - load file into memory
    #   - update the times and if prayer is displayed

    file = "db/display_board/{0}.json".format(organisationId)

    # just write all day prayer times to file
    with open(file, "w") as wfile:
        rawJsonString = jsonpickle.encode(displayBoard);
        wfile.write(rawJsonString)


def get_display_board(organisationId):

    file = "db/display_board/{0}.json".format(organisationId)
    displayBoard = None

    with open(file,"r") as rfile:
        rawJsonString = rfile.read()
        displayBoard = jsonpickle.decode(rawJsonString)

    return displayBoard