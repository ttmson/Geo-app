import streamlit as st
import numpy as np
from PIL import Image
from detect import detect_shapes
from logic import infer_relationships

# Cài đặt cấu hình giao diện
st.set_page_config(
    page_title="📐 Geometry AI – Nhận diện Hình học",
    layout="centered",
)

# Tiêu đề ứng dụng
st.title("📐 Geometry AI")
st.markdown("Ứng dụng nhận diện **đối tượng và quan hệ hình học** từ ảnh, hỗ trợ giáo viên và học sinh.")

# Tải ảnh
uploaded_file = st.file_uploader("🖼️ Tải ảnh bài toán hình học", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)
    st.image(image, caption="📎 Ảnh gốc", use_column_width=True)

    # Nhận diện hình học
    with st.spinner("🤖 Đang phân tích hình ảnh..."):
        annotated_image, shapes = detect_shapes(img_array)
        relationships = infer_relationships(shapes)

    # Hiển thị kết quả
    st.image(annotated_image, caption="✅ Kết quả nhận diện", use_column_width=True)

    st.subheader("📌 Đối tượng hình học được phát hiện:")
    if shapes:
        for s in shapes:
            st.markdown(f"- **{s['label']}** tại tọa độ `{s['bbox']}`")
    else:
        st.write("Không phát hiện được hình học nào.")

    st.subheader("📐 Các quan hệ hình học suy luận:")
    if relationships:
        for a, b, rel in relationships:
            st.markdown(f"- **{a['label']}** ↔ **{b['label']}** → *{rel}*")
    else:
        st.info("Hệ thống không phát hiện quan hệ hình học rõ ràng.")

# Footer
st.markdown("---")
st.caption("🎓 Phát triển bởi Geometry AI – Dành cho giáo dục và học tập hình học phẳng.")
