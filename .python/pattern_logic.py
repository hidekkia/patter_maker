import numpy as np
import math

def generate_points(piece_style, measurements):
    # --- Extract Measurements with Defaults ---
    if piece_style == "standard male pants":
        waist = measurements.get("Waist")
        hip = measurements.get("Hip")
        rise = measurements.get("Rise")
        leg_length = measurements.get("Leg Length")
        knee_width = measurements.get("Knee Width")
        leg_width = measurements.get("Leg Width")
        knee_adjust_right = measurements.get("Knee Adjust Right", 0)
        knee_adjust_left = measurements.get("Knee Adjust Left", 0)
        leg_adjust_right = measurements.get("Leg Adjust Right", 0)
        leg_adjust_left = measurements.get("Leg Adjust Left", 0)
        dart_depth = measurements.get("Dart Depth", 0)

        # --- Base Rectangle for Front and Back ---
        rect_width = hip / 4 - 0.5
        rect_height = rise

        # Corrected Rectangle Points
        a = (0, 0)           # Index 0: A
        c = (rect_width, 0)  # Index 2: C
        b = (0, rise)        # Index 1: B
        d = (rect_width+1, rise)  # Index 3: D

        # --- Front Pattern Points ---
        e = (0.59, 0)        # Index 4: E
        g = (0.59, 0.39)     # Index 6: G
        f = (waist / 4 + 0.59, 0)   # Index 5: F
        h = (-hip / 16, rise)  # Index 7: H
        x = (0, rise - 2.5)  # Index 15: X
        h_to_d = math.sqrt((d[0] - h[0])**2 + (d[1] - h[1])**2)
        i_x = h[0] + h_to_d / 2
        i = (i_x, rise)      # Index 8: I
        k = (i_x, leg_length)  # Index 9: K
        i_to_k = leg_length
        knee_y = (i_to_k / 2 - 5) + rise
        l = (i_x, knee_y)    # Index 10: L
        m = (i_x - knee_width / 4 - 1 - knee_adjust_left, knee_y)  # Index 11: M
        n = (i_x + knee_width / 4 + 1 + knee_adjust_right, knee_y)  # Index 12: N
        o = (i_x - leg_width / 4 - 1 - leg_adjust_left, k[1])  # Index 13: O
        p = (i_x + leg_width / 4 + 1 + leg_adjust_right, k[1])  # Index 14: P

        front_points = [
            a,  # 0: A
            b,  # 1: B
            c,  # 2: C
            d,  # 3: D
            e,  # 4: E
            f,  # 5: F
            g,  # 6: G
            h,  # 7: H
            i,  # 8: I
            k,  # 9: K
            l,  # 10: L
            m,  # 11: M
            n,  # 12: N
            o,  # 13: O
            p,  # 14: P
            x   # 15: X
        ]

        # --- Back Pattern Points ---
        back_a = a  # 0: A
        back_b = b  # 1: B
        back_c = c  # 2: C
        back_d = d  # 3: D
        back_e = e  # 4: E
        back_f = f  # 5: F
        back_g = g  # 6: G
        back_h = h  # 7: H
        back_i = i  # 8: I
        back_k = k  # 9: K
        back_l = l  # 10: L
        back_m = m  # 11: M
        back_n = n  # 12: N
        back_o = o  # 13: O
        back_p = p  # 14: P
        back_x = x  # 15: X

        # Step 1: M2 and N2
        m2 = (back_m[0] - 0.7874, back_m[1])  # 16: M2
        n2 = (back_n[0] + 0.7874, back_n[1])  # 17: N2

        # Step 2: O2 and P2
        o2 = (back_o[0] - 0.7874, back_o[1])  # 18: O2
        p2 = (back_p[0] + 0.7874, back_p[1])  # 19: P2

        # Step 3: Q
        q = (back_e[0] + 1.1811, back_e[1])  # 20: Q

        # Step 5: R
        v_x = q[0] - back_b[0]
        v_y = q[1] - back_b[1]
        v_norm = math.sqrt(v_x**2 + v_y**2)
        r_x = q[0] + 1.1811 * (v_x / v_norm)
        r_y = q[1] + 1.1811 * (v_y / v_norm)
        r = (r_x, r_y)  # 21: R

        # Step 6: T
        t = (back_d[0] + 1.1811, back_d[1])  # 22: T

        # Step 7: U
        u = (back_b[0] - hip / 8, back_b[1])  # 23: U


        # Step 8: W
        w = (u[0], u[1] + 0.3937)  # 24: W

        # Step 9: Y
        vr_x = r[0] - back_b[0]
        vr_y = r[1] - back_b[1]
        vr_norm = math.sqrt(vr_x**2 + vr_y**2)
        y_x = back_b[0] + 4.7244 * (vr_x / vr_norm)
        y_y = back_b[1] + 4.7244 * (vr_y / vr_norm)
        y = (y_x, y_y)  # 25: Y



        # Step 10: S
        vc_x = back_c[0] - r[0]
        vc_y = back_c[1] - r[1]
        vc_norm = math.sqrt(vc_x**2 + vc_y**2)
        s_x = r[0] + (waist / 4 + 2) * (vc_x / vc_norm)
        s_y = r[1] + (waist / 4 + 2) * (vc_y / vc_norm)
        s = (s_x, s_y)  # 26: S

        # Step 11: Z
        z_x = (r[0] + s[0]) / 2
        z_y = (r[1] + s[1]) / 2
        z = (z_x, z_y)  # 27: Z

        # Step 12: Z_dart
        vs_x = s[0] - r[0]
        vs_y = s[1] - r[1]
        p_x = -vs_y
        p_y = vs_x
        p_norm = math.sqrt(p_x**2 + p_y**2)
        up_x = p_x / p_norm
        up_y = p_y / p_norm
        z_dart = (z[0] + dart_depth * up_x, z[1] + dart_depth * up_y)  # 28: Z_dart

        # Step 13: Z_left and Z_right
        vs_norm = math.sqrt(vs_x**2 + vs_y**2)
        us_x = vs_x / vs_norm
        us_y = vs_y / vs_norm
        z_left = (z[0] - 0.3937 * us_x, z[1] - 0.3937 * us_y)  # 29: Z_left
        z_right = (z[0] + 0.3937 * us_x, z[1] + 0.3937 * us_y)  # 30: Z_right

        back_points = [
            back_a,    # 0: A
            back_b,    # 1: B
            back_c,    # 2: C
            back_d,    # 3: D
            back_e,    # 4: E
            back_f,    # 5: F
            back_g,    # 6: G
            back_h,    # 7: H
            back_i,    # 8: I
            back_k,    # 9: K
            back_l,    # 10: L
            back_m,    # 11: M
            back_n,    # 12: N
            back_o,    # 13: O
            back_p,    # 14: P
            back_x,    # 15: X
            m2,        # 16: M2
            n2,        # 17: N2
            o2,        # 18: O2
            p2,        # 19: P2
            q,         # 20: Q
            r,         # 21: R
            t,         # 22: T
            u,         # 23: U
            w,         # 24: W
            y,         # 25: Y
            s,         # 26: S
            z,         # 27: Z
            z_dart,    # 28: Z_dart
            z_left,    # 29: Z_left
            z_right    # 30: Z_right
        ]
    
    elif piece_style == "GU male pants":
        waist = measurements.get("Waist")
        hip = measurements.get("Hip")
        rise = measurements.get("Rise")
        leg_length = measurements.get("Leg Length")
        knee_width = measurements.get("Knee Width")
        leg_width = measurements.get("Leg Width")
        knee_adjust_right = measurements.get("Knee Adjust Right", 0)
        knee_adjust_left = measurements.get("Knee Adjust Left", 0)
        leg_adjust_right = measurements.get("Leg Adjust Right", 0)
        leg_adjust_left = measurements.get("Leg Adjust Left", 0)
        dart_depth = measurements.get("Dart Depth", 0)

        # --- Base Rectangle for Front and Back ---
        rect_width = hip / 4 + 1
        rect_height = rise

        # Corrected Rectangle Points
        a = (0, 0)           # Index 0: A
        c = (rect_width, 0)  # Index 2: C
        b = (0.5, rise)        # Index 1: B
        d = (rect_width, rise)  # Index 3: D

        # --- Front Pattern Points ---
        e = (0.59, 0)        # Index 4: E
        g = (0.59, 0.39)     # Index 6: G
        f = (waist / 4 + 0.59, 0)   # Index 5: F
        h = (-hip / 16, rise)  # Index 7: H
        x = (0, rise - 2.5)  # Index 15: X
        h_to_d = math.sqrt((d[0] - h[0])**2 + (d[1] - h[1])**2)
        i_x = h[0] + h_to_d / 2
        i = (i_x, rise)      # Index 8: I
        k = (i_x, leg_length)  # Index 9: K
        i_to_k = leg_length
        knee_y = (i_to_k / 2 - 5) + rise
        l = (i_x, knee_y)    # Index 10: L
        m = (i_x - knee_width / 4 - 1 - knee_adjust_left, knee_y)  # Index 11: M
        n = (i_x + knee_width / 4 + 1 + knee_adjust_right, knee_y)  # Index 12: N
        o = (i_x - leg_width / 4 - 1 - leg_adjust_left, k[1])  # Index 13: O
        p = (i_x + leg_width / 4 + 1 + leg_adjust_right, k[1])  # Index 14: P

        front_points = [
            a,  # 0: A
            b,  # 1: B
            c,  # 2: C
            d,  # 3: D
            e,  # 4: E
            f,  # 5: F
            g,  # 6: G
            h,  # 7: H
            i,  # 8: I
            k,  # 9: K
            l,  # 10: L
            m,  # 11: M
            n,  # 12: N
            o,  # 13: O
            p,  # 14: P
            x   # 15: X
        ]

        # --- Back Pattern Points ---
        back_a = a  # 0: A
        back_b = b  # 1: B
        back_c = c  # 2: C
        back_d = d  # 3: D
        back_e = e  # 4: E
        back_f = f  # 5: F
        back_g = g  # 6: G
        back_h = h  # 7: H
        back_i = i  # 8: I
        back_k = k  # 9: K
        back_l = l  # 10: L
        back_m = m  # 11: M
        back_n = n  # 12: N
        back_o = o  # 13: O
        back_p = p  # 14: P
        back_x = x  # 15: X

        # Step 1: M2 and N2
        m2 = (back_m[0] - 0.7874, back_m[1])  # 16: M2
        n2 = (back_n[0] + 0.7874, back_n[1])  # 17: N2

        # Step 2: O2 and P2
        o2 = (back_o[0] - 0.7874, back_o[1])  # 18: O2
        p2 = (back_p[0] + 0.7874, back_p[1])  # 19: P2

        # Step 3: Q
        q = (back_e[0] + 1.1811, back_e[1])  # 20: Q

        # Step 5: R
        v_x = q[0] - back_b[0]
        v_y = q[1] - back_b[1]
        v_norm = math.sqrt(v_x**2 + v_y**2)
        r_x = q[0] + 1.1811 * (v_x / v_norm)
        r_y = q[1] + 1.1811 * (v_y / v_norm)
        r = (r_x, r_y)  # 21: R

        # Step 6: T
        t = (back_d[0] + 1.1811, back_d[1])  # 22: T

        # Step 7: U
        u = (r[0] - hip / 6.8, back_b[1])  # 23: U


        # Step 8: W
        w = (u[0], u[1] + 0.3937)  # 24: W

        # Step 9: Y
        vr_x = r[0] - back_b[0]
        vr_y = r[1] - back_b[1]
        vr_norm = math.sqrt(vr_x**2 + vr_y**2)
        y_x = back_b[0] + 4.7244 * (vr_x / vr_norm)
        y_y = back_b[1] + 4.7244 * (vr_y / vr_norm)
        y = (y_x, y_y)  # 25: Y



        # Step 10: S
        vc_x = back_c[0] - r[0]
        vc_y = back_c[1] - r[1]
        vc_norm = math.sqrt(vc_x**2 + vc_y**2)
        s_x = r[0] + (waist / 4 + 1.25) * (vc_x / vc_norm)
        s_y = r[1] + (waist / 4 + 1.25) * (vc_y / vc_norm)
        s = (s_x, s_y)  # 26: S

        # Step 11: Z
        z_x = (r[0] + s[0]) / 2
        z_y = (r[1] + s[1]) / 2
        z = (z_x, z_y)  # 27: Z

        # Step 12: Z_dart
        vs_x = s[0] - r[0]
        vs_y = s[1] - r[1]
        p_x = -vs_y
        p_y = vs_x
        p_norm = math.sqrt(p_x**2 + p_y**2)
        up_x = p_x / p_norm
        up_y = p_y / p_norm
        z_dart = (z[0] + dart_depth * up_x, z[1] + dart_depth * up_y)  # 28: Z_dart

        # Step 13: Z_left and Z_right
        vs_norm = math.sqrt(vs_x**2 + vs_y**2)
        us_x = vs_x / vs_norm
        us_y = vs_y / vs_norm
        z_left = (z[0] - 0.3937 * us_x, z[1] - 0.3937 * us_y)  # 29: Z_left
        z_right = (z[0] + 0.3937 * us_x, z[1] + 0.3937 * us_y)  # 30: Z_right

        back_points = [
            back_a,    # 0: A
            back_b,    # 1: B
            back_c,    # 2: C
            back_d,    # 3: D
            back_e,    # 4: E
            back_f,    # 5: F
            back_g,    # 6: G
            back_h,    # 7: H
            back_i,    # 8: I
            back_k,    # 9: K
            back_l,    # 10: L
            back_m,    # 11: M
            back_n,    # 12: N
            back_o,    # 13: O
            back_p,    # 14: P
            back_x,    # 15: X
            m2,        # 16: M2
            n2,        # 17: N2
            o2,        # 18: O2
            p2,        # 19: P2
            q,         # 20: Q
            r,         # 21: R
            t,         # 22: T
            u,         # 23: U
            w,         # 24: W
            y,         # 25: Y
            s,         # 26: S
            z,         # 27: Z
            z_dart,    # 28: Z_dart
            z_left,    # 29: Z_left
            z_right    # 30: Z_right
        ]
    
    elif piece_style == "women top":

