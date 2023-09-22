import datetime
import requests
import subprocess
import os
import win32print
import time


SHEET_LINK = 'https://www.printyourbrackets.com/images/WEEK'
PRINTER_NAME = "HP Smart Tank 6000 series [F6584A]"


def download_pdf(url, filename):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36'})
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print('PDF downloaded successfully.')
    else:
        print('Failed to download PDF. Status code:', response.status_code)


def printing():
    current_date = datetime.datetime.now()
    # if its tuesday
    if current_date.weekday() == 1:
        #get current week number
        nfl_week = get_nfl_week()
        current_sheet = SHEET_LINK + str(nfl_week) + '.pdf'
        sheet_file_name = str(nfl_week) + ".pdf"
        # if the sheet has been downloaded already
        if os.path.isfile(sheet_file_name):
            #dont do anything
            print("EXISTS")
        else: 
            #no file yet, download it and print 4
            download_pdf(current_sheet, sheet_file_name)
            pdf_file  = 'C:/Users/klayt/OneDrive/Desktop/sheets/' + sheet_file_name
            time.sleep(10)
            print_pdf3(pdf_file)
    else:
        print("not tuesday")

def print_pdf3(pdf_file):
    acrobat = 'C:/Program Files/Adobe/Acrobat DC/Acrobat/Acrobat.exe'
    name = win32print.GetDefaultPrinter()
    cmd = '"{}" /n /o /t "{}" "{}"'.format(acrobat, pdf_file, name)
    for i in range(5):
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def get_nfl_week():
    nfl_start_date = datetime.date(year=2023, month=9, day=5)
    current_date = datetime.date.today()
    week_number = ((current_date - nfl_start_date).days // 7) + 1
    return week_number

if __name__ == "__main__":
    printing()