import anki
from anki.collection import _Collection

def _newCard(self, note, template, due, did = None, flush=True):
        "Create a new card."
        card = anki.cards.Card(self)
        card.nid = note.id
        card.ord = template['ord']
        card.did = self.db.scalar("select did from cards where nid = ? and ord = ?", card.nid, card.ord)
        # Use template did (deck override) if valid, otherwise did in argument, otherwise model did
        if not card.did:
            if template['did'] and str(template['did']) in self.decks.decks:
                card.did = template['did']
            elif did:
                card.did = did
            else:
                card.did = note.model()['did']
        # if invalid did, use default instead
        deck = self.decks.get(card.did)
        if deck['dyn']:
            # must not be a filtered deck
            card.did = 1
        else:
            card.did = deck['id']
        card.due = self._dueForDid(card.did, due)
        if flush:
            card.flush()
        return card
_Collection._newCard = _newCard

def previewCards(self, note, type=0, did = None):
        if type == 0:
            cms = self.findTemplates(note)
        elif type == 1:
            cms = [c.template() for c in note.cards()]
        else:
            cms = note.model()['tmpls']
        if not cms:
            return []
        cards = []
        for template in cms:
            cards.append(self._newCard(note, template, 1, flush=False, did = did))
        return cards
_Collection.previewCards = previewCards
