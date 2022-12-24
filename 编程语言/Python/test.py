class AssignValue(object):
    def __init__(self, value, xie):
        self.value = value
        self.xie = xie


my_value = AssignValue(6.2, 3)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的
