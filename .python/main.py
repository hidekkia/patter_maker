from pattern_logic import generate_points
from svg_generator import save_pattern

measurements = {
    "Waist": 36,
    "Hip": 37,
    "Rise": 10,
    "Leg Length": 42,
    "Knee Width": 13,
    "Leg Width": 13,
    "Knee Adjust Right": 2.5,
    "Knee Adjust Left": 0,
    "Leg Adjust Right": 3,
    "Leg Adjust Left": 0,
    "Dart Depth": 3.5,
    "wy_adjust_x": 1.5,  # Depth adjustment in inches (positive = right)
    "wy_adjust_y": -0.75,  # Height adjustment in inches (negative = up)

    "Pocket Height": 0,
    "Pokeckt WIdth": 0,
    "Bottom Leg Darts": 0,
    "Knee Darts": 0,

    "Bust arc": 8.625,
    "Back arc": 8.625,
    "Waist arc Front": 6.8125,
    "Waist arc Back": 6.8125,
    "Center length Front": 14.5,
    "Center length Back": 16.5,
    "Full length Front": 17.25,
    "Full length Back": 17.0,
    "Shoulder slope Front": 17.5,
    "Shoulder slope Back": 16.75,
    "New Strap": 17.25,
    "Bust depth": 9.5,
    "Bust span": 3.75,
    "Side length": 8.5,
    "Back neck": 2.75,
    "Shoulder length": 5.0,
    "Across shoulder Front": 7.75,
    "Across shoulder Back": 8.0,
    "Across chest": 6.75,
    "Across back": 7.0,
    "Dart Placement Front": 3.25,
    "Dart Placement Back": 3.25
}

piece_style = "GU male pants"
file_name = "GU_pattern_points.svg"

points = generate_points(piece_style, measurements)
# Add wy_adjust to points dictionary
points["wy_adjust_x"] = measurements["wy_adjust_x"]
points["wy_adjust_y"] = measurements["wy_adjust_y"]
save_pattern(points, file_name, piece_style)