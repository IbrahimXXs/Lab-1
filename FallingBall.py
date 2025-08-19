import mujoco
import mujoco_viewer
import time

# Load model
model = mujoco.MjModel.from_xml_path('FallingBall.xml')
data = mujoco.MjData(model)
ctrl = data.ctrl
viewer = mujoco_viewer.MujocoViewer(model, data)

while viewer.is_alive:
 
    mujoco.mj_step(model, data)
    viewer.render()
    time.sleep(0.01) 