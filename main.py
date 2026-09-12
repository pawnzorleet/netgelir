import streamlit as st

st.header('Yıllık Brüt Gelirden Net Gelir Hesaplama')

brutgelir=st.number_input('Brüt gelir: ')


if brutgelir<190_000:
  gv=brutgelir*0.15
elif brutgelir>=190_000 and brutgelir<=400_000:
  gv=(400_000-190_000)*0.20+28_500
elif brutgelir>400_000 and brutgelir<=1_500_000:
  gv=(1_500_000-400_000)*0.27+70_500
elif brutgelir>1_500_000 and brutgelir<=5_300_000:
  gv=(5_300_000-1_500_000)*0.35+367_500
else:
  gv=brutgelir*0.40


netgelir=brutgelir-gv

st.write('Net gelir: ',netgelir)
