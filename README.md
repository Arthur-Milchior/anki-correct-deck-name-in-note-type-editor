# Correct add-on name
This add-on is integrated in Anki 2.1.9. you thus won't need it unless
your anki is out of date. Hence it's not on ankiweb anymore.

## Rationale
When you open the note editor, {{Deck}} is replaced by a deck you
recently used, and not at all by the correct deck name. This add-on
almost correct this error.

The only case which is not corrected yet is when you change the «deck
override» value of a deck. You must close and reopen the card note in
order to see the correct value.

## Warning
This add-on is currently incompatible with Add-On
additional_card_fields_during_review. The (pull
request)[https://github.com/ijgnd/anki21__additional_card_fields_during_review/pull/1/commits/a74a093fd163e1105da7ca4998521f23808ea48a]
is supposed to correct that.

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
Support me on| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
