import streamlit as st

def show():
    """Display the Products page."""
    
    st.title("🛒 Our Products")
    
    st.markdown("""
    <div style="text-align: center; font-size: 1.3em; color: #1ABC9C; margin-bottom: 20px;">
        Explore our innovative AI-powered solutions designed for businesses.
    </div>
    """, unsafe_allow_html=True)

    # Example Products (Modify these later)
    products = [
        {
            "name": "AI Business Insights",
            "description": "Get real-time analytics and automated insights to make data-driven decisions.",
            "image": "https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/product1.jpg"
        },
        {
            "name": "Machine Learning API",
            "description": "Integrate AI into your workflows with our easy-to-use ML API solutions.",
            "image": "https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/product2.jpg"
        },
        {
            "name": "Geospatial Analytics",
            "description": "Advanced GIS-based analytics for business planning and environmental insights.",
            "image": "https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/product3.jpg"
        }
    ]

    # Display Products in a Grid Layout
    col1, col2, col3 = st.columns(3)

    for i, product in enumerate(products):
        with [col1, col2, col3][i]:
            st.image(product["image"], use_column_width=True)
            st.markdown(f"### {product['name']}")
            st.write(product["description"])
            st.markdown("---")
