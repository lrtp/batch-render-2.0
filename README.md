# batch-render-2.0
Batch render script to render multiple file in background


Overview

This project contains a Python script that allows you to batch render multiple Blender files and scenes in sequence using Blender’s command-line interface. It’s a simple and effective way to automate rendering without having to open Blender manually for each file.
📂 Project Structure

/project-folder
│
├── render_batch.py          # Python script to batch render files
├── render_batch_improved.py # Enhanced version with custom output paths and error handling
└── README.md                # This file

⚙️ Requirements

    Blender 4.3 or compatible version

    Basic Python (no external libraries required)

    Windows Command Prompt (or any terminal that can run Blender CLI)

🚀 How to Run

    Prepare the script:

        Edit the files_to_render list to include the absolute paths of your .blend files and the specific scene names you want to render.

        Define your desired output directory in output_base_dir.

    Run the script from the Command Prompt:

    "C:\Program Files\Blender Foundation\Blender 4.3\blender.exe" -b --python "D:\Path\To\Your\render_batch.py"

        -b: Runs Blender in background mode (no GUI)

        --python: Runs the provided Python script inside Blender

    Optional:
    Create a .bat file for quick execution.

✅ Features

    Render multiple .blend files in sequence.

    Supports selecting specific scenes per file.

    Custom output directories for each file/scene.

    Automatic folder creation for renders.

    Error handling if files or scenes are missing.

    Progress logging to the terminal.

📌 Notes

    You must provide absolute paths for both .blend files and the Python script.

    Ensure that your render output settings (file format, resolution, etc.) are correctly configured inside each .blend file.

    The script assumes you are rendering animations. If you want to render still frames, the script can easily be adapted.

✨ Credits

Script developed with support from ChatGPT.
Maintained by [Your Name].
