"""
Scene 3: Challenge 1 - "The Single Target" (0:45-1:05)

Mission briefing → Hash teleports instantly → B-tree traverses path →
Hash wins speed comparison

This is the first challenge and establishes Hash's strength in exact lookups.
"""

from manim import *
import numpy as np
from components.colors import *
from components.hash_character import HashCharacter
from components.btree_character import BTreeCharacter


class Challenge1Scene(Scene):
    """
    Challenge 1: Single exact lookup - Hash Index wins.

    Timeline:
    - 0:45-0:47: Mission briefing setup
    - 0:47-0:52: Hash approach (teleport)
    - 0:52-0:57: B-tree approach (tree traversal)
    - 0:57-1:05: Side-by-side comparison
    """

    def construct(self):
        # Set background
        self.camera.background_color = BACKGROUND

        # ==========================================
        # STEP 1: Mission Briefing Setup
        # ==========================================

        # Characters at starting positions
        hash_char = HashCharacter().shift(LEFT*4 + DOWN*1)
        btree_char = BTreeCharacter().shift(LEFT*4 + DOWN*1.2)

        self.play(
            FadeIn(hash_char, shift=RIGHT),
            FadeIn(btree_char, shift=RIGHT),
            run_time=0.8
        )

        # Mission briefing (HUD style, like a video game mission)
        mission_title = Text(
            "MISSION: Find user_id = 42",
            font="Monospace",
            font_size=32,
            color=ACCENT_WHITE,
            weight=BOLD
        ).to_edge(UP)

        mission_bg = Rectangle(
            width=mission_title.width + 1,
            height=mission_title.height + 0.5,
            fill_color=BLACK,
            fill_opacity=0.7,
            stroke_color=SUCCESS_GREEN,
            stroke_width=2
        ).move_to(mission_title.get_center())

        self.play(
            FadeIn(mission_bg),
            Write(mission_title),
            Flash(mission_title, color=SUCCESS_GREEN),
            run_time=1.2
        )

        # Target book appears in distance (the goal)
        target_book = Rectangle(
            width=0.5,
            height=0.8,
            fill_color=GOLD,
            fill_opacity=0.9,
            stroke_color=ACCENT_WHITE,
            stroke_width=2
        ).shift(RIGHT*5 + UP*1)

        # Glow around target to make it stand out
        target_glow = target_book.copy().scale(1.3).set_stroke(
            color=GOLD,
            width=10,
            opacity=0.3
        )

        self.play(
            FadeIn(target_book, scale=1.2),
            FadeIn(target_glow),
            run_time=0.8
        )

        # Countdown timer (builds tension)
        countdown = VGroup(*[
            Text(str(i), font_size=72, color=ACCENT_WHITE, weight=BOLD)
            for i in [3, 2, 1]
        ])

        for num in countdown:
            self.play(FadeIn(num, scale=2), run_time=0.3)
            self.play(FadeOut(num, scale=0.5), run_time=0.3)

        go_text = Text("GO!", font_size=96, color=SUCCESS_GREEN, weight=BOLD)
        self.play(
            Flash(go_text, color=SUCCESS_GREEN, flash_radius=2),
            FadeIn(go_text, scale=2),
            run_time=0.3
        )
        self.play(FadeOut(go_text), run_time=0.2)

        # ==========================================
        # STEP 2: Hash Function Visualization + Teleport
        # ==========================================

        # Query enters Hash
        query = Text("id = 42", font_size=24, color=ACCENT_WHITE)
        query.next_to(hash_char, LEFT)

        self.play(
            FadeIn(query),
            query.animate.move_to(hash_char.get_center()),
            run_time=0.5
        )

        # HASH FUNCTION VISUALIZATION - Kaleidoscope effect
        kaleidoscope = VGroup(*[
            RegularPolygon(n=6, radius=0.5)
            .rotate(PI*i/6)
            .set_fill(HASH_CYAN, opacity=0.3)
            .set_stroke(HASH_CYAN, width=2)
            for i in range(6)
        ]).move_to(hash_char.get_center())

        self.play(
            FadeOut(query),
            FadeIn(kaleidoscope),
            Rotate(kaleidoscope, PI*4, run_time=1),
            kaleidoscope.animate.scale(2).set_opacity(0)
        )

        # Output: Bucket coordinate
        bucket_label = Text(
            "BUCKET[7]",
            font_size=28,
            color=HASH_CYAN,
            weight=BOLD
        ).move_to(hash_char.get_center() + UP*1)

        self.play(Write(bucket_label), run_time=0.3)

        # TELEPORT EFFECT - Instant travel
        ghost = hash_char.copy().set_opacity(0.3)

        teleport_flash = Circle(
            radius=2,
            fill_color=HASH_CYAN,
            fill_opacity=0.5,
            stroke_width=0
        ).move_to(hash_char.get_center())

        self.play(
            FadeIn(teleport_flash, scale=0.1),
            FadeOut(teleport_flash, scale=3),
            hash_char.animate.move_to(target_book.get_center() + LEFT*0.5),
            FadeIn(ghost),
            run_time=0.3
        )

        # Ghost fades
        self.play(FadeOut(ghost, bucket_label), run_time=0.5)

        # Hash grabs the book
        self.play(
            target_book.animate.move_to(hash_char.get_center()),
            Flash(target_book, color=HASH_CYAN),
            run_time=0.4
        )

        # Victory pose (showboating)
        self.play(
            hash_char.animate.scale(1.2),
            rate_func=there_and_back,
            run_time=0.6
        )

        # Timer display - incredibly fast
        hash_time = Text(
            "0.003 seconds",
            font_size=32,
            color=SUCCESS_GREEN,
            weight=BOLD
        ).next_to(hash_char, DOWN)

        hash_complexity = Text(
            "O(1)",
            font_size=48,
            color=HASH_CYAN,
            weight=BOLD
        ).next_to(hash_time, DOWN)

        self.play(
            FadeIn(hash_time),
            FadeIn(hash_complexity, scale=1.5),
            run_time=1
        )

        # ==========================================
        # STEP 3: B-tree Path Traversal
        # ==========================================

        # Reset scene for B-tree attempt
        self.play(
            *[FadeOut(mob) for mob in [hash_char, target_book, hash_time, hash_complexity]],
            run_time=0.5
        )

        # B-tree back at start
        btree_char = BTreeCharacter().shift(LEFT*4 + DOWN*1)
        target_book = Rectangle(
            width=0.5,
            height=0.8,
            fill_color=GOLD,
            fill_opacity=0.9
        ).shift(RIGHT*5 + UP*1)

        self.play(FadeIn(btree_char), FadeIn(target_book))

        # Build tree structure for visualization
        tree = VGroup()

        # Root node
        root = Circle(radius=0.4, fill_color=BTREE_AMBER_START, fill_opacity=0.6)
        root.move_to(ORIGIN)
        root_text = Text("50", font_size=20, color=BLACK).move_to(root.get_center())
        tree.add(VGroup(root, root_text))

        # Level 2 nodes
        left_node = Circle(radius=0.4, fill_color=BTREE_AMBER_START, fill_opacity=0.6)
        left_node.move_to(LEFT*2 + DOWN*1.5)
        left_text = Text("25", font_size=20, color=BLACK).move_to(left_node.get_center())

        right_node = Circle(radius=0.4, fill_color=BTREE_AMBER_START, fill_opacity=0.6)
        right_node.move_to(RIGHT*2 + DOWN*1.5)
        right_text = Text("75", font_size=20, color=BLACK).move_to(right_node.get_center())

        # Connections
        conn1 = Line(root.get_bottom(), left_node.get_top(), color=BTREE_AMBER_END, stroke_width=2)
        conn2 = Line(root.get_bottom(), right_node.get_top(), color=BTREE_AMBER_END, stroke_width=2)

        tree.add(conn1, conn2)
        tree.add(VGroup(left_node, left_text), VGroup(right_node, right_text))

        # Leaf level
        leaf = Rectangle(
            width=1.5,
            height=0.4,
            fill_color=BTREE_AMBER_START,
            fill_opacity=0.6
        ).next_to(left_node, DOWN, buff=1)
        leaf_text = Text("38, 39, 42, 45", font_size=16, color=BLACK).move_to(leaf.get_center())

        conn3 = Line(left_node.get_bottom(), leaf.get_top(), color=BTREE_AMBER_END, stroke_width=2)
        tree.add(conn3, VGroup(leaf, leaf_text))

        self.play(FadeIn(tree), run_time=0.8)

        # Traversal animation - showing decision process
        # Step 1: Root decision
        decision_1 = Text("42 < 50 ?", font_size=20, color=ACCENT_WHITE).next_to(root, UP)
        self.play(
            Write(decision_1),
            root.animate.set_stroke(color=SUCCESS_GREEN, width=4),
            run_time=0.8
        )

        # Path glows
        path_glow_1 = conn1.copy().set_stroke(color=SUCCESS_GREEN, width=8, opacity=0.6)
        self.play(
            FadeIn(path_glow_1),
            btree_char.animate.move_to(left_node.get_center()),
            run_time=1
        )

        self.play(FadeOut(decision_1))

        # Step 2: Left node decision
        decision_2 = Text("42 > 25 ?", font_size=20, color=ACCENT_WHITE).next_to(left_node, UP)
        self.play(
            Write(decision_2),
            left_node.animate.set_stroke(color=SUCCESS_GREEN, width=4),
            run_time=0.8
        )

        path_glow_2 = conn3.copy().set_stroke(color=SUCCESS_GREEN, width=8, opacity=0.6)
        self.play(
            FadeIn(path_glow_2),
            btree_char.animate.move_to(leaf.get_center()),
            run_time=1
        )

        self.play(FadeOut(decision_2))

        # Step 3: Find in leaf
        target_highlight = Circle(radius=0.15, color=GOLD, stroke_width=3)
        target_highlight.move_to(leaf.get_center() + LEFT*0.2)  # Around "42"

        self.play(
            Create(target_highlight),
            Flash(target_highlight, color=GOLD),
            run_time=0.8
        )

        # Book slides out gracefully
        self.play(
            target_book.animate.move_to(btree_char.get_center()),
            run_time=1
        )

        # Respectful nod (showing B-tree's thoughtful nature)
        self.play(
            btree_char.animate.rotate(PI/12),
            rate_func=there_and_back,
            run_time=0.8
        )

        # Timer - slightly slower but still fast
        btree_time = Text(
            "0.012 seconds",
            font_size=32,
            color=SUCCESS_GREEN,
            weight=BOLD
        ).to_edge(DOWN)

        btree_complexity = Text(
            "O(log n)",
            font_size=48,
            color=BTREE_AMBER_START,
            weight=BOLD
        ).next_to(btree_time, DOWN)

        self.play(
            FadeIn(btree_time),
            FadeIn(btree_complexity, scale=1.5),
            run_time=1
        )

        # ==========================================
        # STEP 4: Side-by-Side Comparison
        # ==========================================

        # Clear scene
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)

        # Split screen comparison
        hash_result = VGroup(
            HashCharacter(),
            Rectangle(width=0.5, height=0.8, fill_color=GOLD, fill_opacity=0.9),
            Text("0.003s", font_size=24, color=SUCCESS_GREEN),
            Text("O(1)", font_size=32, color=HASH_CYAN)
        ).arrange(DOWN, buff=0.3).shift(LEFT*3)

        btree_result = VGroup(
            BTreeCharacter(),
            Rectangle(width=0.5, height=0.8, fill_color=GOLD, fill_opacity=0.9),
            Text("0.012s", font_size=24, color=SUCCESS_GREEN),
            Text("O(log n)", font_size=32, color=BTREE_AMBER_START)
        ).arrange(DOWN, buff=0.3).shift(RIGHT*3)

        self.play(
            FadeIn(hash_result),
            FadeIn(btree_result),
            run_time=1
        )

        # Crown appears above Hash (winner!)
        crown = Text("👑", font_size=48).next_to(hash_result, UP)

        self.play(
            FadeIn(crown, shift=DOWN*0.3),
            hash_result.animate.scale(1.1),
            run_time=0.8
        )

        # Winner text
        winner = Text(
            "Speed: Hash wins",
            font_size=36,
            color=HASH_CYAN,
            weight=BOLD
        ).to_edge(UP)

        self.play(Write(winner), run_time=1)

        # Subtle foreshadowing (sets up future challenges)
        hint = Text(
            "But notice...",
            font_size=20,
            color=ACCENT_WHITE,
            slant=ITALIC,
            opacity=0.6
        ).to_edge(DOWN)

        self.play(FadeIn(hint), run_time=1)
        self.wait(2)


# ==========================================
# VALIDATION CHECKLIST
# ==========================================
# Before proceeding to next scene, verify:
# [ ] Scene renders without errors: manim -ql scenes/scene_03_challenge_1.py Challenge1Scene
# [ ] Mission briefing builds excitement
# [ ] Hash teleport feels FAST and dramatic
# [ ] B-tree traversal is educational and clear
# [ ] Path lighting shows decision-making process
# [ ] Side-by-side comparison is fair
# [ ] Hash victory is obvious
# [ ] Foreshadowing is subtle but present
# [ ] Total timing is ~20 seconds
#
# STOP - Do not proceed until Challenge 1 works perfectly
# ==========================================
