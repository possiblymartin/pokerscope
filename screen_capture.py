import mss
import numpy as np

# give a list of monitors for the user to choose from
def monitor_list():
  with mss.mss() as sct:
    monitors = sct.monitors
    return monitors

def monitor_prompt(monitors):
  print("Please choose the monitor you would like to capture from:")
  for i, monitor in enumerate(monitors):
    print(f"{i}: {monitor}")

  while True:
    try:
      selection = int(input("Enter the number of the monitor you would like to capture: "))
      if 0 <= selection < len(monitors):
        return selection
      else:
        print("Invalid selection. Please try again.")
    except ValueError:
      print("Please enter a valid number")

def capture_screen(display):
  with mss.mss() as sct:
    screenshot = np.array(sct.grab(display))
  return screenshot

def main():
  monitors = monitor_list()
  selected_monitor = monitor_prompt(monitors)
  print(f"You have selected monitor {selected_monitor}")

  capture_screen(selected_monitor)


if __name__ == "__main__":
  main()