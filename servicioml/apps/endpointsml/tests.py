
from django.test import TestCase

# Create your tests here.

from apps.endpointsml.mlclassifier import LogisticRegresion




class LogisticRegrsionTest(TestCase):
    def test__rf_algoritm(self):
        input_data = '''Absolutely appalling. Sent my parents here for their 30th anniversary. The place was over booked. They entered their room to find the belongings of another guest. Then had to wait over an hour for a room. Spa facilities were closed although they did not mention this when booking. They advertised it as a spa get away. Paid good money for the night too! I’m so disappointed that my parents had this experience for their anniversary. Don’t book'''
        my_algoritm = LogisticRegresion()
        
        cleaner_text = my_algoritm.preprocesing(input_data)
        vectorize = my_algoritm.vectorize(cleaner_text)
        predict = my_algoritm.predict(vectorize)

        response = my_algoritm.postprocesing(predict[0])

        print(predict)
        print(response)

