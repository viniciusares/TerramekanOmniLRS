# TerramekanOmniLRS version=unversioned
## a fork from jnskkmhr/OmniLRS (which itself is a fork from AntoineRichard/OmniLRS)

This fork contains work from SpaceR, SRL and UNICAMP FEEC AdRobLab. For details refer to the “upstream” repositories.
> Should you run into any bug, or would like to have a new feature, feel free to open an issue.

This initial include the environments:
 - The lunalab 
 - The lunaryard (3 versions 20m, 40m, 80m)
 - The deformable lunalab
 - The deformable lunaryard

As we are in the development phase, only one operation mode is being focused:
 - ROS1: allows to run ROS1 enabled EX1 rover with terrain deformation enabled and joystick teleoperation.

This fork is only focusing in renderer=ray_tracing and not path_tracing.

## Getting started:

<details><summary><b>Requirements</b></summary>

Software:
 - Ubuntu 20.04 or 22.04 (in case you don't have ubuntu installed and is trying to set up dual boot, first read about how Secure Boot relates to UEFI/BIOSlegacy, if you don't invest time in this, be prepared for pain, tears and nightmares :)   )
 - ROS1 installed.
 - IsaacSim version 2022.2.1 or 2023.1.1

Hardware:
 - Workstation with a dedicated Nvidia graphics card of the type/series RTX.
 - Nvidia/Ubuntu graphics card driver compatible with Nvidia IsaacSim.

Installation:
```bash
git clone https://github.com/viniciusares/TerramekanOmniLRS.git
cd TerramekanOmniLRS
git submodule init
git submodule update
~/.local/share/ov/pkg/isaac_sim-2023.1.1/python.sh -m pip install opencv-python omegaconf hydra-core
```

Assets and WorldBuilders:
 - Download the assets from: https://drive.google.com/file/d/1NpgMdD__DaU_mogeA7D-GqObMkGJ5-fN/view?usp=sharing
 - Unzip the assets inside the git repository. (The directory should be as shown in [Directory Structure](#directory-structure)
 - Download ZIP WorldBuilders from: https://github.com/AntoineRichard/WorldBuilders
 - Unzip the WorldBuilders as shown in the folder structure: (The directory should be as shown in [Directory Structure](#directory-structure)

</details>

<details><summary><b>Running the sim</b></summary>
 
To run the simulation we use a configuration manager called Hydra.
Inside the `cfg` folder, you will find three folders:
 - `mode`
 - `environment`
 - `rendering`

To run the lunaryard deformable environment you can use the following command:
```bash
~/.local/share/ov/pkg/isaac_sim-2023.1.1/python.sh run.py environment=lunaryard_deformable_10m mode=ROS1 rendering=ray_tracing
```
Similarly, to run the lunalab deformable environment, use the following command:
```bash
~/.local/share/ov/pkg/isaac_sim-2023.1.1/python.sh run.py environment=lunalab_deformable mode=ROS1 rendering=ray_tracing
```

The rendering mode can be changed by using `rendering=path_tracing` instead of `rendering=ray_tracing` but that is not being maintained for this fork.
Changing form `ray_tracing` to path `path_tracing` tells Hydra to use `cfg/rendering/path_tracing.yaml` instead of `cfg/rendering/ray_tracing.yaml`.
Hence, if you wanted to change some of these parameters, you could create your own yaml file inside `cfg/rendering`
and let Hydra fetch it.

If you just want to modify a parameter for a given run, say disabling the lens-flare effects, then you can also edit parameters directly from the command line:
For instance:
```bash
~/.local/share/ov/pkg/isaac_sim-2023.1.1/python.sh run.py environment=lunaryard_deformable_10m mode=ROS1 rendering=ray_tracing rendering.lens_flares.enable=False
```

We provide bellow a couple premade command line that can be useful, the full description of the configuration files is given here:
Lunaryard, ROS1
```bash
~/.local/share/ov/pkg/isaac_sim-2023.1.1/python.sh run.py environment=lunaryard_deformable_10m mode=ROS1 rendering=ray_tracing
```
Lunalab, ROS1
```bash
~/.local/share/ov/pkg/isaac_sim-2023.1.1/python.sh run.py environment=lunalab_deformable mode=ROS1 rendering=ray_tracing
```
SDG (sythetic data generation)
Please, try on the upstream repositories

</details>

<details><summary><b>Simulation Interaction</b></summary>
Since we do not have custom topics, we had to use the base ROS topics for everything.
 Most of the simulation interactions are Not fairly straightforward, but we can't provide details on how to make custom fancy runs, for that case refer to OpenAI chatGPT or your favorite chatbot.  

- Interacting with the robots: refer to upstream repos
- Radomizing terrain or rocks: refer to upstrem repos
- Hiding the rocks: in IsaacSim, the right-most menu has a tree structure showing the current items of the sim, find the "rocks item", then one of the columns has an eye-logo button. Use this button to hide/unhide the rocks.
- Changing the render mode: path_tracing / ray_tracing (try at your own risk of refer to upstream repos and try at your own risk)
 
</details>

## Citation
Please use the following citation if you use `OmniLRS` in your work. (This is actually important, avoid being sued ;-) )
```bibtex
@article{richard2023omnilrs,
  title={OmniLRS: A Photorealistic Simulator for Lunar Robotics},
  author={Richard, Antoine and Kamohara, Junnosuke and Uno, Kentaro and Santra, Shreya and van der Meer, Dave and Olivares-Mendez, Miguel and Yoshida, Kazuya},
  journal={arXiv preprint arXiv:2309.08997},
  year={2023}
}
```

## File Structure
```bash
/
├── Home
    ├── student_folder
    │   └── project_folder
    │       ├── catkin_ws
    │       └── TerramekanOmniLRS
    │           ├── assets
    │           │   ├── Terrains
    │           │   ├── Textures
    │           │   ├── USD_Assets
    │           │   └── __init__.py
    │           ├── cfg
    │           │   ├── environment
    │           │   ├── mode
    │           │   ├── rendering
    │           │   └── config.yaml
    │           ├── src
    │           │   ├── configurations
    │           │   ├── environments
    │           │   ├── environments_wrappers
    │           │   ├── labeling
    │           │   ├── robots
    │           │   ├── ros
    │           │   └── terrain_management
    │           │       ├── terrain_generation.py
    │           │       └── terrain_manager.py
    │           ├── WorldBuilders
    │           │   ├── WorldBuilders-main
    │           │   ├── Clippers.py
    │           │   ├── ...
    │           │   └── WorldBuilder.py
    │           ├── __init__.py
    │           ├── README.md
    │           └── run.py
    ├── .local
    │   └── share
    │       └── ov
    │           └── pkg
    │               └── isaac_sim-202x.x.1
    │                   └── kit
    │                       └── python  
    │                           ├── python
    │                           └── python3
    ├── .ros
    └── .bashrc
```
