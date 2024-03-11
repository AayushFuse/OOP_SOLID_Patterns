"""
[Builder Design Pattern] Design a document generator using the Builder Design Pattern. 
Create a DocumentBuilder that creates documents of various types (e.g., PDF, HTML, Plain Text). 
Implement the builder methods to format the document content and structure according to the chosen type. 
Demonstrate how the Builder Design Pattern allows for the creation of different document formats without tightly coupling the document generation logic.
"""

from abc import ABC,abstractmethod

class Document():
    def __init__(self) -> None:
        self.title = None
        self.author = None
        self.heading = None
        self.body = None
        
    def __str__(self) -> str:
        return f"Document Title: {self.title}\nAuthor: {self.author}\nHeading: {self.heading}\n\nBody: {self.body}"

class DocumentBuilder(ABC):
    @abstractmethod
    def set_title(self,title):
        pass
    
    @abstractmethod
    def add_heading(self,heading):
        pass
    
    @abstractmethod
    def add_body(self,body):
        pass

class PDFBuilder(DocumentBuilder):
    def __init__(self) -> None:
        self.document = Document()
        
    def set_title(self, title):
        self.document.title = title
        print("PDF Title Set to: ",title)
        
    def add_heading(self,heading):
        self.document.heading = heading
        print("Heading: ",heading)
        
    def add_body(self, body):
        self.document.body = body
        print("Body: ",body)

class HTMLBuilder(DocumentBuilder):
    def __init__(self) -> None:
        self.document = Document()
        
    def set_title(self, title):
        self.document.title = title
        print("HTML Title Set to: ",title)
        
    def add_heading(self,heading):
        self.document.heading = heading
        print("Heading: ",heading)
        
    def add_body(self, body):
        self.document.body = body
        print("Body: ",body)

class TextBuilder(DocumentBuilder):
    def __init__(self) -> None:
        self.document = Document()
        
    def set_title(self, title):
        self.document.title = title
        print("Textfile Title Set to: ",title)
        
    def add_heading(self,heading):
        self.document.heading = heading
        print("Heading: ",heading)
        
    def add_body(self, body):
        self.document.body = body
        print("Body: ",body)
        
        
class DocumentDirector:
    def __init__(self) -> None:
        self.builder = None
        
    def create_document(self,builder,title,heading,body):
        self.builder = builder
        self.builder.set_title(title)
        self.builder.add_heading(heading)
        self.builder.add_body(body)
        
        
    @property
    def document(self):
        return self.builder.document
    
    
    
if __name__ == "__main__":
    director = DocumentDirector()
    tb = TextBuilder()
    director.create_document(tb,"Aayush","Hello! This is me","Arsenal Top of the table. How are you feeling")
    print(director.document)