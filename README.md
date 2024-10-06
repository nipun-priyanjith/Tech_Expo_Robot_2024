# Tech Expo Robot

<img src="https://github.com/nipun-priyanjith/Tech_Expo_Robot_2024/blob/main/tech_expo_robot/p1.png"/><br/><br/>
## Objective
This project involves developing a robot interface for the NIBM Tech Expo 2024, designed to guide users through the expo. The robot uses text-to-speech functionality along with animated facial expressions to interact with users and explain the location of different products in various rooms.

## Skills Learned
- Python GUI programming with Tkinter
- Multithreading and task management using queues
- Text-to-speech (TTS) integration via Pyttsx3
- Image handling and manipulation using Pillow (PIL)
- Interactive UI design and animation

## Tools Used
- **Python**: Main programming language
- **Tkinter**: For creating the graphical user interface
- **Pyttsx3**: For text-to-speech conversion
- **Pillow (PIL)**: For handling and manipulating images
- **Threading**: To manage animations and TTS concurrently

## Setup Guide


### Clone this repository:
  ```bash
  git clone https://github.com/nipun-priyanjith/Tech_Expo_Robot_2024.git
  ```
  
### Prerequisites:
- Python 3.x installed on your system
- Required Python packages:

  ```bash
  pip install tk pyttsx3 Pillow 
  ```

### Update Image Paths: 
- Update the code using your <b> ellips.png </b>  location
   
  ```bash
  ellips_image_path = r'your_location\tech_expo_robot_2024\tech_expo_robot\ellips.png'
  ```

### make your own Speech Texts and Images:
```bash
# Define the text to be spoken and associated expressions
   speech_texts = [
    ("Good morning dear. Welcome to tech expo 2024.", "y.png"),
    ("Thank you, I hope you enjoy our expo.", "f.png")
   ]
```

### Run the Python script:
```bash
python test14.py
```
<br/><br/>

<img src="https://github.com/nipun-priyanjith/Tech_Expo_Robot_2024/blob/main/tech_expo_robot/p2.png"/>  
