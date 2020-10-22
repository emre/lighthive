class Operation:

    def __init__(self, type, value):
        self.type = type
        self.op_type = "%s_operation" % type
        self.op_value = value

    def to_dict(self):
        # return {
        #     "type": self.op_type,
        #     "value": self.op_value,
        # }
        return [self.type, self.op_value]

    def __repr__(self):
        return self.to_dict()
