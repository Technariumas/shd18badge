## Experiences of a mac user getting the Tardigrade set up

1. Install drivers as per [the README](README.md). 
2. Open a terminal, plug the tardigrade in to your computer, and run `sudo dmesg` in the terminal. 
3. You should see a line like this, or something similar: `wch_usb detach. provider USB2.0-Serial.` - if not, unplug the tardigrade and plug it back in again before re-running `sudo dmesg`.
4. We now know we're looking for a device called wch_usb. run `ls /dev/tty.wchusb` and press tab to get the exact device name. It might be `/dev/tty.wchusbserial1410`.
5. Ok, we're ready to connect to the device! We'll open a session using the program called *screen*. Type `screen /dev/tty.wchusbyourdevice here  115200` - for me it was `screen /dev/tty.wchusbserial1410  115200`. 
6. After a few seconds, you should start seeing the temperature being output continuously to the screen now. Try putting your finger on the temperatures sensor (bottom middle of the tardigrade on the LED side) and watch the numbers change!
7. Press ctrl+c on your keyboard to stop the temperature output. Now you'll have a command prompt where you can type commands to your tardigrade. 
8. Try some commands like `flash(200)`, `getTemperature`, `setPixel(255,0,100)`, `setLeds(0b10101010)`, or `wigglefeet`. You can see the full list here: https://github.com/Technariumas/shd18badge/blob/master/micropython/main.py 

Some more tips:

- press ctrl+d to start the temperature readings again
- press ctrl+a+d to detach from the screen session and get your terminal window back.
- if you want to go back to the screen session and you haven't unplugged your tardigrade, type `screen -dr` to start playing with your tardigrade again. 

## setLeds:

You'll always need to leave 0b there, but try changing `01010101` to something else - there's one number for each tardigrade foot, and you can switch them all off by setting them to 0, e.g. `setLeds(0b00000000)`. Can you guess how to turn them all on? 
