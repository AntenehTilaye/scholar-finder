from scholarly import scholarly

# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('Ketema Adere')
author = scholarly.fill(next(search_query))
pubs = []

if("Adama Science and Technology University".strip().lower() in author['affiliation'].strip().lower()):
    for pub in author['publications']:
        
        if("pub_year" in pub["bib"].keys()):

            one = {"name": author['name'],
                    "paper_id": pub["author_pub_id"],
                    "affiliation": author['affiliation'],
                    "title": pub["bib"]["title"],
                    "year": pub["bib"]["pub_year"],
                    "journal": pub["bib"]["citation"],
                    "citation_count": pub["num_citations"],
                    "authors": author['name'],
                    }
            
            pubs.append(one)

print(pubs)
print(len(pubs))

# # Print the titles of the author's publications
# print([pub['bib'] for pub in author['publications']])

# {'container_type': 'Author', 'filled': ['basics', 'indices', 'counts', 'coauthors', 'publications', 'public_access'], 
#  'source': <AuthorSource.SEARCH_AUTHOR_SNIPPETS: 'SEARCH_AUTHOR_SNIPPETS'>, 'scholar_id': 'sz943bMAAAAJ', 
# 'url_picture': 'https://scholar.google.com/citations?view_op=medium_photo&user=sz943bMAAAAJ', 
# 'name': 'Yadeta Chemdesa Chemeda', 'affiliation': 'Adama Science and Technology University', 'email_domain': '@astu.edu.et', 'interests': [], 
# 'citedby': 159, 'citedby5y': 121, 'hindex': 4, 'hindex5y': 4, 'i10index': 3, 'i10index5y': 3, 
# 'cites_per_year': {2015: 9, 2016: 5, 2017: 8, 2018: 15, 2019: 18, 2020: 14, 2021: 22, 2022: 31, 2023: 27, 2024: 9}, 
# 'coauthors': [], 
# 'publications': [{'container_type': 'Publication', 'source': <PublicationSource.AUTHOR_PUBLICATION_ENTRY: 'AUTHOR_PUBLICATION_ENTRY'>, 'bib': {'title': 'Influence of hydrated lime on the surface properties 
# and interaction of kaolinite particles', 'pub_year': '2015', 'citation': 'Applied Clay Science 107, 1-13, 2015'}, 'filled': False, 'author_pub_id': 'sz943bMAAAAJ:W7OEmFMy1HYC', 'num_citations': 69, 'citedby_url': 'https://scholar.google.com/scholar?oi=bibs&hl=en&cites=16654888528532118500', 'cites_id': ['16654888528532118500']}, {'container_type': 'Publication', 'source': <PublicationSource.AUTHOR_PUBLICATION_ENTRY: 'AUTHOR_PUBLICATION_ENTRY'>, 'bib': {'title': 'Rheological properties of palygorskite–bentonite and sepiolite–bentonite mixed clay suspensions', 'pub_year': '2014', 'citation': 'Applied Clay Science 90, 165-174, 2014'}, 'filled': False, 'author_pub_id': 'sz943bMAAAAJ:u5HHmVD_uO8C', 'num_citations': 42, 'citedby_url': 'https://scholar.google.com/scholar?oi=bibs&hl=en&cites=1553989996859065259', 'cites_id': ['1553989996859065259']}, {'container_type': 'Publication', 'source': <PublicationSource.AUTHOR_PUBLICATION_ENTRY: 'AUTHOR_PUBLICATION_ENTRY'>, 'bib': {'title': 'Short-term lime solution-kaolinite interfacial chemistry and its effect on long-term pozzolanic activity', 'pub_year': '2018', 'citation': 'Applied Clay Science 161, 419-426, 2018'}, 'filled': False, 'author_pub_id': 'sz943bMAAAAJ:2osOgNQ5qMEC',
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'num_citations': 26, 'citedby_url': 'https://scholar.google.com/scholar?oi=bibs&hl=en&cites=7328357679389403371', 'cites_id': ['7328357679389403371']},