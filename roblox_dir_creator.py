import os
import sys
from pathlib import Path

def create_roblox_directory_structure(base_path):
    """
    Creates the standard Roblox Studio directory structure
    """
    # Define the Roblox directory structure
    directories = [
        "Workspace",
        "Workspace/Camera",
        "Workspace/Terrain",
        "Workspace/SpawnLocation",
        "Workspace/Baseplate",
        
        "Players",
        
        "Lighting",
        "Lighting/Atmosphere",
        "Lighting/Sky",
        "Lighting/Bloom",
        "Lighting/DepthOfField",
        "Lighting/SunRays",
        
        "MaterialService",
        
        "ReplicatedFirst",
        
        "ReplicatedStorage",
        
        "ServerScriptService",
        
        "ServerStorage",
        
        "StarterGui",
        
        "StarterPack",
        
        "StarterPlayer",
        "StarterPlayer/StarterCharacterScripts",
        "StarterPlayer/StarterPlayerScripts",
        
        "Teams",
        
        "SoundService",
        
        "TextChatService",
        "TextChatService/ChatWindowConfiguration",
        "TextChatService/ChatInputBarConfiguration",
        "TextChatService/ChannelTabsConfiguration",
        "TextChatService/BubbleChatConfiguration"
    ]
    
    # Create base directory if it doesn't exist
    base_path = Path(base_path)
    base_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Creating Roblox directory structure in: {base_path.absolute()}")
    print("=" * 60)
    
    # Create all directories
    created_count = 0
    for directory in directories:
        dir_path = base_path / directory
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            created_count += 1
            print(f"✓ Created: {directory}")
        except Exception as e:
            print(f"✗ Failed to create {directory}: {e}")
    
    print("=" * 60)
    print(f"Successfully created {created_count} directories!")
    print(f"Directory structure created at: {base_path.absolute()}")
    
    return base_path

def create_readme_file(base_path):
    """
    Creates a README file explaining the directory structure
    """
    readme_content = """# Roblox Directory Structure

This directory contains a complete Roblox Studio directory structure for development.

## Main Directories

### Workspace
- **Camera**: Main camera object for the game
- **Terrain**: Terrain and landscape objects
- **SpawnLocation**: Player spawn point
- **Baseplate**: Base platform for the game world

### Players
- Contains player objects when they join the game

### Lighting
- **Atmosphere**: Atmospheric effects and settings
- **Sky**: Sky and environment settings
- **Bloom**: Bloom lighting effects
- **DepthOfField**: Depth of field effects
- **SunRays**: Sun ray lighting effects

### MaterialService
- Manages materials and textures

### ReplicatedFirst
- Stores local scripts/assets that load immediately when the player joins

### ReplicatedStorage
- Shared storage between client and server

### ServerScriptService
- Where server-only Scripts and ModuleScripts are stored

### ServerStorage
- Server-only storage for models, assets, and resources

### StarterGui
- GUI objects placed here will be cloned into each player's PlayerGui

### StarterPack
- Tools placed here go into each player's Backpack when they spawn

### StarterPlayer
- **StarterCharacterScripts**: Scripts inserted into each character model when spawned
- **StarterPlayerScripts**: LocalScripts that run for each player

### Teams
- Team management and configuration

### SoundService
- Manages global sound settings, music, etc.

### TextChatService
- **ChatWindowConfiguration**: Chat window settings
- **ChatInputBarConfiguration**: Chat input bar settings
- **ChannelTabsConfiguration**: Chat channel tab settings
- **BubbleChatConfiguration**: Bubble chat settings

## Usage

1. Place your 3D objects in Workspace subdirectories
2. Use ReplicatedStorage for shared code and assets
3. Keep server logic in ServerScriptService
4. Organize client code in StarterPlayerScripts
5. Structure UI elements in StarterGui
6. Store server-only resources in ServerStorage
7. Configure chat settings in TextChatService

## Best Practices

- Keep modules in appropriate ModuleScript locations
- Use descriptive folder names
- Organize assets by type and purpose
- Maintain consistent naming conventions
- Document your code structure
- Separate client and server code appropriately

This structure follows Roblox Studio conventions and best practices for game development.
"""
    
    readme_path = base_path / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✓ Created README.md with documentation")

def main():
    """
    Main function that prompts for folder path and creates the structure
    """
    print("=" * 60)
    print("ROBLOX DIRECTORY STRUCTURE CREATOR")
    print("=" * 60)
    print()
    
    while True:
        # Get folder path from user
        folder_path = input("Enter the folder path where you want to create the Roblox directory structure: ").strip()
        
        if not folder_path:
            print("Please enter a valid folder path.")
            continue
        
        # Expand user path if needed
        folder_path = os.path.expanduser(folder_path)
        
        # Check if path is valid
        try:
            # Test if we can create the directory
            test_path = Path(folder_path)
            if test_path.exists() and not test_path.is_dir():
                print(f"Error: '{folder_path}' exists but is not a directory.")
                continue
        except Exception as e:
            print(f"Error with path '{folder_path}': {e}")
            continue
        
        # Confirm with user
        print(f"\nYou entered: {folder_path}")
        confirm = input("Is this correct? (y/n): ").strip().lower()
        
        if confirm in ['y', 'yes']:
            break
        else:
            print("Let's try again.\n")
    
    try:
        # Create the directory structure
        base_path = create_roblox_directory_structure(folder_path)
        
        # Create README file
        create_readme_file(base_path)
        
        print("\n" + "=" * 60)
        print("SUCCESS! Roblox directory structure has been created.")
        print("=" * 60)
        print(f"\nLocation: {base_path.absolute()}")
        print("\nYou can now start developing your Roblox game!")
        print("Open the README.md file for more information about the structure.")
        
    except Exception as e:
        print(f"\nError creating directory structure: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
