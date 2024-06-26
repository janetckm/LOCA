import csv
import requests

api_key = '430df319'

imdb_ids = [ 'tt0212712',
 'tt0118694',
 'tt0380069',
 'tt0286112',
 'tt0092263',
 'tt0338564',
 'tt1988689',
 'tt0188766',
 'tt0118694',
 'tt0338564',
 'tt0266067',
 'tt0380069',
 'tt0338564',
 'tt0338565',
 'tt0113672',
 'tt0395991',
 'tt0109424',
 'tt0109424',
 'tt0104684',
 'tt0455151',
 'tt0286635',
 'tt0093435',
 'tt2199429',
 'tt2332707',
 'tt6878882',
 'tt3923024',
 'tt5847286',
 'tt2165735',
 'tt5291094',
 'tt7245176',
 'tt7131870',
 'tt0338564',
 'tt2165505',
 'tt1726220',
 'tt3141320',
 'tt6869538',
 'tt5866930',
 'tt7183578',
 'tt7183578',
 'tt7183578',
 'tt10944634',
 'tt10530176',
 'tt7070530',
 'tt0097244',
 'tt0455195',
 'tt0286112',
 'tt0116456',
 'tt0382625',
 'tt3705760',
 'tt2332707',
 'tt1663189',
 'tt0491244',
 'tt0299977',
 'tt8459250',
 'tt1489428',
 'tt2197299',
 'tt7057652',
 'tt0105864',
 'tt0338564',
 'tt0105679',
 'tt3144180',
 'tt0113651',
 'tt10667354',
 'tt0089374',
 'tt0068767',
 'tt0111512',
 'tt0992911',
 'tt7245176',
 'tt0463985',
 'tt6427662',
 'tt0116456',
 'tt0178235',
 'tt0367837',
 'tt0098691',
 'tt0136317',
 'tt0439630',
 'tt0101258',
 'tt0102735',
 'tt0112913',
 'tt7521904',
 'tt1663189',
 'tt4738154',
 'tt0119217',
 'tt0365847',
 'tt0100777',
 'tt1602479',
 'tt0117905',
 'tt0096461',
 'tt0373074',
 'tt3469568',
 'tt0113672',
 'tt17504220',
 'tt17504220',
 'tt0299977',
 'tt0093978',
 'tt0385004',
 'tt0114996',
 'tt0112913',
 'tt0099426',
 'tt0913968',
 'tt0796212',
 'tt0338564',
 'tt2008006',
 'tt5355536',
 'tt5151488',
 'tt0992966',
 'tt0085127',
 'tt0093258',
 'tt0338564',
 'tt1462900',
 'tt0093258',
 'tt1602572',
 'tt0108611',
 'tt0089374',
 'tt0338564',
 'tt0109424',
 'tt0338564',
 'tt0105864',
 'tt1663189',
 'tt0117905',
 'tt0068935',
 'tt0080179',
 'tt0118694',
 'tt5866930',
 'tt0446059',
 'tt0113326',
 'tt0054357',
 'tt0097202',
 'tt0092263',
 'tt0178998',
 'tt2186715',
 'tt0118694',
 'tt0097202',
 'tt11463680',
 'tt0105864',
 'tt0111770',
 'tt0365717',
 'tt5292986',
 'tt1220719',
 'tt0220580']  

rating_data = []

for imdb_id in imdb_ids:
    url = f'http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        movie_data = response.json()
        rating = movie_data.get('imdbRating')
        rating_data.append({'IMDb ID': imdb_id, 'Rating': rating})

filename = 'imdb_ratings.csv'

with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['IMDb ID', 'Rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(rating_data)
    