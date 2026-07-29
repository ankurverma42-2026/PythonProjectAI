import random
import json
#Reg Exp
import re



class TextAnalyzer:
    def __init__(self,text):
        self.text = text

    def word_count(self):
        return len(self.text.split())

    @staticmethod
    def random_no_gen():
        print(random.randint(1,100))


    def check_string_in_stmt(self):
        if "cool" in self.text:
            return True
        else:
            return False

    def python_2_json(self):
        print(json.dumps(self.text))

    def json_2_python(self):
        x='{"name":"Ankur", "city":"Tampa"}'
        return json.loads(x)