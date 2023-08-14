from Focus_Roots import *

def change():
    set_background(color_violet) #Background

    write_text("A Girl",230,70,50,color=color_aquamarine)

    draw_rect(130,140,200,400,0,color=color_black) #Back Hair
   
    draw_rect(150,150,200,130,0,color=color_skin) #Head
    draw_polygon([[250,335],[150,280],[345,280]],0,color=color_skin) #Head


    draw_rect(180,200,15,45,0,color=color_light_salmon) #Eyes
    draw_rect(280,200,15,45,0,color=color_light_salmon) #Eyes
    draw_rect(170,200,50,10,0,color=color_black) #Eyes
    draw_rect(270,200,50,10,0,color=color_black) #Eyes
    draw_rect(230,280,45,5,0,color=color_black) #Mouth
    draw_rect(237,285,30,8,0,color=color_violet_red) #Mouth

    draw_ellipse(130,100,150,80,0,color=color_black) #Top hair
    draw_ellipse(220,100,140,80,0,color=color_black) #Top hair
    draw_rect(150,130,210,60,0,color=color_black) #Front Hair

    draw_ellipse(125,210,40,50,0,color=color_skin) #ears

    draw_rect(220,300,50,50,0,color=color_skin) #Neck
    draw_rect(90,350,300,200,0,color=color_mid_night_blue) #shirt
    draw_rect(90,460,65,50,0,color=color_skin) #Arms
    draw_rect(325,460,65,50,0,color=color_skin) #Arms
    


draw(change)