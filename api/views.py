from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PublicationSerializer
from scholarly import scholarly
import requests
from scholarly import ProxyGenerator
pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)



@api_view(["GET"])
def getAuthorPublications(request, name):
    if request.method == "GET":

        # Retrieve the author's data, fill-in, and print
        search_query = scholarly.search_author(name)
        author = scholarly.fill(next(search_query))
        pubs = []
        

        if(("Adama Science and Technology University".strip().lower() in author['affiliation'].strip().lower()) or ("Adama Science and Technology".strip().lower() in author['affiliation'].strip().lower()) or ("Adama University".strip().lower() in author['affiliation'].strip().lower()) or ("@astu.edu.et".strip().lower() in author['email_domain'].strip().lower())):
            for pub in author['publications']:
                
                if("pub_year" in pub["bib"].keys()):

                    one = {"name": author['name'],
                            "title": pub["bib"]["title"],
                            "affiliation": author['affiliation'],
                            "paper_id": pub["author_pub_id"],
                            "year": pub["bib"]["pub_year"],
                            "journal": pub["bib"]["citation"],
                            "citation_count": pub["num_citations"],
                            "is_open_access" : author["public_access"],
                            "authors": author['name'],
                            }
                    
                    pubs.append(one)

        pubSer = PublicationSerializer(pubs, many=True)
        return Response(pubSer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def getAuthorPublicationsByYear(request, name, year):
    if request.method == "GET":

        # Retrieve the author's data, fill-in, and print
        search_query = scholarly.search_author(name)
        author = scholarly.fill(next(search_query))
        pubs = []

        if(("Adama Science and Technology University".strip().lower() in author['affiliation'].strip().lower()) or ("Adama Science and Technology".strip().lower() in author['affiliation'].strip().lower()) or ("Adama University".strip().lower() in author['affiliation'].strip().lower()) or ("@astu.edu.et".strip().lower() in author['email_domain'].strip().lower())):
            for pub in author['publications']:
                
                if("pub_year" in pub["bib"].keys()):
                    print(pub["bib"]["pub_year"], year)
                    if(pub["bib"]["pub_year"] == str(year)):

                        one = {"name": author['name'],
                                "title": pub["bib"]["title"],
                                "affiliation": author['affiliation'],
                                "paper_id": pub["author_pub_id"],
                                "year": pub["bib"]["pub_year"],
                                "journal": pub["bib"]["citation"],
                                "citation_count": pub["num_citations"],
                                "is_open_access" : author["public_access"],
                                "authors": author['name'],
                                }
                    
                        pubs.append(one)

        pubSer = PublicationSerializer(pubs, many=True)
        return Response(pubSer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def getAuthorPublicationsSemantic(request, name):
    if request.method == "GET":

        headers = {
            'x-api-key': '3FU8Nj7vAh241fadF6HlA6kVFfqQzKl115z6tQUO'
        }

        res = requests.get("https://api.semanticscholar.org/graph/v1/author/search?query="+name+"&fields=name,affiliations,url,papers.title,papers.year,papers.publicationTypes,papers.journal,papers.paperId,papers.authors,papers.abstract,papers.citationCount,papers.isOpenAccess,papers.openAccessPdf,papers.publicationDate,papers.url,papers.influentialCitationCount",headers=headers)
        res_json = res.json()
        pubs = []

        for author in res_json['data']:

            for aff in author['affiliations']:
                if(("Adama Science and Technology University".strip().lower() in aff.strip().lower()) or ("Adama Science and Technology".strip().lower() in aff.strip().lower()) or ("Adama University".strip().lower() in aff.strip().lower()) or ("@astu.edu.et".strip().lower() in author['email_domain'].strip().lower())):
                

                    for pub in author['papers']:
                        

                        one = {"name": author['name'],
                                "title": pub["title"],
                                "affiliation": aff,
                                "paper_id": pub["paperId"],
                                "year": pub["year"],
                                "citation_count": pub["citationCount"],
                                "abstract": pub["abstract"],
                                "is_open_access" : pub["isOpenAccess"],
                                "publication_date" : pub["publicationDate"],
                                "url": pub["url"],
                                "journal" : pub["journal"]['name'] if "name" in pub["journal"] else None,
                                "influential_citation_count": pub["influentialCitationCount"],
                                "publication_types" : ",".join([a for a in pub['publicationTypes']]) if pub['publicationTypes'] is not None else None,
                                "authors" : ",".join([a['name'] for a in pub['authors']]) if "authors" in pub else None,
                                }
                        
                        
                        
                        pubs.append(one)

            # pubSer = PublicationSerializer(pubs, many=True)
        return Response(pubs, status=status.HTTP_200_OK)


@api_view(["GET"])
def getAuthorPublicationsSemanticByYear(request, name, year):
    if request.method == "GET":
        headers = {
            'x-api-key': '3FU8Nj7vAh241fadF6HlA6kVFfqQzKl115z6tQUO'
        }
        res = requests.get("https://api.semanticscholar.org/graph/v1/author/search?query="+name+"&fields=name,affiliations,url,papers.title,papers.year,papers.publicationTypes,papers.journal,papers.paperId,papers.authors,papers.abstract,papers.citationCount,papers.isOpenAccess,papers.openAccessPdf,papers.publicationDate,papers.url,papers.influentialCitationCount",headers=headers)
        res_json = res.json()
        pubs = []

        for author in res_json['data']:

            for aff in author['affiliations']:
                if(("Adama Science and Technology University".strip().lower() in aff.strip().lower()) or ("Adama Science and Technology".strip().lower() in aff.strip().lower()) or ("Adama University".strip().lower() in aff.strip().lower()) or ("@astu.edu.et".strip().lower() in author['email_domain'].strip().lower())):
                

                    for pub in author['papers']:
                        
                        if(pub["year"] == year):
                            one = {"name": author['name'],
                                    "title": pub["title"],
                                    "affiliation": aff,
                                    "paper_id": pub["paperId"],
                                    "year": pub["year"],
                                    "citation_count": pub["citationCount"],
                                    "abstract": pub["abstract"],
                                    "is_open_access" : pub["isOpenAccess"],
                                    "publication_date" : pub["publicationDate"],
                                    "url": pub["url"],
                                    "journal" : pub["journal"]['name'] if "name" in pub["journal"] else None,
                                    "influential_citation_count": pub["influentialCitationCount"],
                                    "publication_types" : ",".join([a for a in pub['publicationTypes']]) if pub['publicationTypes'] is not None else None,
                                    "authors" : ",".join([a['name'] for a in pub['authors']]) if "authors" in pub else None,
                                    }
                            
                            
                            
                            pubs.append(one)

            # pubSer = PublicationSerializer(pubs, many=True)
        return Response(pubs, status=status.HTTP_200_OK)
    


@api_view(["GET"])
def getAuthorPublicationsBoth(request, name):
    if request.method == "GET":

        pubs = []
        title = []
        headers = {
            'x-api-key': '3FU8Nj7vAh241fadF6HlA6kVFfqQzKl115z6tQUO'
        }
        res = requests.get("https://api.semanticscholar.org/graph/v1/author/search?query="+name+"&fields=name,affiliations,url,papers.title,papers.year,papers.publicationTypes,papers.journal,papers.paperId,papers.authors,papers.abstract,papers.citationCount,papers.isOpenAccess,papers.openAccessPdf,papers.publicationDate,papers.url,papers.influentialCitationCount",headers=headers)
        res_json = res.json()

    
        if('data' in res_json):
            for author in res_json['data']:

                for aff in author['affiliations']:
                    if(("Adama Science and Technology University".strip().lower() in aff.strip().lower()) or ("Adama Science and Technology".strip().lower() in aff.strip().lower()) or ("Adama University".strip().lower() in aff.strip().lower()) or ("@astu.edu.et".strip().lower() in author['email_domain'].strip().lower())):
                    
                        for pub in author['papers']:
                            
                            title.append(pub["title"].strip().lower())
                            
                            one = {"name": author['name'],
                                    "title": pub["title"],
                                    "affiliation": aff,
                                    "paper_id": pub["paperId"],
                                    "year": pub["year"],
                                    "citation_count": pub["citationCount"],
                                    "abstract": pub["abstract"],
                                    "is_open_access" : pub["isOpenAccess"],
                                    "publication_date" : pub["publicationDate"],
                                    "url": pub["url"],
                                    "journal" : pub["journal"]['name'] if "name" in pub["journal"] else None,
                                    "influential_citation_count": pub["influentialCitationCount"],
                                    "publication_types" : ",".join([a for a in pub['publicationTypes']]) if pub['publicationTypes'] is not None else None,
                                    "authors" : ",".join([a['name'] for a in pub['authors']]) if "authors" in pub else None,
                                    }
                            
                            
                            
                            pubs.append(one)


        # Retrieve the author's data, fill-in, and print
        search_query = scholarly.search_author(name)
        try:
            author = scholarly.fill(next(search_query))
               
            if(("Adama Science and Technology University".strip().lower() in author['affiliation'].strip().lower()) or ("Adama Science and Technology".strip().lower() in author['affiliation'].strip().lower()) or ("Adama University".strip().lower() in author['affiliation'].strip().lower()) or ("@astu.edu.et".strip().lower() in author['email_domain'].strip().lower())):
                for pub in author['publications']:
                    
                    if("pub_year" in pub["bib"].keys()):

                        if not (pub["bib"]["title"].strip().lower() in title):

                            one = {"name": author['name'],
                                    "title": pub["bib"]["title"],
                                    "affiliation": author['affiliation'],
                                    "paper_id": pub["author_pub_id"],
                                    "year": pub["bib"]["pub_year"],
                                    "journal": pub["bib"]["citation"],
                                    "citation_count": pub["num_citations"],
                                    "is_open_access" : author["public_access"],
                                    "authors": author['name'],
                                    }
                            
                            pubs.append(one)

            pubSer = PublicationSerializer(pubs, many=True)
            return Response(pubSer.data, status=status.HTTP_200_OK)

        except StopIteration:
            
            pubSer = PublicationSerializer(pubs, many=True)
            return Response(pubSer.data, status=status.HTTP_200_OK)



@api_view(["GET"])
def getAuthorPublicationsBothByYear(request, name, year):
    if request.method == "GET":

        pubs = []
        title = []
        headers = {
            'x-api-key': '3FU8Nj7vAh241fadF6HlA6kVFfqQzKl115z6tQUO'
        }

        res = requests.get("https://api.semanticscholar.org/graph/v1/author/search?query="+name+"&fields=name,affiliations,url,papers.title,papers.year,papers.publicationTypes,papers.journal,papers.paperId,papers.authors,papers.abstract,papers.citationCount,papers.isOpenAccess,papers.openAccessPdf,papers.publicationDate,papers.url,papers.influentialCitationCount",headers=headers)
        res_json = res.json()
        
        if('data' in res_json):
            for author in res_json['data']:

                for aff in author['affiliations']:
                    if(("Adama Science and Technology University".strip().lower() in aff.strip().lower()) or ("Adama Science and Technology".strip().lower() in aff.strip().lower()) or ("Adama University".strip().lower() in aff.strip().lower()) or ("@astu.edu.et".strip().lower() in author['email_domain'].strip().lower())):
                    

                        for pub in author['papers']:
                            
                            if(pub["year"] == year):

                                title.append(pub["title"].strip().lower())
                                
                                one = {"name": author['name'],
                                        "title": pub["title"],
                                        "affiliation": aff,
                                        "paper_id": pub["paperId"],
                                        "year": pub["year"],
                                        "citation_count": pub["citationCount"],
                                        "abstract": pub["abstract"],
                                        "is_open_access" : pub["isOpenAccess"],
                                        "publication_date" : pub["publicationDate"],
                                        "url": pub["url"],
                                        "journal" : pub["journal"]['name'] if "name" in pub["journal"] else None,
                                        "influential_citation_count": pub["influentialCitationCount"],
                                        "publication_types" : ",".join([a for a in pub['publicationTypes']]) if pub['publicationTypes'] is not None else None,
                                        "authors" : ",".join([a['name'] for a in pub['authors']]) if "authors" in pub else None,
                                        }
                                
                                
                                
                                pubs.append(one)


        # Retrieve the author's data, fill-in, and print
        search_query = scholarly.search_author(name)
        try:
            author = scholarly.fill(next(search_query))


            if(("Adama Science and Technology University".strip().lower() in author['affiliation'].strip().lower()) or ("Adama Science and Technology".strip().lower() in author['affiliation'].strip().lower()) or ("Adama University".strip().lower() in author['affiliation'].strip().lower()) or ("@astu.edu.et".strip().lower() in author['email_domain'].strip().lower())):
                for pub in author['publications']:
                    
                    if("pub_year" in pub["bib"].keys()):
                        
                        if(pub["bib"]["pub_year"] == str(year)):

                            
                            if(pub["bib"]["title"].strip().lower() in title): 
                            
                                one = {"name": author['name'],
                                        "title": pub["bib"]["title"],
                                        "affiliation": author['affiliation'],
                                        "paper_id": pub["author_pub_id"],
                                        "year": pub["bib"]["pub_year"],
                                        "journal": pub["bib"]["citation"],
                                        "citation_count": pub["num_citations"],
                                        "is_open_access" : author["public_access"],
                                        "authors": author['name'],
                                        }
                            
                                pubs.append(one)
            

            pubSer = PublicationSerializer(pubs, many=True)
            return Response(pubSer.data, status=status.HTTP_200_OK)
            
        except StopIteration:
            
            pubSer = PublicationSerializer(pubs, many=True)
            return Response(pubSer.data, status=status.HTTP_200_OK)