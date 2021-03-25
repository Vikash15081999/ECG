# import bluetooth

# target_name = "Hc-05"
# target_address = None

# nearby_devices = bluetooth.discover_devices()

# for bdaddr in nearby_devices:
#     if target_name == bluetooth.lookup_name( bdaddr ):
#         target_address = bdaddr
#         break

# if target_address is not None:
#     print("found target bluetooth device with address "), target_address
# else:
#     print("could not find target bluetooth device nearby")

from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

#from kivy.config import Config
import matplotlib.animation as animation




#Config.set('graphics', 'resizable', True)

plt.ylabel('readings')
plt.title('Your ECG')


red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue =  [0, 0, 1, 1]
purple = [1, 0, 1, 1]

canvas =FigureCanvasKivyAgg(plt.gcf())
class MainApp(App):
    def build(self):
        superBox = BoxLayout(orientation ='vertical')
  
        # To position widgets next to each other,
        # use a horizontal BoxLayout.
        
  
        colors = [red, green, blue, purple]
          
      
  
        # To position widgets above/below each other,
        # use a vertical BoxLayout.
        VB = BoxLayout(orientation ='vertical',size_hint =( 1,None))
  
        btn3 = Label(text ="[b][size=20][color=ff3333]ECG Monitoring System[/color][/size][/b]",markup = True)
        btn4 = Button(text ="Print as PDF",
                      background_color = green,
                      font_size = 15,
                      size_hint =(0.3, 0.5),
                      pos_hint ={'right':1})
        btn4.bind(on_release=self.on_press_button)
        # VB represents the vertical boxlayout orientation
        # declared above
        VB.add_widget(btn3)
        VB.add_widget(btn4)
  
        # superbox used to again align the orented widgets
       
        superBox.add_widget(VB)
        
        
        superBox.add_widget(canvas)
        VB1 = BoxLayout(orientation ='vertical',size_hint =( 1,None))
        btn5 = Button(text ="REFRESH",
                      background_color = green,
                      font_size = 15,
                      size_hint =(0.3, 0.5),
                      pos_hint ={'right':1})
        btn5.bind(on_release=self.animate)
        VB1.add_widget(btn5)
        superBox.add_widget(VB1)
        return superBox

    def animate(self, instance):
        
        if(instance.background_color==green):
            instance.background_color=blue
        else:
            instance.background_color=green
      
        
        dataArray = [[1,2],[2,3],[3,6],[4,9],[5,4],[6,7],[7,7],[8,4],[9,3],[10,7]]
        xar = []
        yar = []
        for eachLine in dataArray:
            if len(eachLine)>1:
                x,y = eachLine[0],eachLine[1]
                xar.append(int(x))
                yar.append(int(y))
        plt.plot(xar,yar)
        
        canvas.draw()
        print("completed")

    def on_press_button(self, instance):
        if(instance.background_color==green):
            instance.background_color=blue
        else:
            instance.background_color=green
        plt.savefig('line_plot.pdf')
        print('You have downloaded')
    
        

if __name__ == '__main__':
    app = MainApp()
    app.run()