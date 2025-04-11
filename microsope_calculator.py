# microscope_calculator.py

def calculate_real_size(microscope_size, magnification):
    return microscope_size / magnification

# Example usage
microscope_size = float(input("Enter microscope size (in µm): "))
magnification = float(input("Enter magnification: "))

real_size = calculate_real_size(microscope_size, magnification)
print(f"The real life size of the specimen is {real_size:.2f} µm")
