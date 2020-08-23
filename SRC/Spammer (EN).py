import time
import pyautogui

text = ""
repe = 500
delay = 0
i = 1
print("------------------------------------------------------------------------")
print("")
print("       ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗")
print("       ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗")
print("       ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝")
print("       ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗")
print("       ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║")
print("       ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝")

print("                                By Omar.")
print("")
print("------------------------------------------------------------------------")
print("")
print("")
text = str(input("What text does Spamear want?: "))
print("")
repe = int(input("How many times do you want to send the message: "))
print("")
delay = float(input("Every time the message will be sent (Seconds): "))

print("You have 5 seconds to open a chat")
time.sleep(5)


while i <= repe:
    pyautogui.typewrite(text)
    pyautogui.press("Enter")
    print(i)
    i = i + 1
    time.sleep(delay)

exit()

# Todos los derechos reservados a [Omar]