import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class SmartHomeSimulator:
    def __init__(self, master):
        self.master = master
        master.title("Smart Home IoT Simulator")

        self.create_widgets()

        # Schedule a function to simulate temperature changes every 5 seconds
        self.master.after(5000, self.update_temperature)

    def create_widgets(self):
        # Thermostat Frame
        thermostat_frame = ttk.LabelFrame(self.master, text="Thermostat")
        thermostat_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.temperature_label = ttk.Label(thermostat_frame, text="Set Temperature:")
        self.temperature_label.grid(row=0, column=0, padx=10, pady=10)

        self.temperature_entry = ttk.Entry(thermostat_frame)
        self.temperature_entry.grid(row=0, column=1, padx=10, pady=10)

        self.thermostat_button = ttk.Button(thermostat_frame, text="Adjust Thermostat", command=self.adjust_thermostat)
        self.thermostat_button.grid(row=0, column=2, padx=10, pady=10)

        self.current_temperature_label = ttk.Label(thermostat_frame, text="Current Temperature: 25.00°C")  # Initial value
        self.current_temperature_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        # Smart Lights Frame
        lights_frame = ttk.LabelFrame(self.master, text="Smart Lights")
        lights_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.light_label = ttk.Label(lights_frame, text="Room:")
        self.light_label.grid(row=0, column=0, padx=10, pady=10)

        self.room_combobox = ttk.Combobox(lights_frame, values=["Living Room", "Bedroom", "Kitchen"])
        self.room_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.room_combobox.set("Living Room")

        self.brightness_label = ttk.Label(lights_frame, text="Brightness:")
        self.brightness_label.grid(row=0, column=2, padx=10, pady=10)

        self.brightness_slider = ttk.Scale(lights_frame, from_=0, to=100, orient=tk.HORIZONTAL)
        self.brightness_slider.grid(row=0, column=3, padx=10, pady=10)

        self.light_button_on = ttk.Button(lights_frame, text="Lights On", command=self.turn_lights_on)
        self.light_button_on.grid(row=2, column=0, padx=10, pady=10)

        self.light_button_off = ttk.Button(lights_frame, text="Lights Off", command=self.turn_lights_off)
        self.light_button_off.grid(row=2, column=1, padx=10, pady=10)

        # Security Camera Frame
        camera_frame = ttk.LabelFrame(self.master, text="Security Camera")
        camera_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.security_camera_button = ttk.Button(camera_frame, text="Check Security Camera", command=self.check_security_camera)
        self.security_camera_button.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        # Log Frame
        log_frame = ttk.LabelFrame(self.master, text="Activity Log")
        log_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        self.log_text = tk.Text(log_frame, height=15, width=50)
        self.log_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Dictionary to store the state of each room
        self.room_states = {"Living Room": {"brightness": 0},
                            "Bedroom": {"brightness": 0},
                            "Kitchen": {"brightness": 0}}

    def log_activity(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)  # Scroll to the end to show the latest log

    def adjust_thermostat(self):
        try:
            desired_temperature = float(self.temperature_entry.get())
            current_temperature = random.uniform(18, 25)  # Simulate dynamic temperature changes

            # Update the current temperature label
            self.current_temperature_label.config(text=f"Current Temperature: {current_temperature:.2f}°C")

            if current_temperature < desired_temperature and desired_temperature > 20:
                self.log_activity(f"Heater is turned on until {desired_temperature}°C.")
            elif current_temperature > desired_temperature or desired_temperature <= 20:
                self.log_activity(f"AC is turned on until {desired_temperature}°C.")
            else:
                self.log_activity("Temperature is already at the desired level.")
        except ValueError:
            self.log_activity("Invalid temperature input. Please enter a valid number.")

    def turn_lights_on(self):
        room = self.room_combobox.get()
        brightness = round(self.brightness_slider.get())
        self.room_states[room]["brightness"] = brightness
        self.log_activity(f"Lights in {room} are turned on with brightness {brightness}%.")

    def turn_lights_off(self):
        room = self.room_combobox.get()
        self.room_states[room]["brightness"] = 0
        self.log_activity(f"Lights in {room} are turned off.")

    def check_security_camera(self):
        # Simulate movement detection 24/7
        self.log_activity("Movement is detected.")
        # Simulate intruder detection
        self.log_activity("Intruder detected! Capturing snapshot.")
        self.capture_intruder()

    def update_temperature(self):
        # Simulate a temperature change
        current_temperature = random.uniform(18, 25)  # Random value between 18 and 25 for simulation
        self.current_temperature_label.config(text=f"Current Temperature: {current_temperature:.2f}°C")

        # Schedule the next temperature update in 5 seconds
        self.master.after(5000, self.update_temperature)

    def capture_intruder(self):
        # Simulate capturing an image (you can replace this with actual image capture logic)
        image_path = "intruder_snapshot.jpg"
        image = Image.open(image_path)
        image = image.resize((200, 150), Image.BILINEAR)  # or Image.BICUBIC
        photo = ImageTk.PhotoImage(image)

        # Display the captured image in a new window
        capture_window = tk.Toplevel(self.master)
        capture_window.title("Intruder Snapshot")

        label = ttk.Label(capture_window, image=photo)
        label.photo = photo  # Keep a reference to the image to prevent garbage collection
        label.pack(padx=10, pady=10)



if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomeSimulator(root)
    root.mainloop()
