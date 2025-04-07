import streamlit as st
import datetime

# Set page config
st.set_page_config(
    page_title="Auto365 Mỹ Đình - Kiểm Tra Bảo Hành PPF",
    page_icon="🚗",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        border-radius: 0.5rem;
        padding: 0.75rem 1.5rem;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("Auto365 Mỹ Đình - Kiểm Tra Bảo Hành PPF")
st.markdown("### Hệ thống kiểm tra bảo hành dán phim PPF chính hãng")

# Search form
search_term = st.text_input("Nhập mã bảo hành PPF...", key="search")
search_button = st.button("Kiểm tra")

# Demo warranty data
DEMO_WARRANTY = {
    "DEMO123": {
        "customer_name": "Nguyễn Văn A",
        "vehicle_info": "Mercedes-Benz GLC 300 2023",
        "install_date": "2024-01-15",
        "warranty_end": "2029-01-15",
        "is_valid": True
    }
}

# Search handling
if search_button and search_term:
    warranty_info = DEMO_WARRANTY.get(search_term.upper())
    
    if warranty_info:
        st.success("✅ Còn bảo hành" if warranty_info["is_valid"] else "❌ Hết bảo hành")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Thông tin khách hàng")
            st.write(f"**Tên khách hàng:** {warranty_info['customer_name']}")
            st.write(f"**Thông tin xe:** {warranty_info['vehicle_info']}")
        
        with col2:
            st.markdown("#### Thông tin bảo hành")
            st.write(f"**Ngày dán:** {warranty_info['install_date']}")
            st.write(f"**Ngày hết hạn:** {warranty_info['warranty_end']}")
    else:
        st.error("❌ Không tìm thấy thông tin bảo hành")
        st.write("Vui lòng kiểm tra lại mã bảo hành hoặc liên hệ Auto365 Mỹ Đình")

# Pricing information
st.markdown("---")
st.markdown("## Bảng giá dán PPF ô tô (Cập nhật 2025)")

pricing_data = {
    "City PPF": [
        {"type": "Diamond 7.5 mil", "sedan": "22 triệu", "suv": "25 triệu", "warranty": "3 năm"},
        {"type": "Ruby 8.5 mil", "sedan": "27 triệu", "suv": "30 triệu", "warranty": "5 năm"}
    ],
    "TeckWrap": [
        {"type": "X75 7.5 mil", "sedan": "27 triệu", "suv": "29 triệu", "warranty": "4 năm"},
        {"type": "G75 7.5 mil", "sedan": "35 triệu", "suv": "40 triệu", "warranty": "6 năm"},
        {"type": "S75 7.5 mil", "sedan": "44 triệu", "suv": "48 triệu", "warranty": "7 năm"}
    ],
    "3M PPF": [
        {"type": "Series 100 Gloss", "sedan": "65 triệu", "suv": "69 triệu", "warranty": "7 năm"}
    ],
    "Premium Shield": [
        {"type": "PPF Premium Shield", "sedan": "40 triệu", "suv": "50 triệu", "warranty": "7 năm"}
    ]
}

for brand, products in pricing_data.items():
    st.markdown(f"### {brand}")
    for product in products:
        st.write(f"**{product['type']}**")
        st.write(f"- Sedan: {product['sedan']}")
        st.write(f"- SUV: {product['suv']}")
        st.write(f"- Bảo hành: {product['warranty']}")
    st.markdown("---")

# Contact information
st.markdown("## Thông tin liên hệ")
contact_col1, contact_col2 = st.columns(2)

with contact_col1:
    st.markdown("""
    - **Địa chỉ:** 116 Phố Trịnh Văn Bô, Xuân Phương, Nam Từ Liêm, Hà Nội
    - **Website:** [auto365mydinh.vn](https://auto365mydinh.vn/)
    - **Facebook:** [Auto365 Mỹ Đình](https://www.facebook.com/dangphuongauto365mydinh.vn/)
    """)

with contact_col2:
    st.markdown("""
    - **Hotline đặt hàng:** [0362467666](tel:0362467666) (Mr Huy)
    - **Hotline bảo hành/Tư vấn:** [036 2387666](tel:0362387666)
    - **Hotline khác:** [0822863366](tel:0822863366)
    """)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
    © 2025 Auto365 Mỹ Đình. All rights reserved.
    </div>
""", unsafe_allow_html=True)
