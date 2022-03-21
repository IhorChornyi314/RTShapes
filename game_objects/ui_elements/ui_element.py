class UIElement:
    def __init__(self):
        self.rectangle = (0, 0, 0, 0)

    def __contains__(self, item):
        return self.rectangle[0] <= item[0] <= self.rectangle[2] and self.rectangle[1] <= item[1] <= self.rectangle[3]

    def activate(self):
        pass

