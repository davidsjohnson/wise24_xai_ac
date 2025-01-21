import numpy as np

import matplotlib.pyplot as plt

CLASS_LABELS = ['Neutral', 'Happy', 'Sad', 'Surprise', 'Fear', 'Disgust', 'Anger', 'Contempt'] 

# Helper functions for plotting faces
def display_one_image(image, title, subplot=(1, 1, 1), xlabel=None, ylabel=None, border=False):
    """ Display an Image
    
    Helper function to display one image in a jupyter notebook
    
    Args:
        image (np.array): the image to display
        title (str): a title for the image
        subplot (tuple): a tuple indicating the matplotlib subplot parameters like (number rows, number cols, image number)
        xlabel (str): a label for the x axis
        ylabel (str): a label for the y axis
        border (bool): indicates if a border should be drawn around the image or not
    """
    plt.subplot(*subplot)
    # plt.axis('off')
    plt.imshow(image)
    plt.title(title, fontsize=16)
    plt.xticks([])
    plt.yticks([])
  
    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)
        
    if border:
        ax = plt.gca()
        ax.patch.set_edgecolor('red')
        ax.patch.set_linewidth(5) 
    
def display_nine_images(images, labels, preds, start, title_colors=None):
    '''Display 9 images with their labels and predictions
    Args:
        images (np.array): the images to display
        labels (np.array): the true labels for the images
        preds (np.array): the predicted labels for the images
        start (int): the index of the first image to display
        title_colors (list): a list of colors for the titles
    '''
    plt.figure(figsize=(13,13))
    for i in range(9):
        color = 'black' if title_colors is None else title_colors[i]
        idx = start+i
        pred = CLASS_LABELS[preds[idx]]
        true = CLASS_LABELS[labels[idx]]
        display_one_image(images[idx], f'Actual={true} \n Pred={pred} \n Index = {idx}', (3, 3, i+1))
    # plt.tight_layout()
    plt.subplots_adjust(wspace=0.1, hspace=0.4)
    plt.show()

def image_title(label, prediction):
  # Both prediction (probabilities) and label (one-hot) are arrays with one item per class.
    class_idx = np.argmax(label, axis=-1)
    prediction_idx = np.argmax(prediction, axis=-1)
    if class_idx == prediction_idx:
        return f'{CLASS_LABELS[prediction_idx]} [correct]', 'black'
    else:
        return f'{CLASS_LABELS[prediction_idx]} [incorrect, should be {CLASS_LABELS[class_idx]}]', 'red'

def get_titles(images, labels, model):
    predictions = model.predict(images)
    titles, colors = [], []
    for label, prediction in zip(labels, predictions):
        title, color = image_title(label, prediction)
        titles.append(title)
        colors.append(color)
    return titles, colors