class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")
        
    class MyStuff1(object):

        def __init__(self):
            self.tangerine = "And now a thousand years between"

        def apple(self):
            print("I AM CLASSY APPLES!")
        
        class MyStuff2(object):

            def __init__(self):
                self.tangerine = "And now a thousand years between"

            def apple(self):
                print("I AM CLASSY APPLES!")

var = MyStuff().MyStuff1().MyStuff2()
var.apple()
print(var.tangerine)