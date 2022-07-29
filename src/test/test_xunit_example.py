# class TestClass:
#
#     @classmethod
#     def setup_class(cls):
#         print('\n setup up TestClass')
#
#     @classmethod
#     def teardown_class(cls):
#         print('\n tear down TestClass')
#
#
#     def setup_method(self, method):
#         if method==self.test1:
#             print ('\n setting up test1')
#         elif method==self.test2:
#             print ('\n setting up test2')
#         else:
#             print('\n setting up unkown test')
#
#     def teardown_method(self, method):
#         if method==self.test1:
#             print ('\n tear down  test1')
#         elif method==self.test2:
#             print ('\n tear down test2')
#         else:
#             print('\n tear down unkown test')
#
#     def test1(self):
#         print ('\n Executing Test1')
#         assert True
#
#     def test2(self):
#         print ('\n Executing Test2')
#         assert True