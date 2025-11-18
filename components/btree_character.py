"""
B-tree Index character component - organic, tree-like, amber gradient character.

Represents the B-tree Index algorithm with patient, wise, organic visual style.
"""

from manim import *
import numpy as np
from components.colors import BTREE_AMBER_START, BTREE_AMBER_END


class BTreeCharacter(VGroup):
    """
    Organic, tree-like, amber gradient character representing B-tree Index.

    Characteristics:
    - Smooth, organic curves
    - Warm amber/gold gradient
    - Fluid, graceful movements
    - Patient, wise personality
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Root/trunk
        self.trunk = Rectangle(
            width=0.3,
            height=1.2,
            fill_color=BTREE_AMBER_END,
            fill_opacity=0.8,
            stroke_width=0
        ).set_sheen_direction(UP)

        # Branches (2 levels) - 3 nodes
        self.branches = VGroup()

        for i in range(3):
            branch = Circle(
                radius=0.3,
                fill_color=BTREE_AMBER_START,
                fill_opacity=0.6,
                stroke_color=BTREE_AMBER_END,
                stroke_width=2
            ).shift(UP*0.8 + RIGHT*(i-1)*1.2)

            # Connection line from trunk to branch
            line = Line(
                self.trunk.get_top(),
                branch.get_bottom(),
                color=BTREE_AMBER_START,
                stroke_width=2
            )

            self.branches.add(line, branch)

        # Leaves (particle effect)
        self.leaves = VGroup(*[
            Dot(radius=0.05, color=BTREE_AMBER_START)
            .move_to(UP*2 + RIGHT*np.random.uniform(-2, 2))
            for _ in range(15)
        ])

        self.add(self.trunk, self.branches, self.leaves)

    def idle_animation(self):
        """
        Gentle swaying animation for idle state.

        Returns:
            AnimationGroup: The idle swaying animation
        """
        return AnimationGroup(
            *[
                leaf.animate.shift(RIGHT*0.1*np.sin(i))
                for i, leaf in enumerate(self.leaves)
            ],
            rate_func=there_and_back,
            run_time=3
        )

    def grow_from_seed(self, seed_position):
        """
        Organic growth animation from a seed.

        Args:
            seed_position: Starting position for the seed

        Returns:
            Succession: Sequence of growth animations
        """
        seed = Dot(
            point=seed_position,
            radius=0.1,
            color=BTREE_AMBER_START
        )

        return Succession(
            FadeIn(seed, scale=0.5),
            FadeOut(seed),
            GrowFromCenter(self.trunk),
            LaggedStart(*[
                GrowFromPoint(branch, self.trunk.get_top())
                for branch in self.branches
            ], lag_ratio=0.2),
            LaggedStart(*[
                FadeIn(leaf, scale=0.5)
                for leaf in self.leaves
            ], lag_ratio=0.05)
        )

    def traverse_path(self, path_lines):
        """
        Animate traversing a path through the tree.

        Args:
            path_lines: List of Line objects representing the path

        Returns:
            AnimationGroup: Path traversal animation
        """
        return LaggedStart(*[
            line.animate.set_stroke(color="#50C878", width=8, opacity=0.6)
            for line in path_lines
        ], lag_ratio=0.3)

    def celebrate(self):
        """
        Respectful nod celebration animation.

        Returns:
            Animation: Slight rotation nod
        """
        return self.animate.rotate(PI/12).set_rate_func(there_and_back)

    def range_sweep(self, start_pos, end_pos):
        """
        Elegant sweeping animation for range queries.

        Args:
            start_pos: Starting position
            end_pos: Ending position

        Returns:
            Animation: Smooth sweep animation
        """
        return self.animate.move_to(end_pos).set_rate_func(smooth)
