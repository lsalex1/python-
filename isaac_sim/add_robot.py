from isaacsim.examples.interactive.base_sample import BaseSample
from isaacsim.core.utils.nucleus import get_assets_root_path
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.api.robots import Robot
import carb


class HelloWorld(BaseSample):
    def __init__(self) -> None:
        super().__init__()
        return

    def setup_scene(self):
        # 获取当前世界的实例
        world = self.get_world()
        # 向场景中添加默认的地面平面
        world.scene.add_default_ground_plane()

        # 获取 Nucleus 服务器中 /Isaac 文件夹的路径
        assets_root_path = get_assets_root_path()
        if assets_root_path is None:
            # 使用 carb 记录错误日志（终端显示）
            carb.log_error("未找到包含 /Isaac 文件夹的 Nucleus 服务器")



        # 定义 Jetbot 机器人的 USD 文件路径
        asset_path =  ""   # 替换为实际路径 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!





        # 在 USD 舞台中创建一个新的 XFormPrim，并将其指向 USD 文件作为引用
        # 类似于内存中的指针
        add_reference_to_stage(usd_path=asset_path, prim_path="/World/MyRobot")

        # 将 Jetbot 的 prim 根节点包装到 Robot 类中，并添加到场景中
        # 以便使用高级 API 设置/获取属性，并初始化所需的物理句柄等
        # 注意：此调用不会在舞台窗口中创建 Jetbot，它已经在 add_reference_to_stage 中创建
        jetbot_robot = world.scene.add(Robot(prim_path="/World/Fancy_Robot", name="fancy_robot"))

        # 注意：在调用 reset 之前，无法访问与 Articulation 相关的信息
        # 因为物理句柄尚未初始化。setup_post_load 在第一次 reset 后调用，因此可以在此处操作
        print("第一次 reset 前的自由度数量: " + str(jetbot_robot.num_dof))  # 输出 None
        return

    async def setup_post_load(self):
        return

    async def setup_pre_reset(self):
        return

    async def setup_post_reset(self):
        return

    def world_cleanup(self):
        return