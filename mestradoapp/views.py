from builtins import print

from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from mestradoAPI.twitter.getTweets import username_tweets_to_csv
from mestradoAPI.synonyms.wordNetSynonyms import retornaSimilaridade
from .models import Music
from .serializers import MusicSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
import re
from collections import Counter
import json
from itertools import groupby
from rest_framework.decorators import api_view


# Create your views here.
class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

def buildDictionarySin(text):
    freq = Counter()
    text = text.lower()
    tokens = re.findall(r"(?u)\b\w+\b", text)
    freq.update(tokens)
    keys = sorted(freq.keys())
    for i in range(len(keys)):
        for z in range(i+1, len(keys) - i):
            retornaSimilaridade(keys[i], keys[z])


def buildDictionary(text):
    freq = Counter()
    text = text.lower()
    tokens = re.findall(r"(?u)\b\w+\b", text)
    freq.update(tokens)
    keys_ordenadas = sorted(freq.keys())

    mydict = {}
    for k, g in groupby(keys_ordenadas, key=lambda x: x[0]):
        if k in mydict:
            mydict[k] += g
        else:
            mydict[k] = list(g)

    return mydict;

@csrf_exempt
def metodo_post(request):
    data = JSONParser().parse(request)

    mydict = buildDictionary(data["texto"])
    retorno = json.dumps(mydict)

    buildDictionarySin(data["texto"])

    return JsonResponse(retorno, safe=False, status=status.HTTP_200_OK)

@api_view(['POST'])
def upload_file(request):
    for file_entry in request.FILES.getlist('file'):
        uploaded_file_name = file_entry.name
        uploaded_file_content = file_entry.read()

    mydict = buildDictionary(uploaded_file_content)
    retorno = json.dumps(mydict)

    return JsonResponse(retorno, safe=False, status=status.HTTP_200_OK)
    # upFile = request.FILES.getlist('file')
    # print upFile
    # outFile = open("/tmp/uploadTest.txt", "w")
    # outFile.write(upFile.read())
    # print request
    # return JsonResponse({uploaded_file_content}, status=200)

@api_view(['POST'])
def send_links(request):

    urlFacebook = request.POST['urlFacebook']
    userTwitter = request.POST['userTwitter']
    urlLinkedIn = request.POST['urlLinkedIn']

    username_tweets_to_csv(userTwitter, 5)

    mydict = buildDictionary("eloisa eloisa carne")
    retorno = json.dumps(mydict)

    return JsonResponse(retorno, safe=False, status=status.HTTP_200_OK)

