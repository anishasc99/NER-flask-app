# NER-flask-app
Run flask form and enter email. For example, 

Entities in 'Hi Robin. I need  100, 400 and 300 tons of Epoxy, Boxofine and Ramflyn respectively. Hope you can deliver on time. Thanks and regards, Anisha'

gives output:

B-QUAN 100
B-QUAN 400
B-QUAN 300
B-PROD Epoxy
B-PROD Boxofine
B-PROD Ramflyn
