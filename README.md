# imageShape
Code to generate a geometric figure randomly.


The generateShape class receives two parameters: width and height. With this data a matrix of size width x height is created with 3 components at zero.

The generateShape method generates a random number between zero and 3 and draws a geometric figure on the black background. The 0 corresponds to a triangle, the 1 to a square rotated 45 °, the 2 to a rectangle and the 3 to a circle. All figures are centered on the image corresponding to the black background.

The showShape method displays the image available in self.shape for 5 seconds. After this time the window closes.

The getShape method displays the image available in self.shape and displays a string that says the name of the resulting shape.

The whatShape method detects the available contours in the image stored in self.shape and displays a string with the name of the resulting shape.
