from src.utils import (
    load_model,
    load_scaler,
    load_encoders,
    load_target_encoder,
)

from src.preprocessing import preprocess_input

# ==========================================
# Load Trained Objects
# ==========================================

model = load_model()
scaler = load_scaler()
encoders = load_encoders()
target_encoder = load_target_encoder()


# ==========================================
# Prediction Function
# ==========================================

def predict_customer(customer_data):

    # Preprocess input
    processed_data = preprocess_input(
        customer_data,
        encoders,
        scaler
    )

    # Prediction
    prediction = model.predict(processed_data)[0]

    # Prediction probabilities
    probabilities = model.predict_proba(processed_data)[0]

    # Decode prediction
    prediction_label = target_encoder.inverse_transform([prediction])[0]

    # Confidence (highest probability)
    confidence = probabilities.max()

    # Get probability of each class
    class_labels = target_encoder.inverse_transform(model.classes_)

    probability_dict = {
        class_labels[i]: float(probabilities[i])
        for i in range(len(class_labels))
    }

    return prediction_label, confidence, probability_dict