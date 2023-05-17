import streamlit as st
import pandas as pd

# fungsi untuk menghitung pH meter ion hidrogen
def ph_meter_ion_hidrogen():
    st.subheader("pH Meter Ion Hidrogen")
    
    # input nilai pH
    ph = st.slider("Masukkan nilai pH", 0.0, 14.0, 7.0, 0.1)
    
    # menghitung konsentrasi ion hidrogen
    h = 10 ** (-ph)
    
    # menampilkan hasil konsentrasi ion hidrogen
    st.write(f"Konsentrasi ion Hidrogen (mol/L): {h:.2e}")
    
    # menampilkan jenis larutan
    if ph < 7:
        st.write("Jenis larutan: Asam")
    elif ph > 7:
        st.write("Jenis larutan: Basa")
    else:
        st.write("Jenis larutan: Netral")

# fungsi untuk menghitung pH meter ion hidrokarbon
def ph_meter_ion_hidrokarbon():
    st.subheader("pH Meter Ion Hidrokarbon")
    
    # input nilai pH
    ph = st.slider("Masukkan nilai pH", 0.0, 14.0, 7.0, 0.1)
    
    # menghitung konsentrasi ion hidrokarbon
    oh = 10 ** (-14 + ph)
    
    # menampilkan hasil konsentrasi ion hidrokarbon
    st.write(f"Konsentrasi ion Hidrokarbon (mol/L): {oh:.2e}")
    
    # menampilkan jenis larutan
    if ph < 7:
        st.write("Jenis larutan: Asam")
    elif ph > 7:
        st.write("Jenis larutan: Basa")
    else:
        st.write("Jenis larutan: Netral")

# fungsi untuk menghitung asam basa netral dalam mol/liter
def asam_basa_netral():
    st.subheader("Asam Basa Netral")
    
    # input nilai konsentrasi asam
    ca = st.slider("Masukkan konsentrasi asam (mol/L)", 0.0, 1.0, 0.1, 0.01)
    
    # input nilai konsentrasi basa
    cb = st.slider("Masukkan konsentrasi basa (mol/L)", 0.0, 1.0, 0.1, 0.01)
    
    # menghitung konsentrasi ion hidrogen
    h = 10 ** (-1 * (pd.np.log10(ca) - pd.np.log10(cb)))
    
    # menampilkan hasil konsentrasi ion hidrogen
    st.write(f"Konsentrasi ion Hidrogen (mol/L): {h:.2e}")
    
    # menampilkan jenis larutan
    if h < 10 ** -7:
        st.write("Jenis larutan: Basa")
    elif h > 10 ** -7:
        st.write("Jenis larutan: Asam")
    else:
        st.write("Jenis larutan: Netral")

# fungsi utama streamlit
def main():
    st.title("pH Meter dan Asam Basa Netral")
    
    option = st.selectbox("Pilih Mode", ("pH Meter Ion Hidrogen", "pH Meter Ion Hidrokarbon", "Asam Basa Netral"))
    
    if option == "pH Meter Ion Hidrogen":
        ph_meter_ion_hidrogen()
    elif option == "pH Meter Ion Hidrokarbon":
        ph_meter_ion_hidrokarbon()
    elif option == "Asam Basa Netral":
        asam_basa_netral()

if __name__ == "__main__":
    main()
