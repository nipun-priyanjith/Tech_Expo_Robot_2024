import tkinter as tk
import pyttsx3
import threading
import time
import queue
from PIL import Image, ImageTk

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define the text to be spoken and associated expressions
speech_texts = [
    ("Good morning dear. Welcome to tech expo 2024.", "y.png"),
    ("We have good products to present to you.", "y.png"),
    ("First room: Left side: Casper","sstt.png"),
    ("  it's a smart home powered by AI.", "y.png"),
    ("Right side: Crash","sstt.png"),
    ("  it's a military robot, it can manually fight.", "y.png"),
    ("Second room: Left side: Saver ","sstt.png"),
    (" it helps farmers to maintain the food.", "y.png"),
    ("Right side: Bleas ","sstt.png"),
    (" healthcare robot.", "y.png"),
    ("Thank you, I hope you enjoy our expo.", "f.png")
]

# Create a queue to manage speech tasks
speech_queue = queue.Queue()

# Function to handle speech with specified expressions
def speak_with_expression(text, eye_image_path):
    stop_event = threading.Event()
    
    # Use threading to handle eyes and mouth expressions
    eyes_thread = threading.Thread(target=animate_eyes, args=(eye_image_path, stop_event))
    mouth_thread = threading.Thread(target=animate_mouth, args=(stop_event,))
    
    eyes_thread.start()
    mouth_thread.start()
    
    def speak():
        engine.say(text)
        engine.runAndWait()
        stop_event.set()
    
    speech_queue.put(speak)

# Function to set and animate eye expressions
def animate_eyes(image_path, stop_event):
    global left_eye, right_eye, ellips_image
    img = ImageTk.PhotoImage(Image.open(image_path).resize((eye_size, eye_size)))
    canvas.delete(left_eye)
    canvas.delete(right_eye)
    left_eye = canvas.create_image(center_x - eye_spacing, center_y - eye_vertical_offset, image=img, anchor=tk.CENTER)
    right_eye = canvas.create_image(center_x + eye_spacing, center_y - eye_vertical_offset, image=img, anchor=tk.CENTER)
    canvas.image = img  # Keep a reference to the image to prevent garbage collection

    # Eye movement animation
    movements = [
        (5, 0), (-5, 0), (0, 5), (0, -5)
    ]

    def move_eyes():
        while not stop_event.is_set():
            try:
                initial_coords_left = canvas.coords(left_eye)
                initial_coords_right = canvas.coords(right_eye)
                for move in movements:
                    new_coords_left = [initial_coords_left[0] + move[0], initial_coords_left[1] + move[1]]
                    new_coords_right = [initial_coords_right[0] + move[0], initial_coords_right[1] + move[1]]
                    canvas.coords(left_eye, *new_coords_left)
                    canvas.coords(right_eye, *new_coords_right)
                    canvas.update()
                    time.sleep(0.5)
                    if stop_event.is_set():
                        break
            except IndexError:
                pass

    threading.Thread(target=move_eyes, daemon=True).start()

# Function to animate the mouth with different expressions
def animate_mouth(stop_event):
    global mouth
    while not stop_event.is_set():
        for shape in mouth_shapes_talk:
            canvas.coords(mouth, *shape)
            canvas.update()
            if stop_event.is_set():
                break
            time.sleep(0.2)  # Adjust the sleep time to control the speed of the animation
        # Reset to the default mouth position
        canvas.coords(mouth, *mouth_coords)

# Function to handle click event
def on_face_click(event):
    def process_texts():
        for text, eye_image_path in speech_texts:
            speak_with_expression(text, eye_image_path)
            speech_queue.join()
        speak_with_expression(" ", "ellips.png")  # Reset eyes to default after speech sequence

    threading.Thread(target=process_texts, daemon=True).start()

# Function to process the speech queue
def process_speech_queue():
    while True:
        speak_func = speech_queue.get()
        speak_func()
        speech_queue.task_done()

# Create the main window
root = tk.Tk()
root.title("Tech Expo Robot")
root.configure(bg='black')

# Set full screen
root.attributes('-fullscreen', True)

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Center coordinates
center_x = screen_width // 2
center_y = screen_height // 2

# Eye and mouth positioning
eye_size = 200  # Adjust the size of the eyes here
eye_spacing = 150  # Adjust the spacing between the eyes here
eye_vertical_offset = 100  # Adjust the vertical offset of the eyes here

# Load images
ellips_image_path = r'D:\projects\NIBM_EXPO_road_explain_robot\ellips.png'

ellips_image = ImageTk.PhotoImage(Image.open(ellips_image_path).resize((eye_size, eye_size)))

# Create the canvas for drawing the face
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='black', highlightthickness=0)
canvas.pack()

# Default eye shape and color
left_eye = canvas.create_image(center_x - eye_spacing, center_y - eye_vertical_offset, image=ellips_image, anchor=tk.CENTER)
right_eye = canvas.create_image(center_x + eye_spacing, center_y - eye_vertical_offset, image=ellips_image, anchor=tk.CENTER)

# Draw the mouth with voice wave shapes
mouth_length = 200  # Adjust the length of the mouth here
mouth_vertical_offset = 150  # Adjust the vertical offset of the mouth here

mouth_coords = [center_x - mouth_length // 2, center_y + mouth_vertical_offset, center_x + mouth_length // 2, center_y + mouth_vertical_offset]  # Adjusted straight line
mouth_shapes_talk = [
    [center_x - mouth_length // 2, center_y + mouth_vertical_offset, center_x - mouth_length // 4, center_y + mouth_vertical_offset - 5, center_x + mouth_length // 4, center_y + mouth_vertical_offset - 5, center_x + mouth_length // 2, center_y + mouth_vertical_offset],  # Talk shape 1
    [center_x - mouth_length // 2, center_y + mouth_vertical_offset, center_x - mouth_length // 3, center_y + mouth_vertical_offset - 10, center_x + mouth_length // 3, center_y + mouth_vertical_offset + 10, center_x + mouth_length // 2, center_y + mouth_vertical_offset],  # Talk shape 2
    [center_x - mouth_length // 2, center_y + mouth_vertical_offset, center_x - mouth_length // 4, center_y + mouth_vertical_offset - 15, center_x + mouth_length // 4, center_y + mouth_vertical_offset + 15, center_x + mouth_length // 2, center_y + mouth_vertical_offset],  # Talk shape 3
    [center_x - mouth_length // 2, center_y + mouth_vertical_offset, center_x - mouth_length // 3, center_y + mouth_vertical_offset - 10, center_x + mouth_length // 3, center_y + mouth_vertical_offset + 10, center_x + mouth_length // 2, center_y + mouth_vertical_offset],  # Talk shape 2
    [center_x - mouth_length // 2, center_y + mouth_vertical_offset, center_x - mouth_length // 4, center_y + mouth_vertical_offset - 5, center_x + mouth_length // 4, center_y + mouth_vertical_offset - 5, center_x + mouth_length // 2, center_y + mouth_vertical_offset]   # Talk shape 1
]
mouth = canvas.create_line(*mouth_coords, fill='#07f523', width=5, smooth=True)

# Bind the click event to the canvas
canvas.bind("<Button-1>", on_face_click)

# Start the speech queue processing thread
speech_thread = threading.Thread(target=process_speech_queue, daemon=True)
speech_thread.start()

# Run the application
root.mainloop()
