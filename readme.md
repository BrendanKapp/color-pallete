<img align="left" width="48" height="48" src="icon.png" alt="Icon">

# Color Pallete

A super simple hex color pallete that can sit above all other windows.

![example](image.png)

Super simple:
1. Setup your pallete.
2. Dock the window on top.
3. Click to copy the hex code.

## Use Cases

I use this when developing games in Godot. Having to use the same colors between Godot, Blender, Krita, and the web can be a pain. This helps simplify my color workflow ensuring nothing ever gets lost.

## Usage

1. Setup your pallete in `palletes/`
    - See: [Demo Pallete](palletes/demo.md)
2. Select the pallete to use in `app.config`
3. Run app:
    > python3 app.py

## Install Dependencies

> pip install PyQt5

## Install as a Desktop App [*Optional*]

1. Update `Exec` and `Icon` path in `pallete.desktop`
2. Copy the file to `~/.local/share/applications`
3. Run: 
    > update-desktop-database ~/.local/share/applications
4. Verify it appears in the start menu. If not, a system restart may be required.

## License

[MIT License](mit_license.md)
