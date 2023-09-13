from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
import gspread
import gitlab
import time
import sys

# Authorize the API
scope = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file']
credentials = ServiceAccountCredentials.from_json_keyfile_name(sys.argv[1],scope)
client = gspread.authorize(credentials)

# Fetch GitLab data
gl = gitlab.Gitlab('https://gitlab.com/', private_token=sys.argv[2])
gl.auth()
group_id = 52238843
group = gl.groups.get(group_id)
members = group.billable_members.list(get_all=True)
size = len(members)

# Get today's date
today = date.today()

# Clear sheet
sheet = client.open('Usuários GitLab').sheet1

# Insert new gitlab data into sheet
for i in range(size):

    user = members[i].attributes
    str_last_login = user['last_login_at'][0:10]
    list_last_login = str_last_login.split('-')
    date_last_login = date(int(list_last_login[0]), int(list_last_login[1]), int(list_last_login[2]))

    sheet.update_cell(i+2, 1, user['id'])
    sheet.update_cell(i+2, 2, user['username'])
    sheet.update_cell(i+2, 3, user['name'])
    sheet.update_cell(i+2, 4, str_last_login + ' -> ' + str((today - date_last_login).days) + ' days ago')
    if i == 15 or i == 30 or i == 45 or i == 60 or i == 75 or i == 90:
        time.sleep(60)

if size >= 100:
    sheet.update_cell(1, 4, "Limite de 100 licenças alcançado")