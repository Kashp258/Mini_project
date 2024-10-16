import streamlit as st

def show_statistics_page():
    st.title("📊 Recycling Statistics")
    
    st.markdown("""
    ### The Importance of Recycling
    Recycling is a crucial aspect of waste management that helps reduce pollution and conserve natural resources. Here are some key statistics:
    
    - **Global Recycling Rate**: Only about **13%** of the world's plastic is recycled.
    - **Energy Savings**: Recycling aluminum saves **95%** of the energy required to produce new aluminum from raw materials.
    - **Reduction in Landfill Waste**: Recycling and composting prevented the release of approximately **186 million metric tons** of carbon dioxide equivalent into the air in 2018.
    
    ### Benefits of Recycling
    - **Conserves Natural Resources**: Reduces the need for new raw materials.
    - **Saves Energy**: Recycling generally uses less energy than producing new products.
    - **Reduces Pollution**: Decreases emissions from the manufacturing process.

    ### How You Can Help
    - **Reduce**: Minimize your waste by choosing products with less packaging.
    - **Reuse**: Find ways to reuse items before throwing them away.
    - **Recycle**: Follow local guidelines for recycling and make sure to recycle properly.
    """)
