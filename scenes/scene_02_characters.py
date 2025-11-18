"""
Scene 1B: Character Introductions (0:30-0:45)

Split screen → Hash materializes (left, geometric, cyan) →
B-tree grows (right, organic, amber) → 360° rotation

This scene introduces our two "characters" with distinct personalities.
"""

from manim import *
import numpy as np
from components.colors import *
from components.hash_character import HashCharacter
from components.btree_character import BTreeCharacter


class CharacterIntroScene(Scene):
    """
    Introduce Hash and B-tree as characters with personality.

    Timeline:
    - 0:30-0:32: Split screen setup
    - 0:32-0:37: Hash emergence (left) with pixelation
    - 0:37-0:42: B-tree growth (right) from seed
    - 0:42-0:45: Hero shot with 360° rotation
    """

    def construct(self):
        # Set background
        self.camera.background_color = BACKGROUND

        # ==========================================
        # STEP 1: Split Screen Setup
        # ==========================================

        # Create vertical divider down the middle
        divider = Line(
            UP*4, DOWN*4,
            color=ACCENT_WHITE,
            stroke_width=2
        ).set_opacity(0.3)

        # Add glow effect to divider (makes it more dramatic)
        divider_glow = divider.copy().set_stroke(
            color=ACCENT_PURPLE,
            width=8,
            opacity=0.2
        )

        self.play(
            Create(divider),
            FadeIn(divider_glow),
            run_time=1
        )

        # ==========================================
        # STEP 2: Hash Character Emergence (Left Side)
        # ==========================================

        # Hash emerges from digital pixels
        hash_char = HashCharacter().shift(LEFT*3)

        # Pixelation effect - scattered pixels coalesce
        pixels = VGroup(*[
            Square(side_length=0.1, fill_color=HASH_CYAN, fill_opacity=0.8)
            .move_to(hash_char.get_center() + np.array([
                np.random.uniform(-2, 2),
                np.random.uniform(-2, 2),
                0
            ]))
            for _ in range(100)
        ])

        # Pixels appear
        self.play(
            LaggedStart(*[
                FadeIn(pixel, scale=0.5) for pixel in pixels
            ], lag_ratio=0.01),
            run_time=1
        )

        # Pixels coalesce into Hash character
        self.play(
            FadeOut(pixels),
            FadeIn(hash_char, scale=0.8),
            run_time=1.2
        )

        # Label and specs appear (HUD-style)
        hash_label = Text(
            "HASH INDEX",
            font="Monospace",  # Fallback for Monument Extended
            font_size=28,
            color=HASH_CYAN,
            weight=BOLD
        ).next_to(hash_char, DOWN, buff=0.5)

        hash_specs = VGroup(
            Text("O(1) lookup", font_size=16, color=WHITE),
            Text("Bucket-based", font_size=16, color=WHITE),
            Text("Equality only", font_size=16, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        hash_specs.next_to(hash_label, DOWN, buff=0.3)

        self.play(
            Write(hash_label),
            FadeIn(hash_specs, shift=UP*0.2, lag_ratio=0.2),
            run_time=1.5
        )

        # ==========================================
        # STEP 3: B-tree Character Growth (Right Side)
        # ==========================================

        # B-tree grows organically from seed
        btree_char = BTreeCharacter().shift(RIGHT*3)

        # Start with a seed
        seed = Dot(
            point=btree_char.get_center() + DOWN*2,
            radius=0.1,
            color=BTREE_AMBER_START
        )

        self.play(FadeIn(seed, scale=0.5), run_time=0.5)

        # Growth animation - organic and natural
        self.play(
            FadeOut(seed),
            GrowFromCenter(btree_char.trunk),
            run_time=1.2,
            rate_func=rush_from
        )

        # Branches grow from trunk
        self.play(
            LaggedStart(*[
                GrowFromPoint(branch, btree_char.trunk.get_top())
                for branch in btree_char.branches
            ], lag_ratio=0.2),
            run_time=1.5
        )

        # Leaves appear like particles
        self.play(
            LaggedStart(*[
                FadeIn(leaf, scale=0.5) for leaf in btree_char.leaves
            ], lag_ratio=0.05),
            run_time=1
        )

        # Label and specs (elegant serif style)
        btree_label = Text(
            "B-TREE INDEX",
            font="Serif",  # Fallback for Cormorant Garamond
            font_size=28,
            color=BTREE_AMBER_START
        ).next_to(btree_char, DOWN, buff=0.5)

        btree_specs = VGroup(
            Text("O(log n) lookup", font_size=16, color=WHITE),
            Text("Sorted structure", font_size=16, color=WHITE),
            Text("Range queries", font_size=16, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        btree_specs.next_to(btree_label, DOWN, buff=0.3)

        self.play(
            Write(btree_label),
            FadeIn(btree_specs, shift=UP*0.2, lag_ratio=0.2),
            run_time=1.5
        )

        # ==========================================
        # STEP 4: Hero Shot - 360° Rotation
        # ==========================================

        # Remove labels for cleaner hero shot
        self.play(
            FadeOut(hash_label, hash_specs, btree_label, btree_specs),
            run_time=0.5
        )

        # Dramatic 360° rotation of both characters
        self.play(
            Rotate(hash_char, PI*2, about_point=hash_char.get_center()),
            Rotate(btree_char, PI*2, about_point=btree_char.get_center()),
            run_time=3,
            rate_func=smooth
        )

        # Add breathing/idle animations
        self.play(
            hash_char.idle_animation(),
            btree_char.idle_animation()
        )

        self.wait(1)


# ==========================================
# VALIDATION CHECKLIST
# ==========================================
# Before proceeding to next scene, verify:
# [ ] Scene renders without errors: manim -ql scenes/scene_02_characters.py CharacterIntroScene
# [ ] Both characters have distinct visual personalities
# [ ] Hash feels aggressive/digital, B-tree feels organic/patient
# [ ] Split screen composition is balanced
# [ ] Pixelation vs growth animations are effective
# [ ] 360° rotation is smooth and dramatic
# [ ] Total timing is ~15 seconds
# [ ] Characters are recognizable and memorable
#
# STOP - Do not proceed until both characters work perfectly
# ==========================================
