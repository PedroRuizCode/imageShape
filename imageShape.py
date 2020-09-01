'''         Image processing and computer vision
                  Pedro Elí Ruiz Zárate
               Electronic engineering student
              Pontificia Universidad Javeriana
                      Bogotá - 2020
'''
import numpy #import numpy library
import cv2 #import openCV library

class imageShape: #create the class imageShape

    def __init__(self, width, height): #Initialize the class
        self.width = width #Assign width to self
        self.height = height #Assign height to self
        self.shape = numpy.zeros((self.height, self.width, 3), dtype=numpy.uint8) #Create 3-Component Array on Zeros

    def generateShape(self): #create the method generateShape
        w_centre = self.width / 2 #Center of width
        h_centre = self.height / 2 #Center of height
        min_hw = int(min(self.height, self.width) / 2) #Minimum between width and height divided by 2
        self.rand_n = numpy.random.randint(4) #Random number from 0 to 3
        if self.rand_n == 0: #If the number is 0 I draw a triangle
            #To calculate pt1, pt2 and pt3, the length of each of the sides is calculated and using
            #trigonometric functions the position of each point is calculated.
            p1t = (int(w_centre), int(h_centre - int((numpy.sqrt(3) / 2) * (min_hw / 2))))
            p2t = (int(w_centre) - int(self.width / 4), int(h_centre + ((numpy.sqrt(3) / 2) * (min_hw / 2))))
            p3t = (int(w_centre) + int(self.width / 4), int(h_centre + ((numpy.sqrt(3) / 2) * (min_hw / 2))))
            pts = numpy.array([p1t, p2t, p3t]) #The array is created with pt1, pt2 and pt3
            self.shape = cv2.drawContours(self.shape, [pts], 0, (255, 255, 0), -1) #Draw the triangle over self.shape
        elif self.rand_n == 1: #If the number is 1 I draw a square
            #p1s is the minimum between width and height is taken and 1/4 of the minimum is shifted backwards.
            #p2s is the minimum between width and height is taken and 1/4 of the minimum is shifted forward.
            p1s = (int(w_centre) - int(min_hw / 2), int(h_centre) - int(min_hw / 2))
            p2s = (int(w_centre) + int(min_hw / 2), int(h_centre) + int(min_hw / 2))
            cv2.rectangle(self.shape, p1s, p2s, [255, 255, 0], -1) #Draw the square
            rot_sq = cv2.getRotationMatrix2D((int(w_centre), int(h_centre)), 45, 1.0) #Rotate the square
            self.shape = cv2.warpAffine(self.shape, rot_sq, (self.width, self.height))#Draw the rotated square
        elif self.rand_n == 2: #If the number is 2 I draw a rectangle
            #To calculate p1r, take half the width and the height and move 1/4 backwards.
            #To calculate p2r, take half the width and the height and move 1/4 forward.
            p1r = (int(w_centre) - int(self.width / 4), int(h_centre) - int(self.height / 4))
            p2r = (int(w_centre) + int(self.width / 4), int(h_centre) + int(self.height / 4))
            cv2.rectangle(self.shape, p1r, p2r, [255, 255, 0], -1) #Draw the rectangle over self.shape
        else: #If the number is 3 I draw a circle
            cv2.circle(self.shape, (int(w_centre), int(h_centre)), int(min_hw / 2), [255, 255, 0], -1)#Draw the circle

    def showShape(self): #create the method showShape
        cv2.imshow(' ', self.shape) #Show the content of self.shape
        cv2.waitKey(5000) #5 second delay

    def getShape(self): #create the method getShape
        #Read the value of the variable rand_n and print which geometric figure it corresponds to.
        if self.rand_n == 0:
            print('The generated image is a triangle')
        elif self.rand_n == 1:
            print('The generated image is a square')
        elif self.rand_n == 2:
            print('The generated image is a rectangle')
        else:
            print('The generated image is a circle')
        cv2.imshow(' ', self.shape) #Show the content of self.shape
        cv2.waitKey(0) #Indefinite delay
        cv2.destroyAllWindows() #Close all windows by pressing any key

    def whatShape(self): #create the method whatShape
        image = self.shape #Upload the image available in self.shape
        image_draw = image.copy() #Create a copy of the image
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Convert the image to grayscale
        ret, Ibw_shapes = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) #Binarize
        contours, hierarchy = cv2.findContours(Ibw_shapes, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #Find the contours
        for i in contours: #Walk through all generated contours
            curve = cv2.approxPolyDP(i, 3, True) #Approximate the contour to a polygon
            x, y, w, h = cv2.boundingRect(curve) #Save the characteristics of the polygon that was approached
            if len(curve) == 3: #If the polygon has 3 sides it is a triangle
                print('The entered figure is a triangle')
            if len(curve) == 4: #If the polygon has 4 sides it is a triangle or a square
                pp = w / h #Aspect ratio between width and height
                if pp == 1: #If pp is 1 the figure is a square
                    print('The entered figure is a square')
                else: ##If pp is not 1 the figure is a rectangle
                    print('The entered figure is a rectangle')
            if len(curve) > 10: #If the polygon has more than 10 sides it is considered a circle
                print('The entered figure is a circle')
            cv2.drawContours(image_draw, [curve], 0, (0, 0, 255), 2) #Draw the contour to the detected polygon
            cv2.imshow('image', image_draw) #Show the image with the outlines by pressing any letter
            cv2.waitKey(0) #Indefinite delay