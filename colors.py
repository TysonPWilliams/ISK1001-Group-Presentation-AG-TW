# Imports functions and classes from color50 to define and apply RGB color styling to the CLI console output
from color50 import rgb, constants, Color 

# Throughout this program's code you will see many f-strings that have {primary_text}
# and {secondary_text}, this is the color of the text in the command line. Within
# colors.py you can find the color variables/objects that are used.

# Define color variables using RGB values for styling the console output
primary_text = rgb(204, 229, 255) # Light blue for primary text

secondary_text = rgb(102, 178, 255) # Lighter blue for secondary text

error_text = rgb(255, 0, 0) # Red for error messages

# Define color objects for headings and body text
heading = Color()
heading.red = 204
heading.green = 229
heading.blue = 255

body_text = Color()
body_text.red = 102
body_text.green = 178
body_text.blue = 255

