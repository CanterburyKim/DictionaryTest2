from dict_example2 import *

users = ['kevin', 'daniel', 'xander']

for user in users:
    addy = get_email_for_user(user)
    print( f'the email address for {user} is : {addy}')
