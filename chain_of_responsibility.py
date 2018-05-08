class EndHandler(object):
    def __init__(self):
        pass

    def handle_request(self, request):
        pass

class Handler1(object):
    def __init__(self):
        self.next_handler = EndHandler()

    def handle_request(self, request):

        self.next_handler.handle_request(request)
        
def main(request):
    concrete_handler = Handler1()

    concrete_handler.handle_request(request)

if __name__ == "__main__":
    # from the command line we can define some request
    main(request)
Alternative
chain_of_responsibility_alt.py


class Dispatcher(object):

  def __init__(self, handlers=[]):
    self.handlers = handlers

    def handle_request(self, request):
      for handler in self.handlers:
        request = handler(request)

      return request