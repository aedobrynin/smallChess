import sqlite3

from config import resourcePath


class Statistics():
    def __init__(self, pathToDatabase):
        self.dbPath = pathToDatabase
        self.con = sqlite3.connect(resourcePath(self.dbPath))

    def __del__(self):
        self.con.close()

    def getStatistics(self, fields=('*', )):
        requestForm = """SELECT {} FROM Players"""
        request = requestForm.format(", ".join(fields))

        cur = self.con.cursor()
        statistics = cur.execute(request).fetchall()

        return statistics

    def getPlayersList(self):
        cur = self.con.cursor()
        playersList = cur.execute("""SELECT id, nickname
FROM Players""").fetchall()

        return playersList

    def getPlayersData(self, playerId, fields=('*',)):
        requestForm = """SELECT {} FROM Players
WHERE id = ?"""
        request = requestForm.format(", ".join(fields))

        cur = self.con.cursor()
        data = cur.execute(request, (playerId, )).fetchone()

        return data

    def getColumnNames(self):
        cur = self.con.cursor()
        cur = self.con.execute("SELECT * FROM Players")
        columnNames = tuple(descr[0] for descr in cur.description)

        return columnNames

    def addPlayer(self, nickname):
        cur = self.con.cursor()
        cur.execute("""INSERT INTO Players(nickname) VALUES (?)""",
                    (nickname, ))
        self.con.commit()

    def deletePlayer(self, playerId):
        cur = self.con.cursor()
        cur.execute("""DELETE FROM Players WHERE id = ?""",
                    (playerId, ))
        self.con.commit()

    def updatePlayersData(self, playerId, fieldValues):
        """Updates player with playerId statistics.
           fieldValues shoud be tuple of pairs (field, value).
           For example (("nickname", "newNickname"), )"""

        requestForm = """UPDATE Players
SET {}
WHERE id = ?"""
        dataChanges = ("{} = '{}'".format(field, value)
                       for field, value in fieldValues)
        request = requestForm.format(",\n    ".join(dataChanges))

        cur = self.con.cursor()
        cur.execute(request, (playerId, ))
        self.con.commit()
