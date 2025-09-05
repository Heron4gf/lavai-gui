# lavai-gui

A graphical user interface for managing AI provider credentials stored by the [lavai](https://github.com/Heron4gf/lavai) library.

## Features

- Simple graphical interface built with tkinter (built-in Python GUI library)
- View all stored AI provider credentials
- Add new providers with their API keys
- Remove existing providers
- Edit API keys for existing providers
- Command-line interface for easy launching

## Install and Use

After installation, you can launch the GUI application from the command line:

```bash
pip install lavai-gui
lavai-gui start
```

### GUI Functionality

1. **Main Window**: Displays a list of all stored client names
2. **Add Button**: Opens a dialog to add a new client with name and API key
3. **Remove Button**: Removes the selected client after confirmation
4. **Edit Button**: Opens a dialog to edit the API key of the selected client
5. **Refresh Button**: Reloads the client list from the credentials file

## Requirements

- Python 3.6+
- [lavai](https://github.com/Heron4gf/lavai) library

## License

MIT
