# Bot token from Bot Father
TOKEN = "1444782765:AAGC1IIKYi0UBedn8HU3O9BUf8aQziOQF3o"

# Your API ID and Hash from https://my.telegram.org/apps
API_ID = 2391388
API_HASH = "75c3fb34752b710b6106b8f510d06ec4"

# Chat used for logs
log_chat = -1001237251568


# Sudoers and super sudoers
super_sudoers = [1352720951]
sudoers = [1352720951]
sudoers += super_sudoers


# Prefixes for commands, e.g: /command and !command
prefix = ["/", "!"]


# List of disabled plugins
disabled_plugins = []


# API keys
TENOR_API_KEY = ""


# Bot version, do not touch this
with open("version.txt") as f:
    version = f.read().strip()
