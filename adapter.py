class WhatIHave(object):
    def provided_function_1(self): pass
    def provided_function_2(self): pass

class WhatIWant(object):
    def required_function(): pass

class ObjectAdapter(object):
    def __init__(self, what_i_have):
        self.what_i_have = what_i_have

    def required_function(self):
        return self.what_i_have.provided_function_1()

    def __getattr__(self, attr):
        #All else is handled by wrapped object
        return getattr(self.what_i_have, attr)
