import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def main():
    # Input the start and end colors in hexadecimal format
    start_color = input("Input the start color (e.g., #FCCF31): ").strip() or "#FCCF31"
    end_color = input("Input the end color (e.g., #F55555): ").strip() or "#F55555"

    # Get the number of colors to generate
    try:
        n_colors = int(input("Number of colors to generate (e.g., 5): ").strip() or 5)
        if n_colors < 2:
            raise ValueError("Number of colors must be at least 2.")
    except ValueError as e:
        print(f"Invalid input for number of colors: {e}")
        return

    # Convert the hexadecimal colors to RGB format
    try:
        start_rgb = hex_to_rgb(start_color)
        end_rgb = hex_to_rgb(end_color)
    except ValueError as e:
        print(f"Invalid color format: {e}")
        return

    # Interpolate the colors
    colors = interpolate_colors(start_rgb, end_rgb, n_colors)
    print("Generated Colors:", colors)

    # Show the color gradient
    show_color_gradient(colors)

# Convert the hexadecimal color to RGB format
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6 or not all(c in "0123456789ABCDEFabcdef" for c in hex_color):
        raise ValueError(f"Invalid hex color: {hex_color}")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Convert RGB color back to hexadecimal
def rgb_to_hex(rgb_color):
    return '#{:02x}{:02x}{:02x}'.format(*rgb_color)

# Interpolate the colors between the start and end RGB values
def interpolate_colors(start_rgb, end_rgb, n_colors):
    return [
        rgb_to_hex(
            tuple(
                int(start_rgb[j] + (float(i) / (n_colors - 1)) * (end_rgb[j] - start_rgb[j]))
                for j in range(3)
            )
        )
        for i in range(n_colors)
    ]

# Display the color gradient
def show_color_gradient(colors):
    # Convert the hexadecimal colors to RGB values (range 0-1)
    rgb_colors = [mcolors.hex2color(c) for c in colors]
    gradient = [rgb_colors]  # Convert the color list into a 2D array

    # Display the color gradient
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.imshow(gradient, extent=[0, len(colors), 0, 1], aspect="auto")
    ax.set_xticks(range(len(colors)))
    ax.set_xticklabels(colors, rotation=45, fontsize=8)
    ax.set_yticks([])  # No y-axis ticks
    ax.set_title("Color Gradient")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
