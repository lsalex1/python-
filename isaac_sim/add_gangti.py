
from isaacsim.examples.interactive.base_sample import BaseSample
import numpy as np
# 立方体 Python API引用
from isaacsim.core.api.objects import DynamicCuboid

class HelloWorld(BaseSample):
    def __init__(self) -> None:
        super().__init__()
        return

    def setup_scene(self):
        world = self.get_world()
        world.scene.add_default_ground_plane()
        fancy_cube = world.scene.add(
            DynamicCuboid(
                prim_path="/World/random_cube",  # 立方体在 USD 舞台中的 prim 路径
                name="fancy_cube",  # 对象名称
                position=np.array([0, 0, 1.0]),  # 立方体世界坐标位置
                scale=np.array([0.5015, 0.5015, 0.5015]),  # 立方体缩放比例
                color=np.array([0, 0, 1.0]),  # 立方体颜色，使用数组表示RGB值
            ))
        return
    
    async def setup_post_load(self):
        return

    async def setup_pre_reset(self):
        return

    async def setup_post_reset(self):
        return

    def world_cleanup(self):
        return