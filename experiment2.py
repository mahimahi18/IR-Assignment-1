import ijson

class Soundex:
    def __init__(self,query):
        self.query=query
        
    def tokenize(self):
        query=self.query.upper().split()
        code_list=[]
        for term in query:
            code_list.append(self.generate_soundex_code(term))
        
    def generate_soundex_code(self, term):
        soundex=""
        soundex += term[0]
        
        soundex_dictionary={"BFPV":"1","CGJKQSXZ":"2","DT":"3","L":"4","MN":"5","R":"6","AEIOUHWY":"0"}
        
        for t in term[1:]:
            for key in soundex_dictionary.keys():
                if t in key:
                    code=soundex_dictionary[key]
                if code!="0" and code!=soundex[-1]:
                    soundex+=(code)
                    
        soundex = soundex[:4].ljust(4,"0")
        
        yield soundex