import sys
from quadtree import Quadtree
from qtexception import QTException

"""
CSCI-603 Lab 8: ImageViewer

This program reads a compressed image file and visualises it. The compressed file is in the form 
of pre order traversal of a quad tree and after uncompressing it, it is converted into 2D array 
which is fit into an image which goes into canvas of a Tkinter

Tkinter displays the image that is displayed on the canvas

author: Kapil Sharma ks4643
"""

def main():
    """
        Main function for the image viewer application using a Quadtree.

        Usage:
            python image_viewer.py [-c] {filename}

        -c: Optional flag indicating compressed image format.
        filename: The name of the text file containing image data.

        :return: None
        """
    if len(sys.argv) < 2:
        print("Usage: python image_viewer.py [-c] {filename}")
        return None
    is_compressed = False
    if sys.argv[1] == "-c":
        is_compressed = True
        if sys.argv[2] is None or not sys.argv[2].endswith(".rit"):
            raise QTException("The file extension is incorrect or missing")
    elif sys.argv[1] is None or not sys.argv[1].endswith(".txt"):
        raise QTException("The file extension is incorrect or missing")

    try:
        q = Quadtree()
        q.read_files_from_file(sys.argv[-1], is_compressed)
        q.display_image_construction()
    except FileNotFoundError:
        print("File not found")
        return None
    except QTException as e:
        print(e)
        return None
    except ValueError:
        print("Pixels should be an integer value")


if __name__ == "__main__":
    main()



