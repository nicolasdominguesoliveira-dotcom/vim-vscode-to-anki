import requests

DECK = "Vim Vscode Shortcuts"
MODEL = "Basic (and reversed card)"
ANKI_URL = "http://localhost:8765"

cards = [
    # Modes
    ("i", "Enter insert mode BEFORE the cursor"),
    ("I", "Enter insert mode at the BEGINNING of the line"),
    ("a", "Enter insert mode AFTER the cursor"),
    ("A", "Enter insert mode at the END of the line"),
    ("o", "Open new line BELOW and enter insert mode"),
    ("O", "Open new line ABOVE and enter insert mode"),
    ("Esc", "Return to normal mode"),
    ("v", "Visual mode (select character by character)"),
    ("V", "Visual mode by line"),
    ("Ctrl+v", "Visual block mode"),

    # Motion
    ("h", "Move cursor LEFT"),
    ("j", "Move cursor DOWN"),
    ("k", "Move cursor UP"),
    ("l", "Move cursor RIGHT"),
    ("w", "Jump to the start of the next word"),
    ("b", "Jump to the start of the previous word"),
    ("0", "Go to the BEGINNING of the line"),
    ("$", "Go to the END of the line"),
    ("gg", "Go to the TOP of the file"),
    ("G", "Go to the BOTTOM of the file"),
    ("Ctrl+u", "Scroll up half a screen"),
    ("Ctrl+d", "Scroll down half a screen"),
    ("f{char}", "Jump to the next occurrence of {char} on the line"),
    ("F{char}", "Jump to the PREVIOUS occurrence of {char} on the line"),
    ("%", "Jump to the matching delimiter ( ), [ ], { }"),
    ("zz", "Center the screen on the cursor"),

    # Actions
    ("x", "Delete the character under the cursor"),
    ("dd", "Delete (cut) the entire line"),
    ("dw", "Delete to the end of the word"),
    ("D", "Delete from the cursor to the end of the line"),
    ("diw", "Delete the entire word (delete inner word)"),
    ("yy", "Copy the entire line"),
    ("yw", "Copy to the end of the word"),
    ("yiw", "Copy the entire word (yank inner word)"),
    ("p", "Paste AFTER the cursor"),
    ("P", "Paste BEFORE the cursor"),
    ("u", "Undo"),
    ("Ctrl+r", "Redo"),
    (".", "Repeat the last command"),
    ("r", "Replace the character under the cursor"),
    ("c", "Change (delete and enter insert mode) — requires a motion"),
    ("ciw", "Change the entire word (change inner word)"),
    ('ci"', "Change the content inside quotes"),
    ("J", "Join the current line with the line below"),
    (">>", "Indent the line to the right"),
    ("<<", "Indent the line to the left"),
    ("~", "Toggle uppercase/lowercase of the character under the cursor"),

    # Search
    ("/", "Start forward search"),
    ("n", "Go to the NEXT search match"),
    ("N", "Go to the PREVIOUS search match"),
    ("*", "Search for the exact word under the cursor"),

    # Commands
    (":", "Open command line"),
    (":w", "Save the file"),
    (":q", "Close the file"),
    (":wq", "Save and close"),
    (":q!", "Force close without saving"),
]

def create_deck(name):
    requests.post(ANKI_URL, json={
        "action": "createDeck",
        "version": 6,
        "params": {"deck": name}
    })

def add_cards(cards):
    notes = []
    for front, back in cards:
        notes.append({
            "deckName": DECK,
            "modelName": MODEL,
            "fields": {
                "Front": f"<code>{front}</code>",
                "Back": back
            },
            "options": {
                "allowDuplicate": True,
                "duplicateScope": "deck"
            },
            "tags": ["vim", "vscode", "shortcuts"]
        })

    response = requests.post(ANKI_URL, json={
        "action": "addNotes",
        "version": 6,
        "params": {"notes": notes}
    }).json()

    result = response.get("result") or []
    added = sum(1 for r in result if r is not None)
    skipped = len(notes) - added
    print(f"✅ {added} cards added")
    if skipped:
        print(f"⚠️  {skipped} skipped (duplicates or empty)")

create_deck(DECK)
add_cards(cards)
