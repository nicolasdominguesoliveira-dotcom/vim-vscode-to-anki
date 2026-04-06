# vim-vscode-to-anki
> Send flashcards to Anki directly with Vim VSCode shortcuts via AnkiConnect

## Requirements

- Anki desktop (running)
- [AnkiConnect](https://ankiweb.net/shared/info/2055492159) add-on installed
- Python 3.8+
- `requests` library

## Installation
```bash
git clone https://github.com/nicolasdominguesoliveira-dotcom/vim-vscode-to-anki.git
cd vim-vscode-to-anki
pip install requests
```

## Usage

1. Open Anki
2. Run the script:
```bash
python vim_shortcuts_anki.py
```

The script will create a deck called **"Vim Vscode Shortcuts"** and add all cards automatically.

## Cards included

- Vim modes (insert, visual, normal)
- Motion commands

## License

MIT