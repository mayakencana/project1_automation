from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.cd import Cd
from modules.catalog import Catalog
import json
book1 = Book(
    'Title test',
    'Ini subject test',
    None,
    '1234-5674',
    'maya',
    '08769707658'
)

book2 = Book(
    'Title test',
    'Ini subject test',
    None,
    '1234-5674',
    'maya',
    '08769707658'
)

book3 = Book(
    'Title test',
    'Ini subject test',
    None,
    '1234-5674',
    'maya',
    '08769707658'
)

magazine1 = Magazine(
    'media cnn test',
    'edisi 14 juli 2023',
    None,
    'volume 4',
    '-'
)

magazine2 = Magazine(
    'media cbnc',
    'edisi 14 juli 2023',
    None,
    'volume 4',
    '-'
)

dvd1 = Dvd(
    'Dvd test',
    'Ini subject test',
    None,
    None,
    None,
    "comedy"
)
cd1= Cd(
    'Cd test',
    'Ini subject  cd test',
    None,
    "Mayaa"
)
#collect data per jenis
book=[book1,book2,book3]
magazine=[magazine1,magazine2]
dvd=[dvd1]
cd=[cd1]
#get data from json
f=open('files/catalog.json')
data_json=json.load(f)
#create objek from data json
for item in data_json:
    if item["source"]=='book':
        book.append(Book(
            title=item["title"],
            subject=item["subject"],
            upc=item["upc"],
            isbn=item["isbn"],
            authors=item["authors"],
            dds_number=item["dds_number"],
        ))
    elif item["source"]=='magazine':
        magazine.append(Magazine(
            title=item["title"],
            subject=item["subject"],
            upc=item["upc"],
            volume=item["volume"],
            issue=item["issue"],
        ))
    elif item["source"]=='dvd':
        dvd.append(Dvd(
            title=item["title"],
            subject=item["subject"],
            upc=item["upc"],
            actors=item["actors"],
            director=item["director"],
            genre=item["genre"],
        ))
    elif item["source"]=='cd':
        cd.append(Cd(
            title=item["title"],
            subject=item["subject"],
            upc=item["upc"],
            artist=item["artist"],
        ))
    

#collect all data
catalog_all=[book, magazine, dvd, cd]

input_search='test'


results= Catalog(catalog_all).search(input_search)
if results:
    for index, result in enumerate(results):
        print (f'result ke-{index+1}| {result}')
else:
    print('no result')