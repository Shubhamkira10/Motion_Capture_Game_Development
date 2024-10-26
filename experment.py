import bpy
import json

# Load joint data from JSON file
json_file_path = "D:\\OPEN CV\\python\\pose_data_20241026_0530.json"
with open(json_file_path, "r") as file:
    joint_data = json.load(file)
    print(joint_data)

# Open the existing Blender file
bpy.ops.wm.open_mainfile(filepath="C:\\Users\\Dell\\Downloads\\body.blend")

# Define a mapping from joint IDs to bone names in the Blender armature
joint_to_bone_map = {
    "11": "Bone.11",
    "12": "Bone.12",
    "13": "Bone.13",
    "14": "Bone.14",
    "23": "Bone.23",
    "24": "Bone.24",
    "25": "Bone.25",
    "26": "Bone.26",
    "27": "Bone.27",
    "28": "Bone.28"
}

boneName = [
    "Bone.11",
    "Bone.23",
    "Bone.27",
    "Bone.28",
    "Bone.29",
    "Bone.30",
    "Bone.32",
    "Bone.31",
    "Bone.12",
    "Bone.24",
    "Bone.13",
    "Bone.25",
    "Bone.14",
    "Bone.26"
]

# Select the armature and enter pose mode
collection_name = "Collection"  # Ensure this matches your collection name
armature_entity = bpy.data.collections[collection_name].objects.get("Armature")

if armature_entity:
    bpy.context.view_layer.objects.active = armature_entity
    bpy.ops.object.mode_set(mode='POSE')

    # Apply joint data to bones and keyframe each frame
    for frame_number, frame_data in enumerate(joint_data):
        # Skip empty frames
        if not frame_data:
            continue
        
        # Set the current frame
        bpy.context.scene.frame_set(frame_number)

        # Update each bone position
        for joint_id, coords in frame_data.items():
            if joint_id in joint_to_bone_map:
                bone_name = joint_to_bone_map[joint_id]
                bone = armature_entity.pose.bones.get(bone_name)

                if bone:
                    # Set bone location using coordinates
                    x, y = coords  # Extract X and Y coordinates
                    z = bone.location.z  # Keep the current Z position

                    # Update bone location
                    bone.location = (x, y, z)
                    
                    # Insert keyframe for the bone's location
                    bone.keyframe_insert(data_path="location", frame=frame_number)

    # Save the updated .blend file
    bpy.ops.wm.save_as_mainfile(filepath="C:\\Users\\Dell\\Downloads\\body.blend")
else:
    print(f"Armature 'Armature' not found in collection '{collection_name}'.")