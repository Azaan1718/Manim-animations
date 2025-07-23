from manim import*

class Creation(Scene):
   def construct(self):
      x=1
      dx=0.1
      
      square=Square(color=BLUE,fill_color=BLUE,fill_opacity=0.5,side_length=x)
      self.play(Create(square))
      text_1=Text('x',font_size=25)
      self.play(text_1.animate.next_to(square,LEFT,buff=0.1))
      
      rectangle=Rectangle(color=RED,fill_color=RED,fill_opacity=0.7,width=dx,height=x)
      self.play(Create(rectangle))
      self.play(rectangle.animate.next_to(square,RIGHT,buff=0))
      rectangle_2=Rectangle(color=RED,fill_color=RED,fill_opacity=0.7,width=x+dx,height=dx)
      self.play(Create(rectangle_2))
      self.play(rectangle_2.animate.next_to(square,UP,buff=0))
      self.play(rectangle_2.animate.shift(RIGHT*dx/2))
      square_2=Square(color=YELLOW,fill_color=YELLOW,fill_opacity=1,side_length=dx)
      self.play(Create(square_2))
      self.play(square_2.animate.next_to(square,UP,buff=0))
      self.play(square_2.animate.shift(RIGHT*((x/2)+dx/2)))
      self.play(FadeOut(rectangle))
      self.play(FadeOut(rectangle_2))
      self.play(FadeOut(square_2))
      self.play(rectangle.animate.shift(RIGHT*6))
      self.play(rectangle_2.animate.shift(RIGHT*2))
      self.play(square_2.animate.shift(RIGHT*4))
      text_2=Text('dx',font_size=25)
      text_3=Text('dx',font_size=25)
      text_4=Text('dx',font_size=25)
      text_5=Text('x',font_size=25)
      text_6=Text('x',font_size=25)
      text_7=MathTex('+')
      text_8=MathTex('+')
      
      self.play(text_2.animate.next_to(square_2,buff=0.1))
      self.play(text_3.animate.next_to(rectangle_2,RIGHT,buff=0.1))
      self.play(text_4.animate.next_to(rectangle,UP,buff=0.1))
      self.play(text_5.animate.next_to(rectangle,RIGHT,buff=0.1))
      self.play(text_6.animate.next_to(rectangle_2,UP,buff=0.1))
      self.play(text_7.animate.next_to(rectangle_2,RIGHT,buff=0.7))
      self.play(text_8.animate.next_to(rectangle,LEFT,buff=0.4))
      formula=MathTex(r"\frac{d}{dx}(x^2)=2x")
      
      
      self.play(Write(formula))
      self.play(formula.animate.shift(DOWN*2,RIGHT*2))
      
      