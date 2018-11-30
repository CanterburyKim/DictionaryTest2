import os

my_dir = os.path.dirname(os.path.realpath(__file__))

# Code to prepare an email to send

def get_email_for_user(selected_user):
    """
    takes in a username and then returns the associated
    email address for that user
    """
    email_address = ''

    if selected_user == 'daniel':
        email_address = 'danthemonkey@foo.bar'
    elif selected_user == 'kevin':
        email_address = 'kbabay@frenetic.com'
    elif selected_user == 'xander':
        email_address = 'xmarksthexander@whitehouse.gov'
    elif selected_user == 'nikita':
        email_address = 'nikitahasahat@notrussia.ru'
    elif selected_user == 'alex':
        email_address = 'aleoraxe@toronto.ca'

    """
    # TODO #1: add the following email addresses:

    joe: joejoesfantasticworld@joe.jo
    tyler: tythison@myworld.com
    david: dave@ruinthegame.com
    leo: thelion@leo.net

    """

    return email_address


# TODO: #2 create a dictionary and then replace the if-else block with dictionary lookup
