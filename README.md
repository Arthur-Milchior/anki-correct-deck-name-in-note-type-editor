# Correct add-on name
## Rationale
When you open the note editor, {{Deck}} is replaced by a deck you
recently used, and not at all by the correct deck name. This add-on
almost correct this error.

The only case which is not corrected yet is when you change the «deck
override» value of a deck. You must close and reopen the card note in
order to see the correct value.

## Usage
Just install the add-on.

## Internal
This change anki.collection._Collection._newCard,
anki.collection._Collection.previewCards and
aqt.clayout.CardLayout.redraw. Those methodes are replaced by new
method and does not use the previous method anymore.

## Pull request
This is pull request number (280)[https://github.com/dae/anki/pull/280] on anki.

## Version 2.0
None
## TODO
See Rationale
## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-correct-deck-name-in-note-type-editor
Addon number| [1658360602](https://ankiweb.net/shared/info/1658360602)
