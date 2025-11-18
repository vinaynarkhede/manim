"""
Hash Index character component - geometric, crystalline, electric blue character.

Represents the Hash Index algorithm with aggressive, sharp, digital visual style.
"""

from manim import *
import numpy as np
from components.colors import HASH_CYAN


class HashCharacter(VGroup):
    """
    Geometric, crystalline, electric blue character representing Hash Index.

    Characteristics:
    - Sharp, angular geometric shapes
    - Electric blue/cyan color
    - Quick, precise movements
    - Aggressive personality
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Core geometric shape - angular hexagon
        self.hexagon = RegularPolygon(
            n=6,
            radius=1.5,
            fill_color=HASH_CYAN,
            fill_opacity=0.3,
            stroke_color=HASH_CYAN,
            stroke_width=3
        )

        # Inner geometric pattern (triangles)
        inner_shapes = VGroup(*[
            RegularPolygon(
                n=3,
                radius=0.3,
                fill_color=HASH_CYAN,
                fill_opacity=0.7
            ).rotate(PI*i/3).shift(UP*0.5*np.cos(i))
            for i in range(6)
        ])

        # Electric particles orbiting
        self.particles = VGroup(*[
            Dot(radius=0.03, color=HASH_CYAN)
            .move_to(self.hexagon.point_from_proportion(i/20))
            for i in range(20)
        ])

        self.add(self.hexagon, inner_shapes, self.particles)

    def idle_animation(self):
        """
        Breathing/pulsing animation for idle state.

        Returns:
            AnimationGroup: The idle breathing animation
        """
        return AnimationGroup(
            self.hexagon.animate.scale(1.05).set_opacity(0.5),
            rate_func=there_and_back,
            run_time=2
        )

    def teleport_to(self, target_position):
        """
        Create teleport effect animation to target position.

        Args:
            target_position: The target position to teleport to

        Returns:
            AnimationGroup: The teleport animation sequence
        """
        # Create ghost trail
        ghost = self.copy().set_opacity(0.3)

        # Flash effect
        flash = Circle(
            radius=2,
            fill_color=HASH_CYAN,
            fill_opacity=0.5,
            stroke_width=0
        ).move_to(self.get_center())

        return AnimationGroup(
            FadeIn(flash, scale=0.1),
            FadeOut(flash, scale=3),
            self.animate.move_to(target_position),
            FadeIn(ghost),
            run_time=0.3
        )

    def celebrate(self):
        """
        Victory celebration animation.

        Returns:
            Animation: Scale up and down for celebration
        """
        return self.animate.scale(1.2).set_rate_func(there_and_back)

    def struggle(self):
        """
        Struggling animation (for range query failure).

        Returns:
            AnimationGroup: Shake and color change animation
        """
        return AnimationGroup(
            self.animate.shift(LEFT*0.1, RIGHT*0.1).set_rate_func(there_and_back),
            self.hexagon.animate.set_stroke(color="#FF0000", width=4),
            run_time=0.5
        )
