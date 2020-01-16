from .prayer import Prayer

class DisplayBoard():

    def __init__(self):
        self.prayers = []

        self.prayers.append(Prayer("BEGIN FAJR"))
        self.prayers[0].display_name = "Being Fajr"

        self.prayers.append(Prayer("FAJR"))
        self.prayers[1].display_name = "Fajr"

        self.prayers.append(Prayer("DAHWAEKUBRA"))
        self.prayers[2].display_name = "Dahwa e Kubra"

        self.prayers.append(Prayer("BEGIN ZUHR"))
        self.prayers[3].display_name = "Begin Zuhr"

        self.prayers.append(Prayer("ZUHR"))
        self.prayers[4].display_name = "Zuhr"

        self.prayers.append(Prayer("BEGIN ASR"))
        self.prayers[5].display_name = "Begin Asr"

        self.prayers.append(Prayer("ASR"))
        self.prayers[6].display_name = "Asr"

        self.prayers.append(Prayer("MAGRIB"))
        self.prayers[7].display_name = "Magrib"

        self.prayers.append(Prayer("BEGIN ISHA"))
        self.prayers[8].display_name = "Begin Isha"

        self.prayers.append(Prayer("ISHA"))
        self.prayers[9].display_name = "Isha"

        self.prayers.append(Prayer("JUMMAH ONE"))
        self.prayers[10].display_name = "Jummah One"

        self.prayers.append(Prayer("JUMMAH TWO"))
        self.prayers[11].display_name = "Jummah Two"


