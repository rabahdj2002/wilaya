import json
        

class handler:
    def __init__(self):
        """
        Initialize YourClass with a name.
        
        :param name: str: The name to initialize the class with.
        """

    def searchByCode(self, code):
        """
        Greet with the name provided.
        
        :return: str: A greeting message.
        """
        if code <= 0 or code > 58 or code is None:
            raise Exception("Wilaya code is not valid!")
        
        with open('wilaya\Wilaya_Of_Algeria.json', 'r', encoding='utf8') as w:
            data = json.load(w)

        return data[code-1]
    

    def searchByName(self, name):
        """
        Greet with the name provided.
        
        :return: str: A greeting message.
        """
        if name is None:
            raise Exception("Wilaya name is not valid!")
        
        with open('wilaya\Wilaya_Of_Algeria.json', 'rb') as w:
            data = [wilaya for wilaya in json.load(w) if wilaya['name'] == name.capitalize()]
            
        return data[0]
    