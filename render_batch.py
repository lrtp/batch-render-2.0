import subprocess
import os

# Percorso Blender (modifica questo con il tuo percorso Blender se diverso)
BLENDER_EXE = r"C:\Program Files\Blender Foundation\Blender 4.0\blender.exe"

# Lista dei file .blend e delle scene da renderizzare
scenes_to_render = [
    (r"C:\TUO\PERCORSO\file1.blend", "Scene 1"),
    (r"C:\TUO\PERCORSO\file2.blend", "Scene 2"),
    # Aggiungi tutte le combinazioni che vuoi
]

# Cartella in cui salvare i log
log_dir = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(log_dir, exist_ok=True)

# Esegui il rendering per ogni scena
for blend_path, scene_name in scenes_to_render:
    blend_filename = os.path.splitext(os.path.basename(blend_path))[0]
    safe_scene_name = scene_name.replace(" ", "_")
    log_filename = f"{blend_filename}_{safe_scene_name}.log"
    log_path = os.path.join(log_dir, log_filename)

    print(f"\n🔄 Rendering {scene_name} from {blend_filename}")
    print(f"📝 Logging to {log_path}")

    cmd = [
        BLENDER_EXE,
        "-b", blend_path,
        "-S", scene_name,
        "-a"
    ]

    with open(log_path, "w", encoding="utf-8") as log_file:
        try:
            subprocess.run(cmd, check=True, stdout=log_file, stderr=subprocess.STDOUT)
            print(f"✅ Done: {scene_name}")
        except subprocess.CalledProcessError:
            print(f"❌ Error rendering {scene_name} — see log")

print("\n📂 Tutti i log sono salvati nella cartella 'logs'")
print("🎉 Rendering completato.")
