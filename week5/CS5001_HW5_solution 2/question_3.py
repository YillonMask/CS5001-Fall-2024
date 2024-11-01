"""
Loops in Autonomous Driving System Using Bounding Box Detection
"""


# Function to calculate the area of bounding boxes
def calculate_area(bounding_boxes):
    areas = {}
    for obj_id, box in bounding_boxes.items():
        area = (box['x2'] - box['x1']) * (box['y2'] - box['y1'])
        areas[obj_id] = area
    return areas


# Function to detect overlapping bounding boxes
def detect_overlapping(bounding_boxes):
    ids = list(bounding_boxes.keys())
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            box1 = bounding_boxes[ids[i]]
            box2 = bounding_boxes[ids[j]]
            if (box1['x1'] < box2['x2'] and box1['x2'] > box2['x1'] and
                    box1['y1'] < box2['y2'] and box1['y2'] > box2['y1']):
                print(f"Bounding boxes {ids[i]} and {ids[j]} overlap.")


# Function to track moving objects over multiple frames
def track_moving_objects(bounding_boxes, movement_vector, frames=5):
    print("Tracking moving objects:")
    for frame in range(frames):
        for obj_id, box in bounding_boxes.items():
            box['x1'] += movement_vector['dx']
            box['y1'] += movement_vector['dy']
            box['x2'] += movement_vector['dx']
            box['y2'] += movement_vector['dy']
        print(f"Frame {frame + 1}: {bounding_boxes}")


# Function to merge overlapping bounding boxes
def merge_overlapping(bounding_boxes):
    ids = list(bounding_boxes.keys())
    # for loop to check for overlapping boxes
    for i in range(len(ids)):
        # Check if the box has already been merged
        if ids[i] not in bounding_boxes:
            continue
        for j in range(i + 1, len(ids)):
            # Check if the box has already been merged
            if ids[j] not in bounding_boxes:
                continue
            box1 = bounding_boxes[ids[i]]
            box2 = bounding_boxes[ids[j]]
            if (box1['x1'] < box2['x2'] and box1['x2'] > box2['x1'] and
                    box1['y1'] < box2['y2'] and box1['y2'] > box2['y1']):
                # Merge the boxes
                new_box = {
                    'x1': min(box1['x1'], box2['x1']),
                    'y1': min(box1['y1'], box2['y1']),
                    'x2': max(box1['x2'], box2['x2']),
                    'y2': max(box1['y2'], box2['y2'])
                }
                # Remove old boxes and add new merged box
                del bounding_boxes[ids[j]]  # Remove the second box
                bounding_boxes[ids[i]] = new_box  # Update the first box


# Running the functions
bounding_boxes = {
    1: {'x1': 50, 'y1': 100, 'x2': 200, 'y2': 250},
    2: {'x1': 300, 'y1': 400, 'x2': 350, 'y2': 450},
    3: {'x1': 150, 'y1': 150, 'x2': 250, 'y2': 250}
}
print("Bounding Boxes:", bounding_boxes)
print('\n')

print("Areas of Bounding Boxes:")
areas = calculate_area(bounding_boxes)
print(areas)
print('\n')

print("Detecting Overlapping Bounding Boxes:")
detect_overlapping(bounding_boxes)
print('\n')

movement_vector = {'dx': 10, 'dy': -5}
track_moving_objects(bounding_boxes, movement_vector)
print('\n')

print("Merging Overlapping Bounding Boxes:")
merge_overlapping(bounding_boxes)
print("Merged Bounding Boxes:", bounding_boxes)

# Multiple overlapping bounding boxes
bounding_boxes_2 = {
    1: {'x1': 0, 'y1': 0, 'x2': 2, 'y2': 2},
    2: {'x1': 1, 'y1': 1, 'x2': 3, 'y2': 3},
    3: {'x1': 2, 'y1': 2, 'x2': 4, 'y2': 4}
}
print("\nBounding Boxes 2:", bounding_boxes_2)
print('\n')

print("Areas of Bounding Boxes:")
areas = calculate_area(bounding_boxes_2)
print(areas)
print('\n')

print("Detecting Overlapping Bounding Boxes:")
detect_overlapping(bounding_boxes_2)
print('\n')

movement_vector = {'dx': 1, 'dy': -1}
track_moving_objects(bounding_boxes_2, movement_vector)
print('\n')

print("Merging Overlapping Bounding Boxes2:")
merge_overlapping(bounding_boxes_2)
print("Merged Bounding Boxes:", bounding_boxes_2)
