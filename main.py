from datetime import date
import pandas as pd
from mainfile import send_email

#enter you sheet id here
sheetid = "1ZztG6NsNY7APE9dKMPWRjRN6w93ooGE9K5MIso3b4c8"
#enter you sheet example id here^^^ (can be found in the link)
sheetname = "Sheet1"
#enter the sheet name (on the bottom of sheet)
url = f"https://docs.google.com/spreadsheets/d/{sheetid}/gviz/tq?tqx=out:csv&sheet={sheetname}"

def load_df(url):
    df = pd.read_csv(url)
    return df
print(load_df(url))
def send_emails(df):
    emailcount=0
    for _,row in df.iterrows():
        send_email(
            subject=f'Congrats, application number: {row["appno"]}',
            reciever_email=row["email"],
            name=row["name"],
            duedate=row["duedate"],
            appnumber=row["appno"],
            amount=row["amount"],
        )
        emailcount+=1
    return f"Total emails: {emailcount}"

#assign csv file instead of the google sheet if u want and skip the sheet link and load df step
df=load_df(url)
result=send_emails(df)
print(result)
