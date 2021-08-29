from django.http.response import JsonResponse
from rest_framework.response import Response

# Create your views here.

from rest_framework.views import APIView
from rest_framework import status

from apps.endpointsml.mlclassifier import LogisticRegresion

# # # Create your views here.
class sentimentAnalysisEnglis(APIView):
#     """ devulve una sentimitio positivo o negativo"""
    def post(self, request):
        print(predictReview(request.data['text']))
        try:
            print(predictReview(request.data['text']))
            data =predictReview(request.data['text'])
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data = {"Error": "request not contain label text for sentiment analisis"}
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self, request):
        return Response({"mensaje:": "Bien venido a la aplicacion para analizar el sentimiento de un comentario"})




def predictReview(input_data):
    """
    Clean the text
    Vectorize the text
    Text prediction
    Returns a response in json
    """
    my_algoritm = LogisticRegresion()
    cleaner_text = my_algoritm.preprocesing(input_data)
    vectorize = my_algoritm.vectorize(cleaner_text)
    predict = my_algoritm.predict(vectorize)
    return my_algoritm.postprocesing(predict[0])