import os
import datetime
print("\x1B[9m \x1B[40m \x1B[32m")
os.system("git remote remove upstream")


def load():
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2023, 12, 1)
    delta = datetime.timedelta(days=1)
    while (start_date <= end_date):
        start_date +=delta
        mydate = start_date.strftime('%a %d %b %Y')
        print(mydate) 
        os.system("git add .")
        os.system("git commit --date=\"{} 10:00 2022 +0500\" -m hack-git-commit".format(mydate))

load()

os.system("git push -f origin master")