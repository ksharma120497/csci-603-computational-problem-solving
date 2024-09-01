import math
from qtnode import QTNode
import tkinter
from qtexception import QTException

"""
This class holds all the information about the QuadTree 

It reads the uncompressed file and displays the image

It reads the compressed file and decompress it and display the image

There are functions to display the string representation of the 
pre order traversal of the image

author: Kapil Sharma ks4643
"""

class Quadtree:
    """
        Quadtree class for compressing and decompressing images using a quadtree data structure.
    """
    __slots__ = "uncompressed_array", "compressed_array", "uncompressed_2D_array", "compressed_2D_array", "filled_image", "root"

    def __init__(self):
        self.filled_image = None
        self.uncompressed_2D_array = None
        self.uncompressed_array = []
        self.compressed_array = []

    def read_files_from_file(self, file_name: str, is_compressed: bool) -> list:
        """
        This function reads file from the text file passed from the arguments
        :param is_compressed: to check if the file given is compressed or uncompressed
        :param file_name: name of the text file from where the file will be read
        :return: None
        """
        image_location = "compressed" if is_compressed else "uncompressed"
        open_file = open("../images/"+ image_location +"/"+ file_name)
        file_content = open_file.readlines()

        if is_compressed:
            first_value = int(file_content.pop(0))
            size = int(math.sqrt(first_value))
            if not math.sqrt(first_value).is_integer():
                raise QTException("The size is not a perfect square")

            for line in file_content:
                if -1 > int(line) or int(line) > 255:
                    raise QTException("The pixel values are outside the range of 0 and 255")
                self.compressed_array.append(int(line))


            # Build the quadtree from the compressed array
            node, index = self.build_quadtree(self.compressed_array)
            # Decompress the quadtree into a 2D array
            temp_2D_array = [[0] * size for _ in range(size)]
            self.decompress(node, temp_2D_array,size, 0, 0)
            self.uncompressed_2D_array = temp_2D_array

        else:
            for line in file_content:
                if -1 > int(line) or int(line) > 255:
                    raise QTException("The pixel values are outside the range of 0 and 255")
                self.uncompressed_array.append(int(line))
            self.uncompressed_2D_array_from_uncompressed()

    def uncompressed_2D_array_from_uncompressed(self):
        """
        Convert uncompressed array to a 2D array.
        :return: None
        """
        matrix_size = int(math.sqrt(len(self.uncompressed_array)))
        temp_array = [[0] * matrix_size for _ in range(matrix_size)]
        count= 0
        for i in range(matrix_size):
            for j in range(matrix_size):
                temp_array[i][j]=self.uncompressed_array[count]
                count+=1
        self.uncompressed_2D_array = temp_array

    def build_quadtree(self, preorder_list, index=0):
        """
        Build a quadtree from a preorder list.

        :param preorder_list: The preorder list representing the quadtree.
        :param index: The current index in the list.
        :return: Tuple containing the root of the quadtree and the next index in the list.
        """
        if index >= len(preorder_list):
            return None, index
        val = preorder_list[index]
        if val != -1:
            return QTNode(val), index + 1
        ul, index = self.build_quadtree(preorder_list, index + 1)
        ur, index = self.build_quadtree(preorder_list, index)
        ll, index = self.build_quadtree(preorder_list, index)
        lr, index = self.build_quadtree(preorder_list, index)
        return QTNode(val, ul, ur, ll, lr), index

    def decompress(self, node, c, size, x=0, y=0):
        """
        Decompress a quadtree into a 2D array.

        :param node: The root of the quadtree.
        :param c: The 2D array to fill with decompressed values.
        :param size: The size of the current sub-image.
        :param x: The starting x-coordinate.
        :param y: The starting y-coordinate.
        :return: None
        """

        if node.get_upper_left() is None and node.get_upper_right() is None and node.get_lower_left() is None and node.get_lower_right() is None:
            for i in range(x, x+size):
                for j in range(y, y+size):
                   c[i][j] = node.get_value()
            return

        self.decompress(node.get_upper_left(),c, size//2, x, y)
        self.decompress(node.get_upper_right(), c, size//2, x, y+(size//2))
        self.decompress(node.get_lower_left(),c,size//2, x+(size//2), y)
        self.decompress(node.get_lower_right(),c,size//2, x+size//2, y+size//2)

    def display_quadtree_traversal(self, root):
        """
        Display quadtree traversal starting from the root.

        :param root: The root of the quadtree.
        :return: None
        """
        if root is not None:
            print(root.get_value())
            self.display_quadtree_traversal(root.get_upper_left())
            self.display_quadtree_traversal(root.get_upper_right())
            self.display_quadtree_traversal(root.get_lower_left())
            self.display_quadtree_traversal(root.get_lower_right())


    def display_image_construction(self):
        """
        Display the constructed image using tkinter.

        :return: None
        """
        root = tkinter.Tk()
        root.title("Lab 8")
        rows, cols = len(self.uncompressed_2D_array), len(self.uncompressed_2D_array)
        image_array = self.uncompressed_2D_array
        photo_image = tkinter.PhotoImage(width=rows, height=cols)

        for i in range(rows):
            for j in range(cols):
                pixel_value = int(image_array[i][j])
                color = f"#{pixel_value:02x}{pixel_value:02x}{pixel_value:02x}"
                photo_image.put(color, (j, i))
                self.filled_image = photo_image

        canvas = tkinter.Canvas(root, width=rows, height=cols)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tkinter.NW, image=photo_image)
        root.mainloop()








