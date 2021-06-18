        
# Create your views here.
import json
import numpy as np
import scipy
from sentence_transformers import SentenceTransformer
import time
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets          
from .serializers import docsInformationSerializer, docsEmbeddingsSerializer 
from .models import doc_information, doc_embedding  
from django.views import View   
from django.views import View             
import time
import pickle

# get all the documents from the database
all_doc_information = doc_information.objects.all()
all_doc_embedding = doc_embedding.objects.all()


# load the model
roberta_optimised = pickle.load(open("./../../BERT/roberta_optimised", 'rb'))

# define empty dictionary to store information from database
# for easy access
embedding_dictionary = {}
# define empty arrays to hold embeddings and filenames respectively
# for each document
fileNames = []
# extracted_embeddings = []

# threshold gained by dynamic distance measurement
min_threshold = 0.57

# gets individual embedded vectors and creates a np array of embedded vectors
# and adds it to embedding_dictionary for easy access
def getEmbeddings():
    # gets individual embedded vectors and creates a np array of embedded vectors

    # for every document in database
    for doc in all_doc_information:
        # get name of the doc
        embedding_docs = all_doc_embedding.filter(doc_id=doc.doc_id)
        temp_arr = []
        for embedding in embedding_docs:
            # covert the embedding from binary to np array of type float32
            extracted_embedding = np.frombuffer(embedding.embeddings, dtype = "float32")
            temp_arr.append(extracted_embedding)
            
        # convert the whole embeddings array into an np array 
        # which is needed for comparison
        temp_arr = np.array(temp_arr) 
        embedding_dictionary[doc.doc_id] = temp_arr

# get embeddings at the start to initialize dictionary
getEmbeddings()


# filters the distances in a given array according to a threshold
# @arr: array to filter
# @threshold: a threshold to find the arrays
# returns all elements below the threshold, if the resulting array
# is an empty array, returns the original array
def filterDistances(arr, t):
    new_arr = []
    for element in arr:
        if element < t:
            new_arr.append(element)

    if len(new_arr) == 0:
        return arr
    return new_arr

# runs the loaded model with the given query 
# returns the top 100 documents and the time taken for the 
# query to the frontend
def run_query(query):
    # start timer
    start_time = time.time()

    # encode the query
    query_embedding = roberta_optimised.encode(query)
    # print("Time elapsed during embedding: ", t1 - t0) 


    # declare array to store results
    results = []
    for doc in embedding_dictionary:
        # get all embeddings for every doc
        extracted_embeddings = embedding_dictionary[doc]
        
        #distance of query from every embedding
        distances = scipy.spatial.distance.cdist([query_embedding], extracted_embeddings, "cosine")[0]
        
        # filter distance using predefined threshold
        distances = filterDistances(distances, min_threshold)

        # average the distance
        average_distance = sum(distances)/len(distances)

        result = (doc, average_distance)
        results.append(result)
    
    # sort
    results = sorted(results, key=lambda x: x[1])

    # Find the closest 100 documents based on cosine similarity
    number_top_matches = 100 
    if len(results) < 100:
        number_top_matches = len(results)

    response_docs = []
    for docid, distance in results[0:number_top_matches]:
        doc = doc_information.objects.get(doc_id=docid)
        cosine_score = "%.4f" % (1-distance)
        response_doc = (doc.doc_id, doc.document_name, doc.preview, doc.filepath, cosine_score)
        response_docs.append(response_doc)
    
    end_time = time.time()
    # find the total time taken
    time_taken = "%.4f" % (end_time - start_time)
    
    return (time_taken, response_docs)


class docsView(View):
# serves the get request from the user
  def get(self, request):
    query = request.GET.get('q', 'EMPTY')

    results = run_query(query)
    results = json.dumps(results)
    return HttpResponse(results)
  
  
  
