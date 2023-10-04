class Tag(object):
    def __init__(self,name,contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self,file=None):
        print(self,file=file)

class DocType(Tag):

    def __init__(self):
        super().__init__("doctype something complex",'')
        self.end_tag = ''

class Head(Tag):

    def __init__(self,title):
        super().__init__('head','')
        if title:
            self._title_tag = Tag('title',title)
            self.contents = str(self._title_tag)

class Body(Tag):

    def __init__(self):
        super(Body, self).__init__('body','')
        self._body_contents = []

    def addTags(self,name,content):
        new_tag = Tag(name,content)
        self._body_contents.append(new_tag)

    def display(self,file=None):
        for tag in self._body_contents:
            self.contents += str(tag)
        super().display(file=file)

# implementing composition in HTML class

class HTML():
    def __init__(self,title=None):
        self._body = Body()
        self._head = Head(title=title)
        self._doc_type = DocType()

    def add_tag(self,name,content):
        self._body.addTags(name,content)

    def display(self,file=None):
        self._doc_type.display(file=file)
        print("<html>")
        self._head.display(file=file)
        self._body.display(file=file)
        print("html")

if __name__ == "__main__":
    html = HTML("Demo stuff")
    html.add_tag('h1','main heading')
    html.add_tag('h2','sub heading')
    html.add_tag('p','para in browser')
    with open("text_html.html",'w') as htmldoc:
        html.display(file=htmldoc)
    html.display()

new_body = Body()
new_body.addTags('h1',"Aggregation ")
new_body.addTags('p','unlike <strong>Composition</strong> aggregation uses existing objects to build other objects')
new_body.addTags('p','composed objects doesnt own the object it is made up of and it ceases to exist when composing objects are destroyed')
html._body = new_body
with open("test2.html",'w') as ht:
    html.display(file=ht)


