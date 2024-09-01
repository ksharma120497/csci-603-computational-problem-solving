"""
CSCI-603 Lab 2: Ciphers

A program that encodes/decodes a message by applying a set of transformation operations.
The transformation operations are:
    shift - Sa[,n] changes letter at index a by moving it n letters fwd in the alphabet. A negative
        value for n shifts the letter backward in the alphabet.
    rotate - R[n] rotates the string n positions to the right. A negative value for n rotates the string
        to the left.
    duplicate - Da[,n] follows character at index a with n copies of itself.
    trade - Ta,b swap the places of the a-th and b-th characters.
    affine - Aa,b applies the affine cipher algorithm y = (ax + b) mod 26 using a and b as keys.

All indices numbers (the subscript parameters) are 0-based.

author: Kapil Sharma ks4643
"""


def main() -> None:
    """
    The main loop responsible for getting the input details from the user
    and printing in the standard output the results
    of encrypting or decrypting the message applying the transformations
    :return: None
    """
    print("Welcome to Ciphers!")
    print(
        "What do you want to do: (E)ncrypt, (D)ecrypt or (Q)uit? Enter the message: Enter the encrypting transformation operations: Generating output ...")
    prompt = input()
    if prompt == "Q":
        return None
    elif prompt == "E":
        message_string = input()
        transformation = input()
        if 'S' in transformation:
            shift_operation_on_message("E", message_string, transformation)


'''
This is shift operation
@params operatio n : 
@params message_string : message that needs to be transformed (encrypted/decrypted)

'''


def shift_operation_on_message(operation, message_string, transformation):
    transformation_split = transformation.split(',')
    letter_to_be_transformed = transformation_split[0]

if __name__ == '__main__':
    main()
