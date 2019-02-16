from aqt.clayout import CardLayout

def redraw(self):
        did = self.parent.deckChooser.selectedId() if self.addMode else None
        self.cards = self.col.previewCards(self.note, 2, did = did)
        idx = self.ord
        if idx >= len(self.cards):
            self.ord = len(self.cards) - 1

        self.redrawing = True
        self.updateTopArea()
        self.updateMainArea()
        self.redrawing = False
        self.onCardSelected(self.ord)
CardLayout.redraw = redraw
