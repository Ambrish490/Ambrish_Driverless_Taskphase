def sort_by_proximity(coordinates, ref_point):
    ref_x, ref_y = ref_point
    
   
    sorted_coords = sorted(
        coordinates, 
        key=lambda point: (point[0] - ref_x)**2 + (point[1] - ref_y)**2
    )
    return sorted_coords

# --- Example Usage ---
coords_list = [(0, 1), (0, 3), (1, 2)]
reference_point = (0, 0)

result = sort_by_proximity(coords_list, reference_point)
print(f"Original list: {coords_list}")
print(f"Reference point: {reference_point}")
print(f"Sorted by proximity: {result}")