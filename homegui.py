from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout

class HomeApp(App):
    def build(self):
        
        hlayout = BoxLayout(orientation = 'horizontal',
                            spacing=10,
                            )

        currTempLabel = Label(text = '78',
                          font_size = 150,
                          )

        hlayout.add_widget(currTempLabel)

        vlayout = BoxLayout(orientation = 'vertical',
                            spacing = 10
                            )

        setpointLayout = BoxLayout(orientation = 'horizontal',
                                   spaving = 30,
                                   )

        setpointLabel = Label(text = '72',
                              font_size = 100,
                              )

        setpointLayout.add_widget(setpointLabel)
        
        tempSlider = Slider(orientation = 'vertical',
                            min=40,
                            max=100,
                            value=72,
                            step=1,
                            )

        setpointLayout.add_widget(tempSlider)
        
        vlayout.add_widget(setpointLayout)

        # options
        optionsLayout = BoxLayout(orientation = 'horizontal',
                                   spaving = 30,
                                   )

        heatBtn = ToggleButton(text='Heat',
                               group='onoff',
                               font_size=30,
                               size_hint = (.3, 1)
                               )

        coolBtn = ToggleButton(text='Cool',
                               group='onoff',
                               font_size=30,
                               size_hint = (.3, 1)
                               )

        offBtn = ToggleButton(text='Off',
                              group='onoff',
                              font_size=30,
                              size_hint = (.3, 1)
                              )

        fanLabel = Label(test='      Fan',
                         font_size = 30,
                         size_hint = (.3, 1)
                         )
                         

        fanAutoBtn = ToggleButton(text='Auto',
                                  group='fan',
                                  font_size=30,
                                  size_hint = (.3, 1)
                                  )

        fanOnBtn = ToggleButton(text='On',
                                group='fan',
                                font_size=30,
                                size_hint = (.3, 1)
                                )


        for btn in [heatBtn, coolBtn, offBtn, fanLabel, fanAutoBtn, fanOnBtn]:
            optionsLayout.add_widget(btn)
        

        vlayout.add_widget(optionsLayout)
    
        hlayout.add_widget(vlayout)
        
        quitBtn = Button(text='Quit',
                         background_color=(1,0,0,1),
                         font_size = 30,
                         size_hint = (.2, 1),
                         )
        quitBtn.bind(on_release = self.stop)

        vlayout.add_widget(quitBtn)
        return hlayout

if __name__ == "__main__":
    HomeApp().run()
    
