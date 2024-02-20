__author__ = "Antoine Richard"
__copyright__ = (
    "Copyright 2023, Space Robotics Lab, SnT, University of Luxembourg, SpaceR"
)
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Antoine Richard"
__email__ = "antoine.richard@uni.lu"
__status__ = "development"

from typing import List, Tuple, Union, Dict
import omni.kit.actions.core
import numpy as np
import omni
import carb
import cv2
import os

from omni.isaac.core.utils.stage import add_reference_to_stage

from pxr import UsdGeom, UsdLux, Gf, Usd

from src.environments.lunaryard import LunaryardController
from src.configurations.procedural_terrain_confs import TerrainManagerConf
from src.terrain_management.terrain_manager import TerrainManager
from src.configurations.environments import LunaryardConf
from src.configurations.rendering_confs import FlaresConf
from src.environments.rock_manager import RockManager
from WorldBuilders.pxr_utils import setDefaultOps
from assets import get_assets_path

class LunaryardDeformableController(LunaryardController):
    def __init__(
        self,
        lunaryard_settings: LunaryardConf = None,
        rocks_settings: Dict = None,
        flares_settings: FlaresConf = None,
        terrain_manager: TerrainManagerConf = None,
        **kwargs
    ) -> None:
        """
        Initializes the lab controller. This class is used to control the lab interactive elements.
        Including:
            - Sun position, intensity, radius, color.
            - Terrains randomization or using premade DEMs.
            - Rocks random placements.

        Args:
            lunaryard_settings (LunaryardConf): The settings of the lab.
            rocks_settings (Dict): The settings of the rocks.
            flares_settings (FlaresConf): The settings of the flares.
            terrain_manager (TerrainManagerConf): The settings of the terrain manager.
            **kwargs: Arbitrary keyword arguments."""
    
        super().__init__(lunaryard_settings, rocks_settings, flares_settings, terrain_manager, **kwargs)
    
    def deformTerrain(self, world_poses, contact_forces) -> None:
        self.T.deformTerrain(body_transforms=world_poses, contact_forces=contact_forces)
        self.loadDEM()
        self.RM.updateImageData(self.dem, self.mask)