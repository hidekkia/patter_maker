import drawsvg as draw
import math

def calculate_straight_line_length(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.sqrt(dx**2 + dy**2)

def save_pattern(points, filename, piece_style):
    d = draw.Drawing(3500, 4000, style="background: white")
    
    # Labels for Male Pants
    labels_pants_front = [
        "0: A", "1: B", "2: C", "3: D", "4: E", "5: F", "6: G", "7: H",
        "8: I", "9: K", "10: L", "11: M", "12: N", "13: O", "14: P", "15: X"
    ]
    labels_pants_back = [
        "0: A", "1: B", "2: C", "3: D", "4: E", "5: F", "6: G", "7: H",
        "8: I", "9: K", "10: L", "11: M", "12: N", "13: O", "14: P", "15: X",
        "16: M2", "17: N2", "18: O2", "19: P2", "20: Q", "21: R", "22: T",
        "23: U", "24: W", "25: Y", "26: S", "27: Z", "28: Z_dart", "29: Z_left", "30: Z_right"
    ]
    labels_front = [
        "0: A", "1: B", "2: C", "3: D", "4: E", "5: F", "6: G", "7: H",
        "8: I", "9: J", "10: K", "11: L", "12: M", "13: N", "14: O",
        "15: P", "16: Q", "17: R", "18: Dart Point"
    ]
    labels_back = [
        "0: A", "1: B", "2: C", "3: D", "4: E", "5: F", "6: G", "7: I",
        "8: N", "9: P", "10: Q", "11: M"
    ]

    # Draw grid
    for x in range(0, 3500, 72):
        d.append(draw.Line(x, 0, x, 4000, stroke="lightgray", stroke_width=1))
    for y in range(0, 4000, 72):
        d.append(draw.Line(0, y, 3500, y, stroke="lightgray", stroke_width=1))

    padding = 2 * 72

    if piece_style == "standard male pants":
    # Draw front pattern
        if "front" in points:
            coords = points["front"]
            path = draw.Path(stroke="black", stroke_width=2, fill="none")
            segments = []
            path.M(coords[15][0], coords[15][1])  # X
            path.L(coords[6][0], coords[6][1])  # G
            segments.append(("X-G", calculate_straight_line_length(coords[15], coords[6]) / 72,
                            (coords[15][0] + coords[6][0]) / 2, (coords[15][1] + coords[6][1]) / 2))
            control_gf = (coords[6][0] + (coords[5][0] - coords[6][0]) * 0.75, coords[6][1])
            path.Q(control_gf[0], control_gf[1], coords[5][0], coords[5][1])  # F
            control_fd = (coords[5][0] + 50, coords[5][1] + 100)
            path.Q(control_fd[0], control_fd[1], coords[3][0], coords[3][1])  # D
            path.L(coords[7][0], coords[7][1])  # H
            segments.append(("D-H", calculate_straight_line_length(coords[3], coords[7]) / 72,
                            (coords[3][0] + coords[7][0]) / 2, (coords[3][1] + coords[7][1]) / 2))
            mid_hx = ((coords[7][0] + coords[15][0]) / 2, (coords[7][1] + coords[15][1]) / 2)
            control1_hx = (coords[7][0] + 100, coords[7][1])
            control2_hx = (coords[15][0], coords[15][1] + 50)
            path.C(control1_hx[0], control1_hx[1], control2_hx[0], control2_hx[1], coords[15][0], coords[15][1])  # X
            path.M(coords[3][0], coords[3][1])  # D
            path.L(coords[12][0], coords[12][1])  # N
            segments.append(("D-N", calculate_straight_line_length(coords[3], coords[12]) / 72,
                            (coords[3][0] + coords[12][0]) / 2, (coords[3][1] + coords[12][1]) / 2))
            path.L(coords[14][0], coords[14][1])  # P
            segments.append(("N-P", calculate_straight_line_length(coords[12], coords[14]) / 72,
                            (coords[12][0] + coords[14][0]) / 2, (coords[12][1] + coords[14][1]) / 2))
            path.L(coords[13][0], coords[13][1])  # O
            segments.append(("P-O", calculate_straight_line_length(coords[14], coords[13]) / 72,
                            (coords[14][0] + coords[13][0]) / 2, (coords[14][1] + coords[13][1]) / 2))
            path.L(coords[11][0], coords[11][1])  # M
            segments.append(("O-M", calculate_straight_line_length(coords[13], coords[11]) / 72,
                            (coords[13][0] + coords[11][0]) / 2, (coords[13][1] + coords[11][1]) / 2))
            control_mh = (coords[11][0], coords[11][1] - (coords[11][1] - coords[7][1]) * 0.75)
            path.Q(control_mh[0], control_mh[1], coords[7][0], coords[7][1])  # H
            path.M(coords[11][0], coords[11][1])  # M
            path.L(coords[12][0], coords[12][1])  # N
            segments.append(("M-N", calculate_straight_line_length(coords[11], coords[12]) / 72,
                            (coords[11][0] + coords[12][0]) / 2, (coords[11][1] + coords[12][1]) / 2))
            path.M(coords[8][0], coords[8][1])  # I
            path.L(coords[9][0], coords[9][1])  # K
            segments.append(("I-K", calculate_straight_line_length(coords[8], coords[9]) / 72,
                            (coords[8][0] + coords[9][0]) / 2, (coords[8][1] + coords[9][1]) / 2))
            d.append(path)

            for i, (x, y) in enumerate(coords):
                d.append(draw.Circle(x, y, 5, fill="red"))
                label_x = x + 20 if x >= 0 else x - 40
                label_y = y - 10
                d.append(draw.Text(f"{labels_pants_front[i]} ({x/72:.2f}, {y/72:.2f})", 16, label_x, label_y, fill="black"))

            for label, length, mid_x, mid_y in segments:
                offset_x = 30 if mid_x >= 0 else -50
                d.append(draw.Text(f"{length:.2f}\"", 16, mid_x + offset_x, mid_y, fill="blue"))

        if "back" in points:
            coords = points["back"]
            path = draw.Path(stroke="black", stroke_width=2, fill="none")
            segments = []

                    # Start at W
            path.M(coords[24][0], coords[24][1])  # 24: W

            # W to Y: Quadratic Bézier with adjustable control point
            control_wy_x = coords[24][0] + 300  # Fixed offset from W (adjust as needed)
            control_wy_y = coords[24][1] - 100  # Fixed offset from W (adjust as needed)
            path.Q(control_wy_x, control_wy_y, coords[25][0], coords[25][1])  # 25: Y

            # Y to R via Q: Cubic Bézier ensuring passage through Q
            control1_yq_x = coords[25][0] + (coords[20][0] - coords[25][0]) / 2  # Midpoint influence toward Q
            control1_yq_y = coords[25][1] - 50  # Slight upward adjustment for smoothness
            control2_yq_x = coords[20][0]  # Slightly before Q for smooth transition
            control2_yq_y = coords[20][1] + 50  # Adjust downward to curve toward R
            path.C(control1_yq_x, control1_yq_y,  # Control point 1 from Y
                control2_yq_x, control2_yq_y,  # Control point 2 near Q
                coords[21][0], coords[21][1])  # 21: R

            # Continue the rest of the path
            path.L(coords[26][0], coords[26][1])  # 26: S
            segments.append(("R-S", calculate_straight_line_length(coords[21], coords[26]) / 72,
                            (coords[21][0] + coords[26][0]) / 2, (coords[21][1] + coords[26][1]) / 2))
            path.L(coords[22][0], coords[22][1])  # 22: T
            segments.append(("S-T", calculate_straight_line_length(coords[26], coords[22]) / 72,
                            (coords[26][0] + coords[22][0]) / 2, (coords[26][1] + coords[22][1]) / 2))
            path.L(coords[17][0], coords[17][1])  # 17: N2
            segments.append(("T-N2", calculate_straight_line_length(coords[22], coords[17]) / 72,
                            (coords[22][0] + coords[17][0]) / 2, (coords[22][1] + coords[17][1]) / 2))
            path.L(coords[19][0], coords[19][1])  # 19: P2
            segments.append(("N2-P2", calculate_straight_line_length(coords[17], coords[19]) / 72,
                            (coords[17][0] + coords[19][0]) / 2, (coords[17][1] + coords[19][1]) / 2))
            path.L(coords[18][0], coords[18][1])  # 18: O2
            segments.append(("P2-O2", calculate_straight_line_length(coords[19], coords[18]) / 72,
                            (coords[19][0] + coords[18][0]) / 2, (coords[19][1] + coords[18][1]) / 2))
            path.L(coords[16][0], coords[16][1])  # 16: M2
            segments.append(("O2-M2", calculate_straight_line_length(coords[18], coords[16]) / 72,
                            (coords[18][0] + coords[16][0]) / 2, (coords[18][1] + coords[16][1]) / 2))
            control_m2w = (coords[16][0], coords[16][1] -600)
            path.Q(control_m2w[0], control_m2w[1], coords[24][0], coords[24][1])  # 24: W

            dart_path = draw.Path(stroke="red", stroke_width=2, fill="none")

            dart_path.M(coords[27][0], coords[27][1]) #Starting point: Z
            dart_path.L(coords[28][0], coords[28][1]) #Z to Z_dart
            dart_path.L(coords[29][0], coords[29][1]) #Z_dart to Z_left
            dart_path.M(coords[30][0], coords[30][1]) #Starting point: Z_right
            dart_path.L(coords[28][0], coords[28][1]) #Z_right to Z_left

            d.append(path)
            d.append(dart_path)

            # Add points and labels
            for i, (x, y) in enumerate(coords):
                d.append(draw.Circle(x, y, 5, fill="blue"))
                label_x = x + 20 if x >= 0 else x - 40
                label_y = y - 10
                d.append(draw.Text(f"{labels_pants_back[i]} ({x/72:.2f}, {y/72:.2f})", 16, label_x, label_y, fill="black"))

            # Add segment lengths
            for label, length, mid_x, mid_y in segments:
                offset_x = 30 if mid_x >= 0 else -50
                d.append(draw.Text(f"{length:.2f}\"", 16, mid_x + offset_x, mid_y, fill="blue"))

    if piece_style == "GU male pants":
    # Draw front pattern
        if "front" in points:
            coords = points["front"]
            path = draw.Path(stroke="black", stroke_width=2, fill="none")
            dart_path = draw.Path(stroke="red", stroke_width=2, fill="none")
            segments = []
            path.M(coords[15][0], coords[15][1])  # X
            path.L(coords[6][0], coords[6][1])  # G
            segments.append(("X-G", calculate_straight_line_length(coords[15], coords[6]) / 72,
                            (coords[15][0] + coords[6][0]) / 2, (coords[15][1] + coords[6][1]) / 2))
            control_gf = (coords[6][0] + (coords[5][0] - coords[6][0]) * 0.75, coords[6][1])
            path.Q(control_gf[0], control_gf[1], coords[5][0], coords[5][1])  # F
            control_fd = (coords[5][0] + 20, coords[5][1] + 100)
            path.Q(control_fd[0], control_fd[1], coords[3][0], coords[3][1])  # D
            path.L(coords[7][0], coords[7][1])  # H
            segments.append(("D-H", calculate_straight_line_length(coords[3], coords[7]) / 72,
                            (coords[3][0] + coords[7][0]) / 2, (coords[3][1] + coords[7][1]) / 2))
            
            mid_hx = ((coords[7][0] + coords[15][0]) / 2, (coords[7][1] + coords[15][1]) / 2)
            control1_hx = (coords[7][0] + 100, coords[7][1] - 50)
            control2_hx = (coords[15][0], coords[15][1]) # H to X

            path.C(control1_hx[0], control1_hx[1], control2_hx[0], control2_hx[1], coords[15][0], coords[15][1])  # X
            path.M(coords[3][0], coords[3][1])  # D
            path.L(coords[12][0], coords[12][1])  # N
            segments.append(("D-N", calculate_straight_line_length(coords[3], coords[12]) / 72,
                            (coords[3][0] + coords[12][0]) / 2, (coords[3][1] + coords[12][1]) / 2))
            path.L(coords[14][0], coords[14][1])  # P
            segments.append(("N-P", calculate_straight_line_length(coords[12], coords[14]) / 72,
                            (coords[12][0] + coords[14][0]) / 2, (coords[12][1] + coords[14][1]) / 2))
            path.L(coords[13][0], coords[13][1])  # O
            segments.append(("P-O", calculate_straight_line_length(coords[14], coords[13]) / 72,
                            (coords[14][0] + coords[13][0]) / 2, (coords[14][1] + coords[13][1]) / 2))
            path.L(coords[11][0], coords[11][1])  # M
            segments.append(("O-M", calculate_straight_line_length(coords[13], coords[11]) / 72,
                            (coords[13][0] + coords[11][0]) / 2, (coords[13][1] + coords[11][1]) / 2))
            control_mh = (coords[11][0], coords[11][1] - (coords[11][1] - coords[7][1]) * 0.75)
            path.Q(control_mh[0], control_mh[1], coords[7][0], coords[7][1])  # H
            path.M(coords[11][0], coords[11][1])  # M
            path.L(coords[12][0], coords[12][1])  # N
            segments.append(("M-N", calculate_straight_line_length(coords[11], coords[12]) / 72,
                            (coords[11][0] + coords[12][0]) / 2, (coords[11][1] + coords[12][1]) / 2))
            path.M(coords[8][0], coords[8][1])  # I
            path.L(coords[9][0], coords[9][1])  # K
            segments.append(("I-K", calculate_straight_line_length(coords[8], coords[9]) / 72,
                            (coords[8][0] + coords[9][0]) / 2, (coords[8][1] + coords[9][1]) / 2))
            dart_path.M(coords[6][0], coords[6][1])
            dart_path.L(coords[6][0], coords[13][1])
            
            d.append(path)
            d.append(dart_path)

            for i, (x, y) in enumerate(coords):
                d.append(draw.Circle(x, y, 5, fill="red"))
                label_x = x + 20 if x >= 0 else x - 40
                label_y = y - 10
                d.append(draw.Text(f"{labels_pants_front[i]} ({x/72:.2f}, {y/72:.2f})", 16, label_x, label_y, fill="black"))

            for label, length, mid_x, mid_y in segments:
                offset_x = 30 if mid_x >= 0 else -50
                d.append(draw.Text(f"{length:.2f}\"", 16, mid_x + offset_x, mid_y, fill="blue"))

        if "back" in points:
            coords = points["back"]
            path = draw.Path(stroke="black", stroke_width=2, fill="none")
            segments = []

                    # Start at W
            path.M(coords[24][0], coords[24][1])  # 24: W

            # W to Y: Quadratic Bézier with adjustable control point
            control_wy_x = coords[24][0] + 150  # Fixed offset from W (adjust as needed)
            control_wy_y = coords[24][1] - 50  # Fixed offset from W (adjust as needed)
            path.Q(control_wy_x, control_wy_y, coords[15][0], coords[15][1])  # 25: Y

            # Y to R via Q: Cubic Bézier ensuring passage through Q
            path.L(coords[21][0], coords[21][1])
            path.L(coords[26][0], coords[26][1])

            # Continue the rest of the path
            path.L(coords[26][0], coords[26][1])  # 26: S
            segments.append(("R-S", calculate_straight_line_length(coords[21], coords[26]) / 72,
                            (coords[21][0] + coords[26][0]) / 2, (coords[21][1] + coords[26][1]) / 2))
            path.L(coords[22][0], coords[22][1])  # 22: T
            segments.append(("S-T", calculate_straight_line_length(coords[26], coords[22]) / 72,
                            (coords[26][0] + coords[22][0]) / 2, (coords[26][1] + coords[22][1]) / 2))
            path.L(coords[17][0], coords[17][1])  # 17: N2
            segments.append(("T-N2", calculate_straight_line_length(coords[22], coords[17]) / 72,
                            (coords[22][0] + coords[17][0]) / 2, (coords[22][1] + coords[17][1]) / 2))
            path.L(coords[19][0], coords[19][1])  # 19: P2
            segments.append(("N2-P2", calculate_straight_line_length(coords[17], coords[19]) / 72,
                            (coords[17][0] + coords[19][0]) / 2, (coords[17][1] + coords[19][1]) / 2))
            path.L(coords[18][0], coords[18][1])  # 18: O2
            segments.append(("P2-O2", calculate_straight_line_length(coords[19], coords[18]) / 72,
                            (coords[19][0] + coords[18][0]) / 2, (coords[19][1] + coords[18][1]) / 2))
            path.L(coords[16][0], coords[16][1])  # 16: M2
            segments.append(("O2-M2", calculate_straight_line_length(coords[18], coords[16]) / 72,
                            (coords[18][0] + coords[16][0]) / 2, (coords[18][1] + coords[16][1]) / 2))
            control_m2w = (coords[16][0], coords[16][1] -600)
            path.Q(control_m2w[0], control_m2w[1], coords[24][0], coords[24][1])  # 24: W

            dart_path = draw.Path(stroke="red", stroke_width=2, fill="none")

            dart_path.M(coords[27][0], coords[27][1]) #Starting point: Z
            dart_path.L(coords[28][0], coords[28][1]) #Z to Z_dart
            dart_path.L(coords[29][0], coords[29][1]) #Z_dart to Z_left
            dart_path.M(coords[30][0], coords[30][1]) #Starting point: Z_right
            dart_path.L(coords[28][0], coords[28][1]) #Z_right to Z_left

            dart_path.M(coords[21][0], coords[21][1])
            dart_path.L(coords[21][0], coords[18][1])

            d.append(path)
            d.append(dart_path)

            # Add points and labels
            for i, (x, y) in enumerate(coords):
                d.append(draw.Circle(x, y, 5, fill="blue"))
                label_x = x + 20 if x >= 0 else x - 40
                label_y = y - 10
                d.append(draw.Text(f"{labels_pants_back[i]} ({x/72:.2f}, {y/72:.2f})", 16, label_x, label_y, fill="black"))

            # Add segment lengths
            for label, length, mid_x, mid_y in segments:
                offset_x = 30 if mid_x >= 0 else -50
                d.append(draw.Text(f"{length:.2f}\"", 16, mid_x + offset_x, mid_y, fill="blue"))

    if piece_style == "women top":
        d = draw.Drawing(3500, 4000, style="background: white")
        padding = 2 * 72  # 144
        scale = 72

        labels_front = [
            "0: A", "1: B", "2: C", "3: C1", "4: D", "5: D1", "6: E", "7: E1",
            "8: G", "9: H", "10: I", "11: J", "12: K", "13: L", "14: M", "15: F",
            "16: F1", "17: N", "18: O", "19: P", "20: Q", "21: R", "22: K'", 
            "23: Neck Point", "24: I'"
        ]

        # Draw grid
        for x in range(0, 3500, 72):
            d.append(draw.Line(x, 0, x, 4000, stroke="lightgray", stroke_width=1))
        for y in range(0, 4000, 72):
            d.append(draw.Line(0, y, 3500, y, stroke="lightgray", stroke_width=1))

        if "front" in points:
            coords = points["front"]
            for i, (x, y) in enumerate(coords):
                if i == 20:  # Q remains green as per your original
                    d.append(draw.Circle(x, y, 5, fill="green"))
                else:
                    d.append(draw.Circle(x, y, 5, fill="red"))
                label_x = x + 20 if (x - padding) >= 0 else x - 40
                label_y = y - 10
                inch_x = (x - padding) / scale
                inch_y = (y - padding) / scale
                d.append(draw.Text(f"{labels_front[i]} ({inch_x:.2f}, {inch_y:.2f})", 16, label_x, label_y, fill="black"))

            path = draw.Path(stroke='black', stroke_width='2', fill='none')
            guideline = draw.Path(stroke='red', stroke_width='0.7', fill='none')
            
            #C1 to C to A
            guideline.M(coords[3][0], coords[3][1])
            guideline.L(coords[2][0], coords[2][1])
            guideline.L(coords[0][0], coords[0][1])

            # O guideline and O to E to B guidelines
            guideline.M(coords[18][0] + 100, coords[18][1])
            guideline.L(coords[18][0], coords[18][1])
            guideline.L(coords[6][0], coords[6][1])
            guideline.L(coords[1][0], coords[1][1])

            # G to B (guideline)
            guideline.M(coords[8][0], coords[8][1])
            guideline.L(coords[1][0], coords[1][1])

            #L to M
            guideline.M(coords[13][0], coords[13][1])
            guideline.L(coords[14][0], coords[14][1])

            #F to K to G
            guideline.M(coords[15][0], coords[15][1])
            guideline.L(coords[12][0], coords[12][1])
            guideline.L(coords[20][0], coords[20][1])

            # M guideline
            guideline.M(coords[14][0], coords[14][1] - 100)
            guideline.L(coords[14][0], coords[14][1] + 100)

            # D guideline (updated to show I' intersection)
            guideline.M(coords[4][0], coords[4][1])
            guideline.L(coords[5][0], coords[5][1])

            # I guideline (squared line from I) and I to N guideline
            guideline.M(coords[24][0], coords[24][1])
            guideline.L(coords[10][0], coords[10][1])
            guideline.L(coords[17][0], coords[17][1])

    



            # D to B
            path.M(coords[4][0], coords[4][1])  # Starting point: D
            path.L(coords[1][0], coords[1][1])  # D to B

            # B to F1 (corrected from F, with control point)
            control_bf = (coords[16][0] + 40, coords[16][1] - 17)
            path.Q(control_bf[0], control_bf[1], coords[16][0], coords[16][1])

            # F1 to K' and K' to R
            path.L(coords[22][0], coords[22][1])
            path.L(coords[21][0], coords[21][1])

            # R to P (with control point) and P to O
            control_rq = (coords[21][0] - 40, coords[21][1] - 20)
            path.Q(control_rq[0], control_rq[1], coords[19][0], coords[19][1])
            path.L(coords[18][0], coords[18][1])

            # O to G (with control points)
            control_om = (coords[18][0] + 100, coords[18][1] + 1)  # pivoting at point O
            control_mg = (coords[14][0] + 90, coords[14][1] + 50)  # pivoting at point M
            path.C(control_om[0], control_om[1], control_mg[0], control_mg[1], coords[8][0], coords[8][1])

            # G to I
            path.M(coords[8][0], coords[8][1])
            path.L(coords[10][0], coords[10][1])

            # I to D neck curved line (with control point)
            control_id = (coords[10][0], coords[10][1] + 55) # pivot at point I
            control_line_i = (coords[24][0] - 35, coords[24][1]) #Pivot at point I'
            path.C(control_id[0], control_id[1], control_line_i[0], control_line_i[1], coords[4][0], coords[4][1])
            d.append(guideline)

    # Add piece label
    d.append(draw.Text("Front", 36, padding + 50, 50, fill="black"))
    d.append(draw.Text("Back", 36, padding + 1250, 50, fill="black"))
    d.append(path)
    d.save_svg(filename)