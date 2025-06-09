import bpy

# List your blend files and scene names (None means use current scene)
files_to_render = [
    ("C:/filepath/projectfileA.blend", "Scene 1"),
    ("C:/filepath/projectfileA.blend", "Scene 2"),
    ("C:/filepath/projectfileB.blend", None),
]

for filepath, scene_name in files_to_render:
    print(f"Opening {filepath}")
    bpy.ops.wm.open_mainfile(filepath=filepath)

    if scene_name:
        print(f"Switching to scene: {scene_name}")
        bpy.context.window.scene = bpy.data.scenes[scene_name]

    print("Starting render...")
    bpy.ops.render.render(animation=True)
    print(f"Finished rendering {filepath} - {scene_name if scene_name else 'Current Scene'}")

print("All files rendered!")