# Extract measurements
        full_length_front = measurements.get("Full length Front", 16.875)
        across_shoulder_front = measurements.get("Across shoulder Front", 7.5)
        center_length_front = measurements.get("Center length Front", 14.125)
        bust_arc = measurements.get("Bust arc", 9.5)
        shoulder_slope_front = measurements.get("Shoulder slope Front", 17.0625)
        shoulder_length = measurements.get("Shoulder length", 5.125)
        bust_span = measurements.get("Bust span", 3.625)
        across_chest = measurements.get("Across chest", 6.5)
        dart_placement = measurements.get("Dart Placement Front", 3)
        bust_depth = measurements.get("Bust depth", 9.125)
        new_strap = measurements.get("New Strap", 17)
        side_length = measurements.get("Side length", 8.125)
        waist_arc_front = measurements.get("Waist arc Front", 6.5)

        # Step 1 points
        base_x = bust_arc + 0.25  # 9.75
        a = (base_x, 0)  # A: 9.75, 0
        b = (base_x, full_length_front + 0.125)  # B: 9.75, 17
        c = (base_x - (across_shoulder_front - 0.125), 0)  # C: 2.375, 0
        c1 = (c[0], c[1] + 3)  # C1: 2.375, 3
        d = (base_x, b[1] - center_length_front)  # D: 9.75, 2.875
        d1 = (base_x - 4, d[1])  # D1: 5.75, 2.875
        e = (base_x - (bust_arc + 0.25), b[1])  # E: 0, 17
        e1 = (e[0], e[1] - 11)  # E1: 0, 6

        # Step 2 points
        shoulder_slope_length = shoulder_slope_front + 0.125  # 17.1875
        dx_bg = c[0] - b[0]  # -7.375
        dy_bg = math.sqrt(shoulder_slope_length**2 - dx_bg**2)  # ≈ 15.5244
        g = (c[0], b[1] - dy_bg)  # G: 2.375, 1.4756

        gb_vector = (b[0] - g[0], b[1] - g[1])  # (7.375, 15.5244)
        gb_length = math.sqrt(gb_vector[0]**2 + gb_vector[1]**2)  # 17.1875
        unit_gb = (gb_vector[0] / gb_length, gb_vector[1] / gb_length)  # (0.429, 0.903)
        h = (g[0] + unit_gb[0] * bust_depth, g[1] + unit_gb[1] * bust_depth)  # H: ≈ (6.2896, 9.7155)

        i = (g[0] + shoulder_length, 0)  # I: 7.5, 0
        j = (base_x, h[1])  # J: 9.75, 9.7155
        k = (j[0] - (bust_span + 0.25), j[1])  # K: 5.875, 9.7155
        dj_distance = abs(d[1] - j[1])  # 6.8405
        l = (d[0], d[1] + dj_distance / 2)  # L: 9.75, 6.29525
        m = (l[0] - (across_chest + 0.25), l[1])  # M: 3, 6.29525
        f = (b[0] - dart_placement, b[1])  # F: 6.75, 17
        f1 = (f[0], f[1] + 3/16)  # F1: 6.75, 17.1875

        # Step 3 points
        strap_length = new_strap + 0.125  # 17.125
        dx_in = e[0] - i[0]  # -7.5
        dy_in = math.sqrt(strap_length**2 - dx_in**2)  # ≈ 15.395
        n = (e[0], i[1] + dy_in)  # N: 0, 15.395
        o = (n[0], n[1] - side_length)  # O: 0, 7.27
        p = (n[0] - 1.25, n[1])  # P: -1.25, 15.395

        # Step 4 points
        # Q: On P to F1, distance = Waist arc + 1/4" - (B to F)
        bf_distance = abs(b[0] - f[0])  # 3" (B to F as per instruction)
        q_distance = waist_arc_front + 0.25 - bf_distance  # 6.5 + 0.25 - 3 = 3.75
        pf1_vector = (f1[0] - p[0], f1[1] - p[1])  # (8, 1.7925)
        pf1_length = math.sqrt(pf1_vector[0]**2 + pf1_vector[1]**2)  # ≈ 8.203
        unit_pf1 = (pf1_vector[0] / pf1_length, pf1_vector[1] / pf1_length)  # ≈ (0.975, 0.218)
        q = (p[0] + unit_pf1[0] * q_distance, p[1] + unit_pf1[1] * q_distance)  # Q: ≈ (2.41, 16.21)

        # R: From K, length K to F1, through updated Q
        kf1_distance = math.sqrt((f1[0] - k[0])**2 + (f1[1] - k[1])**2)  # ≈ 7.523
        kq_vector = (q[0] - k[0], q[1] - k[1])  # ≈ (-3.465, 6.4945)
        kq_length = math.sqrt(kq_vector[0]**2 + kq_vector[1]**2)  # ≈ 7.36
        unit_kq = (kq_vector[0] / kq_length, kq_vector[1] / kq_length)  # ≈ (-0.471, 0.882)
        r = (k[0] + unit_kq[0] * kf1_distance, k[1] + unit_kq[1] * kf1_distance)  # R: ≈ (2.33, 16.35)

        # K': At bisector of angle FKQ, 0.625" from K
        fk_vec = (f[0] - k[0], f[1] - k[1])  # (-0.875, 7.41)
        kq_vec = (q[0] - k[0], q[1] - k[1])  # (-2.43, 6.845)
        fk_len = math.sqrt(fk_vec[0]**2 + fk_vec[1]**2)  # ≈ 7.46
        kq_len = math.sqrt(kq_vec[0]**2 + kq_vec[1]**2)  # ≈ 7.26
        unit_fk = (fk_vec[0] / fk_len, fk_vec[1] / fk_len)  # ≈ (-0.117, 0.993)
        unit_kq = (kq_vec[0] / kq_len, kq_vec[1] / kq_len)  # ≈ (-0.335, 0.942)
        bisector_vec = (unit_fk[0] + unit_kq[0], unit_fk[1] + unit_kq[1])  # (-0.452, 1.935)
        bisector_len = math.sqrt(bisector_vec[0]**2 + bisector_vec[1]**2)  # ≈ 1.987
        unit_bisector = (bisector_vec[0] / bisector_len, bisector_vec[1] / bisector_len)  # ≈ (-0.227, 0.974)
        k_prime = (k[0] + unit_bisector[0] * 0.625, k[1] + unit_bisector[1] * 0.625)  # K': ≈ (5.483, 10.449)

        # I': Intersection of perpendicular from G-I with D-D1
        slope_gi = (i[1] - g[1]) / (i[0] - g[0])  # ≈ -0.2879
        perp_slope = -1 / slope_gi  # ≈ 3.473
        x_iprime = (d[1] + perp_slope * i[0]) / perp_slope  # ≈ 8.328
        i_prime = (x_iprime, d[1])  # I': (8.328, 2.875)

        # Neck Point: Midpoint of I to I' with 1/8" perpendicular line (left/up)
        mid_ii_prime = ((i[0] + i_prime[0]) / 2, (i[1] + i_prime[1]) / 2)  # (7.914, 1.4375)
        ii_prime_vec = (i_prime[0] - i[0], i_prime[1] - i[1])  # (0.828, 2.875)
        perp_length = math.sqrt(ii_prime_vec[0]**2 + ii_prime_vec[1]**2)  # ≈ 2.989
        perp_vec = (-ii_prime_vec[1] / perp_length, ii_prime_vec[0] / perp_length)  # ≈ (-0.962, 0.277)
        neck_point = (mid_ii_prime[0] + perp_vec[0] * 0.125, mid_ii_prime[1] + perp_vec[1] * 0.125)  # ≈ (7.794, 1.472)

        front_points = [
            a, b, c, c1, d, d1, e, e1,  # Step 1
            g, h, i, j, k, l, m, f, f1, # Step 2
            n, o, p,                    # Step 3
            q, r, k_prime, neck_point, i_prime  # Step 4 (I' added)
        ]  # 25 points total

        # Scale to SVG units
        scale = 72
        padding_x = 2 * scale
        padding_y = 2 * scale
        front_points_svg = [(x * scale + padding_x, y * scale + padding_y) for x, y in front_points]

        return {
            "front": front_points_svg,
            "piece_style": piece_style
        }

    elif piece_style == "Skirt":

        #Get all Measures
        waist = measurements.get("Waist")
        hip = measurements.get("Hip")
        skirt_lenght = measurements.get("Skirt Length")
        skirt_degree = measurements.get("Skirt Degree")

        raio = waist/2*3.1415
        

    # --- Scale to SVG Units ---
    scale = 72
    padding_x = 8 * scale
    padding_y = 2 * scale
    front_points_svg = [(x * scale + padding_x, y * scale + padding_y) for x, y in front_points]
    back_points_svg = [(x * scale + padding_x + 1200, y * scale + padding_y) for x, y in back_points]

    return {
        "front": front_points_svg,
        "back": back_points_svg
    }