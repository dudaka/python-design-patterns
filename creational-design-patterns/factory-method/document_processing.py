from abc import ABC, abstractmethod

class Document(ABC):
  @abstractmethod
  def open(self):
    pass

class WordDocument(Document):
  def open(self):
    return "Opening a Word document"
  
class PdfDocument(Document):
  def open(self):
    return "Opening a PDF document"
  
class HtmlDocument(Document):
  def open(self):
    return "Opening an HTML document"
  
class DocumentFactory(ABC):
  @abstractmethod
  def create_document(self) -> Document:
    pass

class WordDocumentFactory(DocumentFactory):
  def create_document(self) -> Document:
    return WordDocument()
  
class PdfDocumentFactory(DocumentFactory):
  def create_document(self) -> Document:
    return PdfDocument()
  
class HtmlDocumentFactory(DocumentFactory):
  def create_document(self) -> Document:
    return HtmlDocument()
  
# client code
def process_document(factory: DocumentFactory):
  document = factory.create_document()
  print(document.open())


if __name__ == "__main__":
  word_factory = WordDocumentFactory()
  process_document(word_factory)
  
  pdf_factory = PdfDocumentFactory()
  process_document(pdf_factory)
  
  html_factory = HtmlDocumentFactory()
  process_document(html_factory)