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
text = str(input("Que texto deseas spammear?: "))
print("")
repe = int(input("Cuantas veces quieres enviar el mensaje: "))
print("")
delay = float(input("Cuanto durará un mensaje en enviarse? (Segundos) (Lo puede dejar en 0): "))

print("Tienes 5 segundos para abrir un chat")
time.sleep(5)


while i <= repe:
    pyautogui.typewrite(text)
    pyautogui.press("Enter")
    print(i)
    i = i + 1
    time.sleep(delay)

exit()

# Todos los derechos reservados a [Omar]