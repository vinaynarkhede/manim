"""
Scene 0: Cold Open (0:00-0:15) - "The Hook"

Complete darkness → Query appears → Explodes into particles → Title card emerges

This scene establishes the visual language and immediately hooks the viewer
with a dramatic particle explosion effect.
"""

from manim import *
import numpy as np
from components.colors import *


class ColdOpenScene(Scene):
    """
    The opening hook scene for The Index Paradox.

    Timeline:
    - 0:00-0:04: Query text appearance with slow dolly
    - 0:04-0:07: Particle explosion
    - 0:07-0:15: Title card reformation and display
    """

    def construct(self):
        # Set background to deep navy
        self.camera.background_color = BACKGROUND

        # ==========================================
        # STEP 1: Query Text Appearance (0:00-0:04)
        # ==========================================

        # Create query text
        query = Text(
            "SELECT * FROM users WHERE id = 42",
            font="JetBrains Mono",
            color=ACCENT_WHITE,
            font_size=36
        )

        # Position in center
        query.move_to(ORIGIN)

        # Fade in from darkness with slow dolly (cinematic zoom)
        self.play(
            FadeIn(query, run_time=2),
            self.camera.frame.animate.scale(0.95),  # Slow zoom in
            rate_func=linear
        )
        self.wait(0.5)

        # ==========================================
        # STEP 2: Particle Explosion (0:04-0:07)
        # ==========================================

        # Create particles starting at query center
        particles = VGroup(*[
            Dot(point=query.get_center(), radius=0.02, color=HASH_CYAN)
            for _ in range(500)
        ])

        # Split particles into two streams (chaotic vs ordered)
        hash_particles = particles[:250]  # Chaotic explosion
        btree_particles = particles[250:]  # Ordered pattern

        # EXPLOSION: Query disappears, particles fly outward
        self.play(
            FadeOut(query, run_time=0.2),
            LaggedStart(*[
                particle.animate.move_to(
                    query.get_center() + np.array([
                        np.random.uniform(-4, 4),
                        np.random.uniform(-3, 3),
                        0
                    ])
                ).set_opacity(0)
                for particle in hash_particles
            ], lag_ratio=0.01, run_time=1.5)
        )

        # ==========================================
        # STEP 3: Title Card Reformation (0:07-0:15)
        # ==========================================

        # Create title text with stroke for dramatic effect
        title = Text(
            "THE INDEX PARADOX",
            font="Monospace",  # Fallback for Monument Extended
            color=ACCENT_WHITE,
            font_size=72,
            weight=BOLD
        ).set_stroke(color=HASH_CYAN, width=2, opacity=0.5)

        subtitle = Text(
            "When faster isn't better",
            font="Sans",  # Fallback for Inter
            color=ACCENT_WHITE,
            font_size=28,
            slant=ITALIC,
            opacity=0.8
        ).next_to(title, DOWN, buff=0.3)

        title_group = VGroup(title, subtitle)

        # Particles reform into title (visual callback to explosion)
        self.play(
            LaggedStart(*[
                particle.animate.move_to(title.get_center()).set_opacity(1)
                for particle in particles[:100]
            ], lag_ratio=0.02),
            FadeIn(title, scale=1.2),
            run_time=2
        )

        # Subtitle fades in smoothly
        self.play(FadeIn(subtitle, shift=UP*0.2), run_time=0.8)
        self.wait(1.5)

        # Fade out title card to transition to next scene
        self.play(FadeOut(title_group), run_time=0.8)


# ==========================================
# VALIDATION CHECKLIST
# ==========================================
# Before proceeding to next scene, verify:
# [ ] Scene renders without errors: manim -ql scenes/scene_00_cold_open.py ColdOpenScene
# [ ] Total timing is ~15 seconds (±1 second acceptable)
# [ ] Query text appears cleanly
# [ ] Particle explosion feels dramatic
# [ ] Title card has visual impact
# [ ] Transition out is smooth
#
# STOP HERE - Do not proceed until this scene works perfectly
# ==========================================
