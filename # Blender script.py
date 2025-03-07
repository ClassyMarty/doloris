# Blender script
# CONFIGURATION:
importFolder = "/Users/classymarty/Desktop/import"
exportFolder = "/Users/classymarty/Desktop/export"



# SCRIPT
# Don't touch anything below here, unless you know what you're doing!

import bpy, os
from mathutils import Vector

# Validation
if not os.path.exists(importFolder):
    print("You need to set the import folder in the script!")

if not os.path.exists(exportFolder):
    os.mkdir(exportFolder)



def clear_objects():
    # Clear materials
    for ob in bpy.context.selected_editable_objects:
        ob.active_material_index = 0
        for i in range(len(ob.material_slots)):
            bpy.ops.object.material_slot_remove({'object': ob})
    # Delete the objects
    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj)


# Grab all files in the import directory
files = os.listdir(importFolder)

for f in files:
    if not f.endswith(".gltf"):
        continue
    
    # Ensure the scene we're using doesn't have any meshes
    # We definitely don't want to accidentally export weird stuff
    clear_objects()
    
    # Debug log
    print("Processing: " + f)
    
    # Import the gltf scene
    bpy.ops.import_scene.gltf(filepath = os.path.join(importFolder, f))
    
    # Remove translation from the object
    for obj in bpy.data.objects:
        obj.location = (0, 0, obj.location.z)
    
    #vAt this point the object should be centered on the world origin
    
    # Save to output folder
    # Can use files more like the input files by adding "export_format = 'GLTF_SEPARATE'" parameter below
    # But, according to https://docs.godotengine.org/en/3.2/g...
    # We're better to use the binary format (which is the gltf export default)
    bpy.ops.export_scene.gltf(filepath = os.path.join(exportFolder, f))
    
    Debug log
    print("Done!")