
# QUAN LY DIEM SINH VIEN - STREAMLIT

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Quan ly diem sinh vien",
    page_icon="📚",
    layout="wide"
)

# 1. Tao du lieu
data = {
    "Ho_ten": [
        "Nguyen Van An", "Tran Thi Binh",
        "Le Minh Chau", "Pham Hoang Dung",
        "Vo Thi Ha", "Dang Minh Khang",
        "Bui Ngoc Lan", "Hoang Gia Minh",
        "Do Thu Trang", "Nguyen Quoc Viet"
    ],
    "Chuyen_can": [9, 8, 10, 7, 9, 8, 10, 6, 9, 8],
    "Giua_ky":    [8, 7, 9, 6, 8, 7, 9, 5, 8, 7],
    "Cuoi_ky":    [8, 8, 9, 7, 9, 8, 10, 6, 8, 9]
}

df = pd.DataFrame(data)

# 2. Tinh diem tong ket
df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
).round(2)

# 3. Xep loai
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 4. Tieu de
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 5. Bang diem
st.subheader("Bang diem sinh vien")

bang_diem = df.rename(columns={
    "Ho_ten": "Ho ten",
    "Chuyen_can": "Chuyen can",
    "Giua_ky": "Giua ky",
    "Cuoi_ky": "Cuoi ky",
    "Tong_ket": "Tong ket",
    "Xep_loai": "Xep loai"
})

st.dataframe(bang_diem, use_container_width=True)

# 6. Thong ke
st.subheader("Thong ke ket qua")

sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
diem_tb = df["Tong_ket"].mean()
so_sv_dat = int((df["Tong_ket"] >= 5).sum())

c1, c2, c3, c4 = st.columns(4)

c1.metric("Diem trung binh", f"{diem_tb:.2f}")
c2.metric("Diem cao nhat", f"{sv_max['Tong_ket']:.2f}")
c3.metric("Diem thap nhat", f"{sv_min['Tong_ket']:.2f}")
c4.metric("So sinh vien dat", f"{so_sv_dat}/10")

st.write(
    "Sinh vien cao nhat:",
    sv_max["Ho_ten"], "-", sv_max["Tong_ket"]
)
st.write(
    "Sinh vien thap nhat:",
    sv_min["Ho_ten"], "-", sv_min["Tong_ket"]
)

# 7. Chon sinh vien
st.subheader("Tra cuu diem sinh vien")

ten_sv = st.selectbox("Chon sinh vien", df["Ho_ten"])
sv = df[df["Ho_ten"] == ten_sv].iloc[0]

st.write("Ho va ten:", sv["Ho_ten"])
st.write("Diem chuyen can:", sv["Chuyen_can"])
st.write("Diem giua ky:", sv["Giua_ky"])
st.write("Diem cuoi ky:", sv["Cuoi_ky"])
st.write("Diem tong ket:", sv["Tong_ket"])
st.write("Xep loai:", sv["Xep_loai"])

# 8. Bieu do
st.subheader("Bieu do diem tong ket")

fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("DIEM TONG KET CUA 10 SINH VIEN")
ax.set_xlabel("Ho ten sinh vien")
ax.set_ylabel("Diem tong ket")
ax.set_ylim(0, 10)
plt.xticks(rotation=45, ha="right")
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

# 9. Thong tin nguoi tao
st.divider()
st.caption("Ho ten: [PHẠM THỊ MAI LINH] | MSSV: [038308000154]")
