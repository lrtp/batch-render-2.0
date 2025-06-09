# batch-render-2.0
Batch render script to render multiple file in background


# 🌀 Blender Background Rendering – Multi-Scene Animation Automation

This repository provides step-by-step instructions to render multiple **animations** from different scenes and `.blend` files using **Blender's background mode** on **Windows**, while preserving internal Blender settings for output path, format, and frame range.

---

## 📦 Requirements

- ✅ Blender installed (e.g. `C:\Program Files\Blender Foundation\Blender 4.1\blender.exe`)
- ✅ `.blend` files with:
  - Scene names configured
  - Output path and format set in Blender’s **Output Properties**
  - Frame start/end set in **Output Properties**

---

## 📁 Example Folder Structure

D:
├── Projects
│ ├── MyProject1
│ │ └── project1.blend
│ └── MyProject2
│ └── project2.blend
├── RenderScripts
│ └── render_all.bat

yaml
Copy
Edit

---

## 🛠️ Blender Scene Setup

Inside each `.blend` file:

1. Go to the **Output Properties** tab:
   - Set output path (e.g. `D:\Renders\Scene1\`)
   - Set file format (PNG, FFmpeg, etc.)
   - Set frame start and end (e.g. 1 → 250)
2. Save the file.
3. Repeat for each scene you want to render.

---

## 🖥️ Render from Command Line (Manual)

Open **Command Prompt** and run the following:

```cmd
"C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" -b "D:\Projects\MyProject1\project1.blend" -S "Scene1" -a
To render multiple scenes:

cmd
Copy
Edit
"C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" -b "D:\Projects\MyProject1\project1.blend" -S "Scene1" -a ^
&& "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" -b "D:\Projects\MyProject1\project1.blend" -S "Scene2" -a ^
&& "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" -b "D:\Projects\MyProject2\project2.blend" -S "Scene3" -a
📄 Automate with a .bat File
Open Notepad

Paste the following:

bat
Copy
Edit
@echo off
set BLENDER="C:\Program Files\Blender Foundation\Blender 4.1\blender.exe"

echo Starting Scene1 from project1.blend...
%BLENDER% -b "D:\Projects\MyProject1\project1.blend" -S "Scene1" -a

echo Starting Scene2 from project1.blend...
%BLENDER% -b "D:\Projects\MyProject1\project1.blend" -S "Scene2" -a

echo Starting Scene3 from project2.blend...
%BLENDER% -b "D:\Projects\MyProject2\project2.blend" -S "Scene3" -a

echo All scenes rendered.
pause
Save it as:
D:\RenderScripts\render_all.bat

📌 Important: Select "Save as type: All Files" and not .txt, and use .bat as extension.

Double-click render_all.bat to run the render batch job.

🧪 Notes & Troubleshooting
-b: Run Blender in background (no GUI)

-S SceneName: Choose the scene to render

-a: Render animation using Blender's saved settings

Make sure the scene name matches exactly as written in Blender

Don’t use -F, -o, -f etc. unless you want to override settings in the .blend file

🧠 Tips
You can edit the .bat to log output to a file:

bat
Copy
Edit
%BLENDER% -b "file.blend" -S "Scene" -a >> render_log.txt 2>&1
To render in parallel (advanced), use start in the .bat:

bat
Copy
Edit
start "" %BLENDER% -b "file.blend" -S "Scene" -a
📜 License
MIT License
