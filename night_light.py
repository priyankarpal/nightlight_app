import subprocess
import time

    # make sure to replace the display_name with your own display name using `xrandr` command
def set_night_light(enabled, display_name="eDP"): 
    # Adjust these values based on your preference
    night_light_color = (1.00, 0.85, 0.70)  # RGB values for a warm color with reduced blue component
    transition_duration = 2  # seconds

    if enabled:
        # Adjust the color temperature using xrandr or any other tool
        command = f"xrandr --output {display_name} --gamma {night_light_color[0]}:{night_light_color[1]}:{night_light_color[2]}"
        subprocess.run(command, shell=True)

        time.sleep(transition_duration)  # Wait for the transition

    else:
        # Reset to the default color temperature
        command = f"xrandr --output {display_name} --gamma 1:1:1"
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    set_night_light(enabled=True)
