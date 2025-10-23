import os
import shutil
import json
from vehicle import Car
from vehicle import Driver
import driving_inputs
from PIL import Image
import utils
from pathlib import Path


def main():
    robot = Car()
    driver = Driver()

    timestep = int(robot.getBasicTimeStep())

    #camera
    camera = robot.getDevice("camera")
    camera.enable(timestep)  # timestep

    #Controller
    controller = driving_inputs.XboxOrKeyboardController()

    #Remove & Create folders
    current_folder = Path(__file__).parent
    dataset_folder = current_folder / "dataset"
    if dataset_folder.exists():
        shutil.rmtree(dataset_folder)
    image_folder = dataset_folder / "images"
    os.makedirs(image_folder, exist_ok=True)

    step = 0
    while robot.step() != -1:
        #get image from camera
        image = utils.get_image_rgb(camera)

        leftY, rightX = controller.y_x()

        print(f"leftY {leftY:.2f} - rightY {rightX:.2f}")

        throttle = leftY * 45  # max speed
        angle = rightX * 0.25

        print(f"throttle {throttle:.2f} - angle {angle:.2f}")

        driver.setSteeringAngle(angle)
        driver.setCruisingSpeed(throttle)

        #notsave files if the vehcile is not moving
        if throttle == 0:
            continue

        #saving data
        im = Image.fromarray(image)
        image_path = image_folder / f"image_{step}.png"
        im.save(image_path)

        command = {"angle": angle, "throttle": throttle, "image": str(image_path)}
        with open(dataset_folder / f"frame_{step}.json", "w") as f:
            json.dump(command, f)

        #increase step
        step += 1


if __name__ == "__main__":
    main()
