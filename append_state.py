'''
Created on Jan 15, 2020

@author: ywkim
'''

import pandas as pd
from sys import argv


def city_state_country(coord):
    location = geolocator.reverse(coord, exactly_one=True)
    try:
        address = location.raw['address']
        city = address.get('city', '')
        state = address.get('state', '')
        country = address.get('country', '')
    except AttributeError:
        city = 'NA'
        state = 'NA'
        country = 'NA'

    return city, state, country

if __name__ == '__main__':
    parler_file = argv[1]
    df_parler = pd.read_csv(parler_file, header=None, names=['Longitude', 'Latitude', 'Timestamp', 'ID'])

    election_file = 'election_results.csv'
    df_election = pd.read_csv(election_file)

    state_list = []
    for lat, lng in zip(df_parler['Latitude'], df_parler['Longitude']):
        coord = str(lat) + ', ' + str(lng)
        city, state, country = city_state_country(coord)
        state_list.append(state)

    df_parler['State'] = state_list
    df_parler.drop(df_parler[df_parler['State'] == 'NA'].index, inplace=True)

    df = pd.merge(df_parler, df_election, how='inner', on='State')

    df.to_csv(parler_file + '_states.csv', index=False)