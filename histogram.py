from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_image_histogram(image_path):
    image = Image.open(image_path)
    image = np.array(image)
    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 8))

    for channel_id, channel in enumerate(["red", "green", "blue"]):
        channel_data = image[:, :, channel_id].ravel()
        sns.histplot(channel_data, color=channel, kde=True, stat="density", bins=256, line_kws={'linewidth': 1})
    plt.title('RGB Channel Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Density')
    plt.legend(labels=['Red Channel', 'Green Channel', 'Blue Channel'])
    plt.tight_layout()
    plt.show()


if __name__ ==  "__main__":
    # Change to the desired path.
    image_path = '/home/yalouini/Documents/cv_insights/random_colors.png'
    plot_image_histogram(image_path)