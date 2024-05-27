from rest_framework import serializers


class PublicationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=200)
    affiliation = serializers.CharField(max_length=200)
    paper_id = serializers.CharField(max_length=200)
    year = serializers.IntegerField()
    citation_count = serializers.CharField(max_length=200)
    abstract = serializers.CharField(max_length=1000, required=False, allow_null=True)
    is_open_access = serializers.CharField(max_length=200, required=False, allow_null=True)
    publication_date = serializers.CharField(max_length=200, required=False, allow_null=True)
    url = serializers.CharField(max_length=300, required=False, allow_null=True)
    journal = serializers.CharField(max_length=200, required=False, allow_null=True)
    influential_citation_count = serializers.CharField(max_length=200, required=False, allow_null=True)
    publication_types = serializers.CharField(max_length=200, required=False, allow_null=True)
    authors = serializers.CharField(max_length=200, required=False, allow_null=True)
