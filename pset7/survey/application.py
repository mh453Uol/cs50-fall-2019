import cs50
from datetime import datetime
import calendar
import json
import jsonpickle

from models.prayertimes import PrayerTimes
from models.display_board import DisplayBoard

from db.persistence import save_prayertimes, get_prayertimes, save_display_board, get_display_board

from flask import Flask, jsonify, redirect, render_template, request, Response

# Configure application
app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_index():
    return render_template("index.html")


@app.route("/prayertime", methods=["GET"])
def prayertime_index():
    month = datetime.now().month
    return redirect("/prayertime/{0}".format(month))


@app.route("/prayertime/<int:month>", methods=["GET"])
def prayertime(month):

    now = datetime.now()

    prayerTimes = get_prayertimes('majid',month)

    model = {
        'prayers': prayerTimes,
        'month': calendar.month_name[month],
        'monthIndex': month,
        'year': now.year
    }

    return render_template("form.html", model=model)


@app.route("/form", methods=["POST"])
def post_prayertime():
    month = int(request.form.get("monthIndex"))
    year = int(request.form.get("year"))
    daysInMonth = calendar.monthrange(year, month)[1]

    fajr = request.form.getlist("jamaatFajr[]")
    zuhr = request.form.getlist("jamaatZuhr[]")
    asr = request.form.getlist("jamaatAsr[]")
    magrib = request.form.getlist("jamaatMagrib[]")
    isha = request.form.getlist("jamaatIsha[]")

    prayerTimes = []
    prayerTime = None

    for day in range(daysInMonth):
        prayerTime = PrayerTimes(1, year, month, day + 1)

        if day < len(fajr):
            prayerTime.setFajr(fajr[day])

        if day < len(zuhr):
            prayerTime.setZuhr(zuhr[day])

        if day < len(asr):
            prayerTime.setAsr(asr[day])

        if day < len(magrib):
            prayerTime.setMagrib(magrib[day])

        if day < len(isha):
            prayerTime.setIsha(isha[day])

        prayerTimes.append(prayerTime)

    save_prayertimes("majid", month, prayerTimes)

    return redirect("/prayertime/{0}".format(month))


@app.route("/display_board", methods=["POST"])
def set_display_board():
    organisation = request.form.get("organisation")
    times = request.form.getlist("time[]")
    is_displayed = request.form.getlist("is_displayed[]")

    displayBoard = DisplayBoard()

    for i in range(len(times)):
        prayer = displayBoard.prayers[i]

        prayer.set_time(times[i])
        prayer.is_displayed_to_user(True if is_displayed[i] is '1' else False)

    save_display_board("majid", displayBoard)

    return redirect("/display_board/{0}".format(organisation))


@app.route("/display_board/<organisation>", methods=["GET"])
def get_display_board_view(organisation):
    print(organisation)

    displayBoard = get_display_board(organisation)

    model = {
        'display': displayBoard,
        'organisation': organisation
    }


    return render_template("display_board.html", model=model)

