import random

import numpy as np
import torch
def evaluate_model(model, dataloader, criterion, device):
    model.eval()  # Set model to evaluation mode
    running_loss = 0.0
    correct = 0
    total = 0

    preds = []
    probs = []
    with torch.no_grad():  # Disable gradient calculation
        for data in dataloader:
            if len(data) == 3:
                inputs, labels, _ = data
            else:
                inputs, labels = data
            inputs, labels = inputs.to(device), labels.to(device)

            # Forward pass
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            # Track loss and accuracy
            running_loss += loss.item()
            prop_dist = torch.nn.Softmax(dim=-1)(outputs)
            prob, predicted = prop_dist.max(1)
            
            preds.extend(predicted.cpu().numpy())
            probs.extend(prob.cpu().numpy())
            correct += (predicted == labels).sum().item()
            total += labels.size(0)

    avg_loss = running_loss / len(dataloader)
    accuracy = correct / total

    print(f"Evaluation Loss: {avg_loss:.4f}, Evaluation Accuracy: {accuracy:.4f}")
    return avg_loss, accuracy, preds, probs
