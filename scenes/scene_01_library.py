"""
Scene 1A: Library Scale (0:15-0:30) - "The Scale Problem"

Vast library reveal → Camera flies through → Focus on one shelf →
Book opens → Clock ticking → TIMEOUT alert

This scene establishes the scale problem that necessitates indexing.
"""

from manim import *
import numpy as np
from components.colors import *
from components.library_shelf import LibraryShelf


class LibraryScaleScene(Scene):
    """
    The library scale problem scene.

    Timeline:
    - 0:15-0:22: Infinite library zoom with parallax
    - 0:22-0:27: Focus on single book with data
    - 0:27-0:30: Clock ticking and timeout alert
    """

    def construct(self):
        # Set background
        self.camera.background_color = BACKGROUND

        # ==========================================
        # STEP 1: Infinite Library Zoom (0:15-0:22)
        # ==========================================

        # Create multiple layers of shelves for parallax depth effect
        # Far layer - smallest, most opacity, moves fastest
        shelves_far = VGroup(*[
            LibraryShelf().scale(0.3).move_to(UP*y + RIGHT*x*0.5)
            for y in range(-10, 10, 2)
            for x in range(-5, 5)
        ]).set_opacity(0.3)

        # Mid layer - medium size, medium opacity
        shelves_mid = VGroup(*[
            LibraryShelf().scale(0.6).move_to(UP*y*0.7 + RIGHT*x*0.3)
            for y in range(-6, 6, 2)
            for x in range(-3, 3)
        ]).set_opacity(0.6)

        # Near layer - full size, full opacity
        shelves_near = VGroup(*[
            LibraryShelf().move_to(UP*y*0.5)
            for y in range(-3, 3, 2)
        ])

        self.add(shelves_far, shelves_mid, shelves_near)

        # High-speed fly-through with parallax effect
        # Different layers move at different speeds to create depth
        self.play(
            shelves_far.animate.shift(DOWN*15).set_opacity(0),
            shelves_mid.animate.shift(DOWN*10).set_opacity(0),
            shelves_near.animate.shift(DOWN*5),
            self.camera.frame.animate.scale(0.5),
            run_time=3,
            rate_func=rush_from
        )

        # ==========================================
        # STEP 2: Focus on Single Book + Data (0:22-0:27)
        # ==========================================

        # Slow down and focus on one shelf
        target_shelf = LibraryShelf().move_to(ORIGIN)

        self.play(
            FadeOut(shelves_near),
            FadeIn(target_shelf),
            run_time=0.5
        )

        # Zoom into one specific book (middle book)
        target_book = target_shelf.books[5]

        self.play(
            self.camera.frame.animate.move_to(target_book.get_center()).scale(0.2),
            run_time=1.5,
            rate_func=smooth
        )

        # Book opens to reveal data
        book_open = Rectangle(
            width=2,
            height=1.5,
            fill_color=ACCENT_WHITE,
            fill_opacity=0.9
        ).move_to(target_book.get_center())

        data_text = Text(
            "user_id: 7239482\nname: Sarah Chen\nemail: s.chen@...",
            font="JetBrains Mono",
            font_size=16,
            color=BLACK
        ).move_to(book_open.get_center())

        self.play(
            Transform(target_book, book_open),
            FadeIn(data_text),
            run_time=0.8
        )

        # ==========================================
        # STEP 3: Clock + Timeout Alert (0:27-0:30)
        # ==========================================

        # Clock appears in upper right
        clock = VGroup(
            Circle(radius=0.5, color=WHITE, stroke_width=2),
            Line(ORIGIN, UP*0.3, color=WHITE, stroke_width=2),     # Hour hand
            Line(ORIGIN, RIGHT*0.4, color=DANGER_RED, stroke_width=2)  # Minute hand
        ).to_edge(UR)

        self.play(FadeIn(clock), run_time=0.3)

        # Clock ticks faster and faster (building anxiety)
        for _ in range(5):
            self.play(
                Rotate(clock[2], PI/6, about_point=clock.get_center()),
                run_time=0.1
            )

        # TIMEOUT alert flashes
        alert = Text(
            "QUERY TIMEOUT",
            color=DANGER_RED,
            font_size=48,
            weight=BOLD
        ).to_edge(UP)

        self.play(
            Flash(alert, color=DANGER_RED, flash_radius=1),
            Write(alert),
            run_time=0.8
        )

        # Statistical text overlays emphasize the scale problem
        stats = VGroup(
            Text("2.3 billion records", font_size=24),
            Text("Linear search: 47 minutes", font_size=24),
            Text("Unacceptable.", font_size=28, color=DANGER_RED, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT)

        self.play(
            LaggedStart(*[
                FadeIn(stat, shift=RIGHT*0.3)
                for stat in stats
            ], lag_ratio=0.3),
            run_time=2
        )

        self.wait(1)


# ==========================================
# VALIDATION CHECKLIST
# ==========================================
# Before proceeding to next scene, verify:
# [ ] Scene renders without errors: manim -ql scenes/scene_01_library.py LibraryScaleScene
# [ ] Parallax effect creates sense of depth
# [ ] High-speed fly-through feels fast but controlled
# [ ] Book focus is smooth and readable
# [ ] Clock ticking builds urgency
# [ ] Timeout alert is dramatic
# [ ] Total timing is ~15 seconds
#
# STOP - Test this scene completely before moving forward
# ==========================================
