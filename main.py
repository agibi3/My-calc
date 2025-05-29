from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
import math 
import re
from kivy.uix.scrollview import ScrollView 
from kivy.factory import Factory as F
from kivy.clock import Clock
from kivy.lang import Builder 
from kivy.core.window import Window 


kv = '''
<Manager@ScreenManager>:
    canvas.before:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

<CustomInput@TextInput>:
    keyboard_mode: 'managed'
    background_normal: ''
    background_active: ''
    cursor_width: 0
    size_hint_y: None
    readonly: True
    halign: 'right'
    valign: 'middle'
    multiline: False
    font_name: 'DejaVuSans'
    padding: 10, 0

<CustomButton@Button>:
    font_name: 'DejaVuSans'
    font_size: 35
    background_normal: ''
    background_down: 'lightblue'
<CustomLabel@Label>:
    color: 'gold'
    text_size: self.width, None
    halign: 'center'
    valign: 'middle'
    size_hint_y: None
    height: 60 if self.texture_size[1] < 60 else self.texture_size[1]
    canvas.before:
        Color:
            rgb: 0, .6, .4
        Rectangle:
            size: self.size
            pos: self.pos
            '''
Builder.load_string(kv)
class Soft(App):
      def build(self):
          
          Window.bind(on_resize=self.adjust_heights)
          
          Clock.schedule_interval(self.move_text,0)
          Clock.schedule_interval(self.change_text,8.5)
          
          self.list = [
          ['History', 'rad', '^','C'],
          ['sin', 'cos', 'tan', '∛'],
          ['cosh', 'tanh', 'sinh','!'],
          ['%', 'ln', 'e', 'log'],
          ['(-)', ',', '√', 'π'],
          ['Del', '(', ')','÷'],
          ['7', '8', '9','-'],
          ['4', '5', '6','×'],
          ['1', '2', '3','+'],
          ['.', '0', 'Ans','=']]
          
          self.butts = ['1','2','3','4','5','6','7','8','9','0', 'rad','sin', 'cos', 'tan', '∛','cosh', 'tanh', 'sinh','!', 'ln', 'e', 'log','√', 'π','Ans','.','^','(-)','(',')','+','-','×','÷']
          
          self.operators = ['+', '-', '×','÷']
          
          self.last_button = None
          self.last_scrn = None
          self.last_operator = None
          
          global input1,input2,scientific,agiLabel,sm
          
          sm = F.Manager()
          # screen 1
          scrn1 = F.Screen(name = 'screenOne', size_hint_y=1)
              #scrn1 color .4,.4,.4
          mainLay = BoxLayout (orientation='vertical', size_hint_y=1)
          
          input1 = F.CustomInput(cursor_width=1, halign='left',readonly=False,height=(0.2*sm.height))
          input2 = F.CustomInput(font_size=60, height=(0.2*sm.height))
          scientific = F.CustomLabel(text='Scientific',font_size=50, height=(0.1*sm.height))
          agiLabel=F.CustomLabel (text = 'AgibisCalc', font_size=50, height=(0.1*sm.height))
          miniLays =[agiLabel, 
                     input1,
                     input2,
                     scientific]
          for layout in miniLays:
              mainLay.add_widget(layout)
          
          for row in self.list:
              lay =BoxLayout(padding=2,spacing=5)
              for text in row:
                  button=F.CustomButton(text=text)
                  if text == 'C' or text=='Del':
                      button.background_color= (1,0,0,.7)
                  elif text == 'History':
                      button.background_color= (0,0,1,.7)
                  else:
                     button.background_color= (0,.09,.0,.7)
                  button.bind(on_press = self.on_button_press)
                  lay.add_widget(button)
              mainLay.add_widget(lay)
          
          self.heights=Clock.schedule_once(lambda dt: [setattr(w, 'height', h) for w, h in [
    (input1, 0.07 * sm.height),
    (input2, 0.07 * sm.height),
    (agiLabel, 0.05 * sm.height),
    (scientific, 0.05 * sm.height)
]], 0)
          
          scrn1.add_widget(mainLay)
        
          #screen 2
          scrn2 = F.Screen(name = 'screenTwo') 
     
          lay = BoxLayout(orientation = 'vertical', spacing=20)
          
          histLabel = F.CustomLabel(text='History', font_size=50, color='blue',bold=True)
          lay.add_widget(histLabel)
          scroll_hist = ScrollView()
          self.hist_lay = BoxLayout(orientation ='vertical', size_hint_y= None, height=10, spacing=10)
          self.hist_lay.bind(minimum_height= self.hist_lay.setter('height'))
          scroll_hist.add_widget(self.hist_lay)
          
          lay.add_widget(scroll_hist)
          
          lay2 = BoxLayout (size_hint_y = None, height=75)
          prev_but = F.CustomButton(text = 'back',font_size=30, background_color='maroon')
          formu_but =F.CustomButton(text = 'formulars', background_color = 'green',font_size =30)
          prev_but.bind(on_press = self.on_button_press)
          formu_but.bind(on_press = self.on_button_press)
          lay2.add_widget(prev_but)
          lay2.add_widget(formu_but)
          lay.add_widget(lay2)
          scrn2.add_widget(lay)
          
          #screen 3
          scrn3 = F.Screen(name = 'screenThree')
          mainbox=BoxLayout (orientation='vertical')
          lay3 = F.CustomInput(readonly = True,size_hint_y=1,text = 'Basic Maths Formulas:'+'\n'+'01. Perimeter of Rectangle = 2(l+b)'+'\n'+'02. Area of Rectangle = l × b'+'\n'+ '03. Perimeter of Square = 4a'+'\n'+'04. Area of Square = a²'+'\n'+'05. Area of Triangle = (b×h)/2'+'\n'+'06. Circumference of Circle = 2πr'+'\n'+'07. Area of Circle = π × r²'+'\n'+'08.Surface Area of Cube = 6a²'+'\n'+'09. Volume of Cube = a³'+'\n'+'10. Curved Surface Area of Cylinder = 2πrh'+'\n'+'11. Total Surface Area of Cylinder = 2πr(r +h)'+'\n'+'12. Volume of Cylinder = πr²h'+'\n'+'13. Curved Surface Area of Cone = πrl'+'\n'+'14. Total Surface Area of Cone = πr(r + l)'+'\n'+'15. Volume of Cone = (πr²h)/3'+'\n'+'16. Surface Area of a Sphere = 4πr²'+'\n'+'17. Volume of a Sphere = 4/3 × πr³'+'\n'+'18. percentage Error = (error/actual)×100')
          mainbox.add_widget(lay3)
          self.btns = [
          ['back', 'home']
          ]
          for row in self.btns:
              minbox = BoxLayout (size_hint_y = None, height=75)
              for text in row:
                  btn = F.CustomButton (text=text, font_size =50, background_color='blue' if text=='home' else 'maroon')
                  btn.bind(on_press = self.on_button_press)
                  minbox.add_widget(btn)
              mainbox.add_widget(minbox)
          scrn3.add_widget(mainbox)
 
          screens =[
                    scrn1,
                    scrn2,
                    scrn3,
                     ]
          for screen in screens:
              sm.add_widget(screen)

          return sm
      
      
      def adjust_heights(self, *args):
          self.heights()
      
      def change_text(self,dt):
          if scientific.text == 'Scientific':
              scientific.text = 'Go Smart...!'
          else :
              scientific.text = 'Scientific'
      
      def move_text(self,dt):
          if agiLabel.texture_size[0] < agiLabel.width:
              agiLabel.texture_size[0]  +=2
          else:
              agiLabel.texture_size[0] =0
         
          
          #defining buttons action
      def on_button_press(self, instance):
          #try:
              button_text = instance.text
              curren = re.sub(r'\s+', '',input1.text)
              cursor_pos = input1.cursor_index()
              #screen navigation
              if button_text == 'History':
                  if sm.current == 'screenOne':
                      sm.current = 'screenTwo'
              elif button_text == 'back':
                  if sm.current == 'screenTwo':
                      sm.current= 'screenOne'
              elif button_text == 'formulars':
                  if sm.current== 'screenTwo':
                      sm.current = 'screenThree'
              elif button_text == 'home':
                  if sm.current== 'screenThree':
                      sm.current = 'screenOne'
              elif button_text == 'back':
                  if sm.current== 'screenThree':
                      sm.current = 'screenTwo'
    
              #other buttons function 
              elif button_text == 'C':
                  input1.text = ''
                  input2.text = ''
              elif button_text == 'Del':
                  deleted = 0
                  if curren == "Hey; you can't type an operator first" or curren== 'Ans' or curren== 'Error':
                      input1.text=''
                      input1.cursor=(0, 0)
                  elif curren[cursor_pos-3: cursor_pos] == 'Ans':
                      input1.text=curren[:cursor_pos-3]+curren[cursor_pos:]
                      input1.cursor=(cursor_pos-3, 0)
                      
                      
                  else:
                      input1.text = curren[:cursor_pos-1]+curren[cursor_pos:]
                      input1.cursor=(cursor_pos-1, 0)
              elif button_text == '^' and input1.text == '':
                  return 
              elif button_text == '!' and curren == '':
                  return
              elif button_text == '%' and curren == '':
                  return
              elif self.last_button == '=':
                  if  button_text in self.operators:
                      input1.text = 'Ans'+button_text
                  elif button_text == 'Ans':
                      input1.text = ''
                      input1.text = button_text
                  elif button_text in self.butts[:24]:
                      input1.text = button_text    
              elif button_text == '(-)':
                  input1.text = curren[:]+'-'
              elif self.last_button == 'Ans' and button_text == button_text in self.operators:
                  input1.text = curren[:]+button_text            
              elif self.last_button == button_text in self.operators and button_text == button_text in self.operators:
                  return 
              elif curren == '' and button_text == button_text in self.operators:
                  input1.text = "Hey; you can't type an operator first"      
              elif button_text == '=':
                  symbols = ['√','cos','log','deg','sin', 'tan', 'ln','π', 'tanh','sinh', 'cosh', 'rad', '∛','e','Ans']
                  for symbol in symbols:
                      src= [match.start() for match in re.finditer(symbol, curren)]
                      for position in reversed(src):
                          if position>0 and curren[position-1] not in '*+-/÷×':
                              curren= curren[: position]+'*'+curren[position:]
                  if '!'or '√' or '×' or '^' or '%' or 'log' or '÷' or 'π' or 'deg' in curren:
                      sc1 = curren.replace('×','*')
                      sc2 = sc1.replace('÷', '/')
                      sc3 = sc2.replace('^', '**')
                      sc4 = sc3.replace('%', '/100')
                      sc5 = sc4.replace('π', 'math.pi')
                      sc6 = re.sub(r'∛(\d+)', lambda result: str(float(result.group(1))**(1/3)), sc5)
                      sc7 = re.sub(r'log(\d+)', lambda result: str(math.log10(float(result.group(1)))), sc6)
                      sc8 =re.sub(r'(\d+)!', lambda result: str(math.factorial(int(result.group(1)))), sc7)
                      sc9 = re.sub(r'ln(\d+)', lambda result: str(math.log(float(result.group(1)))), sc8)
                      sc10 = sc9.replace('Ans', input2.text)
                      sc11 = sc10.replace('e', 'math.e')
                      sc12 = re.sub(r'rad(\d+)', lambda result: str(math.radians(float(result.group(1)))),sc11)
                      sc13 = re.sub(r'tan(\d+)', lambda result: str(math.tan(float(result.group(1)))),sc12)
                      sc14 = sc13.replace(',','')
                      sc15 = re.sub(r'sin(\d+)', lambda result: str(math.sin(float(result.group(1)))),sc14)
                      sc16 = re.sub(r'cos(\d+)', lambda result: str(math.cos(float(result.group(1)))),sc15)
                      sc17 = re.sub(r'sinh(\d+)', lambda result: str(math.sinh(float(result.group(1)))),sc16)
                      sc18 = re.sub(r'cosh(\d+)', lambda result: str(math.cosh(float(result.group(1)))),sc17)
                      sc19 = re.sub(r'tanh(\d+)', lambda result: str(math.tanh(float(result.group(1)))),sc18)
                      sc20 = re.sub(r'√(\d+)', lambda result: str(math.sqrt(float(result.group(1)))),sc19)
                      input2.text =str(round(float(eval(sc20)),7)) 
                         
     
                      #set history
                      if input2.text != '':
                          label = F.CustomLabel(text=f' {input1.text} = {input2.text}',font_size=50, color='white')
                          self.hist_lay.add_widget(label)
                      else: 
                          pass
                      if not '.' in input2.text and len(input2.text)>15:
                          input2.text = '{:.9e}'.format(int(input2.text))
                      
              else:    #add text at cursor  position 
                  input1.text = curren[:cursor_pos]+button_text+curren[cursor_pos:]
                  input1.cursor = (cursor_pos+len(button_text),0)
                  curren = input1.cursor
              self.last_button = button_text
              self.last_operator = button_text in self.operators
          #except:
              #return 
if __name__ == "__main__":     
  Soft().run()
