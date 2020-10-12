from datetime import datetime

with open("cron.log", "a") as log:
    log.write("Tâche cron lancée : " + str(datetime.now()))
