class Training:
    entries = None
    output = None

    def __init__(self, entries, output):
        self.entries = entries
        self.output = output

    def showEntries(self):
        out = ""
        for entry in self.entries:
            out += (f"{entry}  ")
        out += f": {self.output}"
        return out
