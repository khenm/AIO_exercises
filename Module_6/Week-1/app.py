import streamlit as st
from PIL import Image
from model import predict

## Streamlit UI
st.title('Digit Recognition App')
st.markdown('### Using LeNet, trained on MNIST')

st.write('Upload an Image of a Digit')
uploaded_image = st.file_uploader("Upload Image File", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    st.success('Uploading successfully. Proceed to predict the Image')
    image = Image.open(uploaded_image)

    # Display the image
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Make prediction
    prediction, confidence = predict(image)
    st.write(f"**Predicted class:** {prediction}") 
    st.write(f"**Confidence:** {confidence:.2f}%")
else:
    st.warning('Please upload an image file.')