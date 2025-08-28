# Roblox Directory Structure Creator

A Python tool that creates a complete Roblox Studio directory structure for game development projects.

## Features

- **Interactive Prompt**: Prompts you for a folder path where you want to create the Roblox directory structure
- **Complete Structure**: Creates all standard Roblox Studio directories and subdirectories
- **Comprehensive Coverage**: Includes all major Roblox services and their typical subdirectories
- **Documentation**: Automatically generates a README.md file explaining the directory structure
- **Error Handling**: Robust error handling and validation
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Quick Start

### Option 1: Using the Batch File (Windows)
1. Double-click `run_roblox_creator.bat`
2. Enter the folder path when prompted
3. Confirm the path
4. The directory structure will be created automatically

### Option 2: Using Python Directly
1. Open a terminal/command prompt
2. Navigate to the project directory
3. Run: `python roblox_dir_creator.py`
4. Follow the prompts

## What Gets Created

The tool creates a streamlined Roblox Studio directory structure including:

### Core Services
- **Workspace** - 3D parts, models, NPCs, and interactive objects
- **Players** - Player objects and data when they join
- **Lighting** - Lighting, atmosphere, post-processing effects, skyboxes
- **MaterialService** - Manages materials and textures
- **ReplicatedFirst** - Local scripts/assets that load immediately (loading screens)
- **ReplicatedStorage** - Shared storage between client and server (remote events, functions, modules, assets)
- **ServerScriptService** - Server-only scripts and modules
- **ServerStorage** - Server-only storage for models, assets, and resources
- **StarterGui** - GUI objects cloned into each player's PlayerGui
- **StarterPack** - Tools that go into each player's Backpack
- **StarterPlayer** - LocalScripts and character scripts
- **Teams** - Team management and configuration
- **SoundService** - Global sound settings, music, SFX
- **TextChatService** - Chat service configurations and scripts

### Directory Structure
```
Workspace/
├── Camera/             # Main camera object for the game
├── Terrain/            # Terrain and landscape objects
├── SpawnLocation/      # Player spawn point
└── Baseplate/          # Base platform for the game world

Players/                # Contains player objects when they join

Lighting/
├── Atmosphere/         # Atmospheric effects and settings
├── Sky/                # Sky and environment settings
├── Bloom/              # Bloom lighting effects
├── DepthOfField/       # Depth of field effects
└── SunRays/            # Sun ray lighting effects

MaterialService/        # Manages materials and textures

ReplicatedFirst/        # Stores local scripts/assets that load immediately

ReplicatedStorage/      # Shared storage between client and server

ServerScriptService/    # Where server-only Scripts and ModuleScripts are stored

ServerStorage/          # Server-only storage for models, assets, and resources

StarterGui/             # GUI objects cloned into each player's PlayerGui

StarterPack/            # Tools that go into each player's Backpack

StarterPlayer/
├── StarterCharacterScripts/  # Scripts inserted into character models
└── StarterPlayerScripts/     # LocalScripts that run for each player

Teams/                  # Team management and configuration

SoundService/           # Manages global sound settings, music, etc.

TextChatService/
├── ChatWindowConfiguration/      # Chat window settings
├── ChatInputBarConfiguration/    # Chat input bar settings
├── ChannelTabsConfiguration/     # Chat channel tab settings
└── BubbleChatConfiguration/      # Bubble chat settings
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone or download this repository
2. No installation required - just run the script

## Usage Examples

### Basic Usage
```bash
python roblox_dir_creator.py
```

### Example Output
```
============================================================
ROBLOX DIRECTORY STRUCTURE CREATOR
============================================================

Enter the folder path where you want to create the Roblox directory structure: C:\MyRobloxGame

You entered: C:\MyRobloxGame
Is this correct? (y/n): y

Creating Roblox directory structure in: C:\MyRobloxGame
============================================================
✓ Created: ReplicatedStorage
✓ Created: ReplicatedStorage/Shared
✓ Created: ReplicatedStorage/Shared/Modules
...
============================================================
Successfully created 25+ directories!
Directory structure created at: C:\MyRobloxGame
✓ Created README.md with documentation

============================================================
SUCCESS! Roblox directory structure has been created.
============================================================

Location: C:\MyRobloxGame

You can now start developing your Roblox game!
Open the README.md file for more information about the structure.
```

## Directory Structure Best Practices

### ReplicatedStorage
- Use for code and assets that need to be shared between client and server
- Keep modules organized by functionality
- Store configuration files here

### ServerScriptService
- Place all server-side scripts here
- Organize by feature or system
- Keep server modules separate from client modules

### StarterPlayer
- Client scripts that run when a player joins
- Organize UI components logically
- Keep client modules organized

### StarterGui
- User interface elements
- Separate screens and components
- Use consistent naming conventions

### Workspace
- Game world and environment
- Organize by region or area
- Keep props and environment separate

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool.

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions, please open an issue on the repository.
