__author__ = 'OliPicard'
import requests
import requests.exceptions
import json
import sys

''' A simple live data view of the national rail london stations.
    Developed by OliPicard (github.com/olipicard)
    This program is licenced under the GNU GPL 3.0 licence,
    a copy of the licence has been enclosed with the program.
    Please report any bugs via the github page - github.com/olipicard/ukstationlive
'''

def settings():  # grabbing settings from config.json.
    try:
        config = json.loads(open('config.json').read())
        if len(config['url']) == 0:
            print("Please edit your config.json file to include the proxy URL.")
            input("Press any key to terminate this application.")
            sys.exit()
        if len(config['accessToken']) == 0:
            print("Please edit your config.json file to include your own National Rail API key.")
            input("Press any key to terminate this application.")
            sys.exit()
        if len(config['nrsa']) == 0:
            print('Please edit your config.json file to include the NRSA URL.')
            input("Press any key to terminate this application.")
        if len(config['nrsd']) == 0:
            print('Please edit your config.json file to include the NRSD URL.')
            input("Press any key to terminate this application.")
    except IOError:  # throw an exception if the json cannot be loaded.
        print("Json failed to load. terminating application")
        sys.exit()
    return config

def station_info(station):
    localconfig = settings()
    URI = localconfig['url']  # Proxy URL for Huxley
    accessToken = localconfig['accessToken']  # API token
    nrsa = localconfig['nrsa']   # national rail arrivals
    nrsd = localconfig['nrsd']   # national rail departures.
    payload = URI+station+accessToken
    try:
        json_object = requests.get(payload)  # grab huxley payload
        gopher = json_object.status_code  # gopher is a fail safe if huxley is down.
        if gopher == 200:
            dataq = json_object.json()
        elif gopher == 403:
            print('Error 403: Oh No, It seems the proxy is refusing connections. please look at the proxy logs.')
            sys.exit()
        elif gopher == 404:
            print('Error 404: Oh No, the page is unavailable at the moment. please check the proxy')
            sys.exit()
    except requests.exceptions.MissingSchema:
        print(' It seems the site has been modified. ')
        sys.exit()
    except requests.exceptions.Timeout:
        print('It seems the API is timing out. Please try again later.')
        sys.exit()
    if dataq['trainServices'] is None:
        input("No Station Services run from this terminal.")
        sys.exit()
    if dataq['nrccMessages'] is not None:  # Experimental: Checking for National Rail National Wide messages.
            for messages in dataq['nrccMessages']:
                print(messages['value'])
    if dataq['platformAvailable'] is not False:  # Experimental: Checking for services at station.
        print('-------------------------')
        print("This station is: %s" % dataq['locationName'])
        print('-------------------------')
        for train_service in dataq['trainServices']:
            a = train_service['origin'][0]['locationName']
            b = train_service['sta']
            c = train_service['std']
            e = train_service['platform']
            f = train_service['destination'][0]['locationName']
            g = train_service['operator']
            k = train_service['etd']
            u = train_service['eta']
            print('This train came from: %s' % a)
            if b is not None:
                print('Scheduled time of Arrival: %s' % b)
            if k == 'On time':
                print("Arrival Status: %s " % k)
            elif k == 'Delayed':
                print(k)
            elif k == 'Cancelled':
                print(k)
            if e is not None:
                print('On platform: %s' % e)
            if c is not None:
                print('Scheduled Departure: %s' % c)
            if u == 'On time':
                print("Departure Status: %s" % u)
            elif u == 'Delayed':
                print(u)
            elif k == 'Cancelled':
                print(u)
            print('This train is terminating at: %s' % f)
            print('The operator of the service: %s' % g)
            print('----------------------')
    else:
        print("Services are currently not available from this station.")
        input('Press any key to terminate this application.')
        sys.exit()
    print('National Rail Enquires Arrivals: ' + nrsa + station.lower())
    print('National Rail Enquires Departures: ' + nrsd + station.lower())
    input('Press [enter] to return back to the main menu.')


def menu():
    print('----------------------------------------------')
    print('Welcome to the UK Station Live platform service')
    print('If you need help, at the main menu type help.')
    print('This program is licenced under the GNU GPL 3.0 licence')
    print('Feel free to report any bugs via our github page.')
    print('---------------------------------------------')


def main():
    menu()
    words = input(' ').lower()
    pload = 'https://s3-eu-west-1.amazonaws.com/ukstationlive/stations.json'  # The CSR codes are stored on S3.
    try:
        shawn_json_object = requests.get(pload)
        grab = shawn_json_object.status_code
        if grab == 200:
            stations = shawn_json_object.json()
        elif grab == 403:
            print("error 403: The json file is currently unavailable, Please try again in a few minutes.")
            input("Press any key to terminate this application.")
            sys.exit()
        elif grab == 404:
            print("error 404: The json file is currently unavailable, Please try again in a few minutes.")
            input("Press any key to terminate this application.")
            sys.exit()
    except requests.exceptions.Timeout:
        print('The JSON station codes are not being loaded. (Timeout)\n This could be down to the file being updated.')
        print('Or it could be an outage with S3 (EU West 1). Check AWS page for any service updates.')
        input('press any key to terminate this application.')
        sys.exit()
    try:
        if words == "quit":
            sys.exit()
        elif words == "exit":
            sys.exit()
        elif words == "credits":
            print('Developed with love by OliPicard')
        elif words == "help":
            print('Welcome to the help center')
            print('Please be connected to the internet when using the service.')
            print('Simply type in the station at the main menu to get the latest updates.')
            print('e.g Ashford International Eurostar')
            print('Other Commands')
            print('Quit - Terminates the application.')
            print('Exit - Terminates the application.')
            print('Credits - displays the credits')
            print('Help - brings up this helpful menu!')
        else:
            station_info(stations[words])
    except KeyError:
        print('It seems you have attempted to enter an invalid key. Please type help for a list of commands.')


while __name__ == "__main__":
    main()