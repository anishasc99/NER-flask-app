# NER-flask-app
Run flask form and enter email. It will use pre-trained model stored in /nlp. For example, 

Entities in 'Hi Robin. I need  100, 400 and 300 tons of Epoxy, Boxofine and Ramflyn respectively. Hope you can deliver on time. Thanks and regards, Anisha'

gives output:

B-QUAN 100
B-QUAN 400
B-QUAN 300
B-PROD Epoxy
B-PROD Boxofine
B-PROD Ramflyn

To train with custom data, use NER-training.ipynb file. To generate the emails, run email_generation.py. Annotate the emails in CoNLL format, using any annotation tool such as
Inception.
