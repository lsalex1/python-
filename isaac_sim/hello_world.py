from isaacsim import SimulationApp
from isaacsim.core.api import World
from isaacsim.robot.wheeled_robots.controllers.differential_controller import DifferentialController
from isaacsim.robot.wheeled_robots.robots import WheeledRobot
from isaacsim.storage.native import get_assets_root_path

# 开启Application和Simulation
simulation_app = SimulationApp({"headless": False})

# 创建World，定义World的度量单位
my_world = World(stage_units_in_meters=1.0)

# 添加Stage至Scene（注：jetbot.usd可理解为一个Stage，由多个Prim组成）
assets_root_path = get_assets_root_path()
if assets_root_path is None:
    carb.log_error("Could not find Isaac Sim assets folder")




my_robot_asset_path = "path/to/your/robot.usd"  # 替换为实际路径 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




my_robot = my_world.scene.add(
    WheeledRobot(
        prim_path="/World/MyRobot",  # 可以自定义路径
        name="my_robot",            # 自定义机器人名称
        wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],  # 修改为您机器人实际的轮子关节名称
        create_robot=True,
        usd_path=my_robot_asset_path,  # 使用您自己的机器人模型路径
        position=np.array([0, 0.0, 2.0]),  # 根据需要调整初始位置
    )
)








#my_world.scene.add_default_ground_plane()

# 移除默认地面
# my_world.scene.add_default_ground_plane()

# 添加您自己的场景
my_scene_asset_path = "path/to/your/scene.usd"  # 替换为您的场景文件路径 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
my_world.scene.add(
    usd_path=my_scene_asset_path,
    prim_path="/World/MyScene"
)








my_controller = DifferentialController(name="simple_control", wheel_radius=0.0675, wheel_base=0.233)
my_world.reset()

# 仿真逻辑
i = 0
reset_needed = False
while simulation_app.is_running():
    my_world.step(render=True)
    if my_world.is_stopped() and not reset_needed:
        reset_needed = True
    if my_world.is_playing():
        if reset_needed:
            my_world.reset()
            my_controller.reset()
            reset_needed = False
        if i >= 0 and i < 1000:
            # forward
            my_robot.apply_wheel_actions(my_controller.forward(command=[0.05, 0]))
            print(my_robot.get_linear_velocity())
        i += 1
    if args.test is True:
        break