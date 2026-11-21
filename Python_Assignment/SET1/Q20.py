import logging
import sys


root = logging.getLogger()
root.setLevel(logging.WARNING)

rh = logging.StreamHandler(sys.stdout)
rh.setFormatter(
    logging.Formatter("ROOT|%(levelname)s|%(name)s|%(message)s")
)
root.addHandler(rh)


app = logging.getLogger("app")
db = logging.getLogger("app.db")

ah = logging.StreamHandler(sys.stdout)
ah.setLevel(logging.INFO)
ah.setFormatter(logging.Formatter("APP|%(message)s"))
app.addHandler(ah)


db.info("one")
db.warning("two")

app.setLevel(logging.DEBUG)
db.debug("three")

print("-- propagate off --")

db.propagate = False
db.error("four")

print("-- done --")
#SOLUTION
four
APP|two
ROOT|WARNING|app.db|two
ROOT|DEBUG|app.db|three
-- propagate off --
-- done --

Process finished with exit code 0
