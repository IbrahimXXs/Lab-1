from pynput import keyboard
import mujoco
import mujoco_viewer
import time

# Load model
model = mujoco.MjModel.from_xml_path('Misc/2Dsimreal_grasp.xml')
data = mujoco.MjData(model)
ctrl = data.ctrl
viewer = mujoco_viewer.MujocoViewer(model, data)

# Initial activation values
activation = [0.0, 0.0]

# Key press state tracking
key_state = {'a': False, 's': False, 'k': False, 'l': False}

def on_press(key):
    try:
        if key.char in key_state:
            key_state[key.char] = True
    except AttributeError:
        pass

def on_release(key):
    try:
        if key.char in key_state:
            key_state[key.char] = False
    except AttributeError:
        pass

# Start the keyboard listener thread
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while True:
    # Update activations based on key states
    for i, keys in enumerate([['a', 's'], ['k', 'l']]):
        if any(key_state[k] for k in keys):
            activation[i] = min(activation[i] + 0.1, 1.0)
        else:
            activation[i] = max(activation[i] - 0.1, 0.0)

    ctrl[0], ctrl[1] = activation
    mujoco.mj_step(model, data)
    viewer.render()
    time.sleep(0.01)
