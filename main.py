'''         Image processing and computer vision
                  Pedro Elí Ruiz Zárate
               Electronic engineering student
              Pontificia Universidad Javeriana
                      Bogotá - 2020
'''
from imageShape import * #Import class imageShape

if __name__ == '__main__':
    print('I´m PedroRuizCode     (°_°)\n') #Print string
    w = input('Enter the width of the image ') #Ask the user for the width
    h = input('Enter the height of the image ') #Ask the user for the height
    a = imageShape(int(w), int(h)) #Call imageShape class
    a.generateShape() #Call generateShape method
    a.showShape() #Call showShape method
    a.getShape() #Call getShape method
    a.whatShape() #Call whatShape method