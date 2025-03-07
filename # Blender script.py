# Blender script
# CONFIGURATION:
importFolder = "/Users/classymarty/Desktop/import"
exportFolder = "/Users/classymarty/Desktop/export"

## SCRIPT
## Don't touch anything below here, unless you know what you're doing!

import bpy, os
from mathutils import Vector

def clear_objects():
    # Clear materials
    for ob in bpy.data.objects:
        if ob.type == 'MESH' and ob.data is not None:
            ob.data.materials.clear()
    
    # Delete the objects
    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj)



def set_mesh_center(obj):
    # Append the -col suffix, so Blender will create collisions
    obj.name += "-col"
    print(obj.name)

    # Cache the mode we were in, and the current location of the 3D cursor
    prevMode = obj.mode
    cursorOldPosition = bpy.context.scene.cursor.location
    
    # Some objects are weird, and have null data (like palmDetailed_large.gltf)
    # We're just going to ignore them and hope for the best!
    if obj.data is None:
        return
    
    # Count the vertices of the object
    count = len(obj.data.vertices)

    # Move the 3D cursor to the center of the object. Then strip out the z component to snap to the bottom plane
    bpy.context.scene.cursor.location = obj.matrix_world @ ((1.0 / count) * sum([v.co for v in obj.data.vertices], Vector()))
    bpy.context.scene.cursor.location.z = 0

    # Toggle to Object mode if necessary
    if obj.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

    # Set object origin to match the 3D cursor we moved above
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

    # Return to the previous mode
    if prevMode != 'OBJECT':
        bpy.ops.object.mode_set(mode=prevMode, toggle=False)
    
    # Return the 3D cursor to its previous position
    bpy.context.scene.cursor.location = cursorOldPosition

if not os.path.exists(importFolder):
    print("You need to set the import folder in the script!")

if not os.path.exists(exportFolder):
    os.mkdir(exportFolder)

# Grab all files in the import directory
files = os.listdir(importFolder)

for f in files:
    if not (f.endswith(".gltf") or f.endswith(".glb")):
        continue
    
    # Ensure the scene we're using doesn't have any meshes
    # We definitely don't want to accidentally export weird stuff
    clear_objects()
    
    # Debug log
    print("Processing: " + f)
    
    # Import the gltf scene
    try:
        bpy.ops.import_scene.gltf(filepath=os.path.join(importFolder, f))
    except Exception as e:
        print(f"Failed to import {f}: {e}")
        continue
    
    # Attempt to set the origin of the mesh to its center on the bottom plane
    for obj in bpy.data.objects:
        set_mesh_center(obj)
    
    # Remove translation from the object
    for obj in bpy.data.objects:
        obj.location = (0, 0, obj.location.z)
    
    # At this point the object should be centered on the world origin
    
    # Save to output folder
    try:
        bpy.ops.export_scene.gltf(filepath=os.path.join(exportFolder, f))
    except Exception as e:
        print(f"Failed to export {f}: {e}")
    
    # Debug log
    print("Done!")
