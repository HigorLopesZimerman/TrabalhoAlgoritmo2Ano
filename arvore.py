class Arvore:
    def __init__(self, key, pos):
        self.data = {"key":key, "pos":pos}
        self.right = None
        self.left = None

    def add_child(self, key, pos):
        if key == self.data["key"]:
            return

        if key < self.data["key"]:
            if self.left:
                self.left.add_child(key, pos)
            else:
                self.left = Arvore(key, pos)
        else:
            if self.right:
                self.right.add_child(key, pos)
            else:
                self.right = Arvore(key, pos)

    def crescente(self):
        elements = []

        # left visit
        if self.left:
            elements += self.left.crescente()

        #base node visit
        elements.append(self.data)

        if self.right:
            elements += self.right.crescente()

        return elements

    def decrescente(self):
        elements = []

        if self.right:
            elements += self.right.decrescente()

        elements.append(self.data)

        if self.left:
            elements += self.left.decrescente()

        return elements

    def search(self, key):
        if key == self.data["key"]:
            return self.data["pos"]

        if key < self.data["key"]:
            if self.left:
                return self.left.search(key)
            else:
                return None
        else:
            if self.right:
                return self.right.search(key)
            else:
                return None



    def find_min(self):
        if not self.left:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if not self.right:
            return self.data
        return self.right.find_max()

    def delete(self, key):
        if key < self.data["key"]:
            if self.left:
                self.left = self.left.delete(key)
        elif key > self.data["key"]:
            if self.right:
                self.right = self.right.delete(key)
        else:
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val["key"])

        return self