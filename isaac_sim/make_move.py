from isaacsim.examples.interactive.base_sample import BaseSample
from isaacsim.core.utils.nucleus import get_assets_root_path
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.robot.wheeled_robots.controllers.differential_controller import DifferentialController
from isaacsim.robot.wheeled_robots.robots import WheeledRobot
import carb
import numpy as np


class RobotMovement(BaseSample):
    def __init__(self) -> None:
        super().__init__()
        self._controller = DifferentialController(name="simple_control", wheel_radius=0.0675, wheel_base=0.233)
        self._step_count = 0
        return

    def setup_scene(self):
        world = self.get_world()
        
        # 获取资源根路径
        assets_root_path = get_assets_root_path()
        if assets_root_path is None:
            carb.log_error("Could not find Isaac Sim assets folder")
            
        # 添加自定义场景
        my_scene_asset_path = "path/to/your/scene.usd"  # 替换为您的场景文件路径
        world.scene.add(
            usd_path=my_scene_asset_path,
            prim_path="/World/MyScene"
        )
            
        # 添加自定义机器人
        my_robot = world.scene.add(
            WheeledRobot(
                prim_path="/World/MyRobot",
                name="my_robot",
                wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],  # 修改为您机器人实际的轮子关节名称
                create_robot=True,
                usd_path="path/to/your/robot.usd",  # 替换为实际路径
                position=np.array([0, 0.0, 2.0]),  # 根据需要调整初始位置
            )
        )
        return

    async def setup_post_load(self):
        self._world = self.get_world()
        self._robot = self._world.scene.get_object("my_robot")
        self._world.add_physics_callback("robot_actions", callback_fn=self.send_robot_actions)
        return

    def send_robot_actions(self, step_size):
        if self._step_count >= 0 and self._step_count < 1000:
            # 使用与hello_world.py相同的控制逻辑
            self._robot.apply_wheel_actions(self._controller.forward(command=[0.05, 0]))
            print(self._robot.get_linear_velocity())
        self._step_count += 1
        return

    async def setup_pre_reset(self):
        self._step_count = 0
        return

    async def setup_post_reset(self):
        self._controller.reset()
        return

    def world_cleanup(self):
        return
