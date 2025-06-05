
import streamlit as st
import streamlit.components.v1 as components

# ----- Título -----
st.markdown("<h1 style='text-align: center; color: red;'>💖 Para Mi Mudosa 💖</h1>", unsafe_allow_html=True)

# ----- Corazón animado -----
heart_html = """
<div style="display: flex; justify-content: center; margin-top: 30px;">
  <div style="width: 100px; height: 90px; position: relative; animation: beat 1s infinite;">
    <div style="background-color: red; width: 100px; height: 100px; border-radius: 50% 50% 0 0; transform: rotate(-45deg); position: absolute; top: 0; left: 0;"></div>
    <div style="background-color: red; width: 100px; height: 100px; border-radius: 50% 50% 0 0; transform: rotate(45deg); position: absolute; top: 0; right: 0;"></div>
  </div>
</div>

<style>
@keyframes beat {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
}
</style>
"""
st.markdown(heart_html, unsafe_allow_html=True)

# ----- Carta de Amor -----
st.markdown("## 📜 Carta para Mi Cielo")

carta = """
Mi china hermosa,

Hoy cumplimos **dos años** de habernos elegido... y mientras más pasa el tiempo, más agradecido estoy con la vida por cruzarnos.

No hay día que no piense en lo mucho que significas para mí. **Tú eres mi alegría, mi refugio, mi lugar favorito.**  
Eres esa luz suave que me calma, ese abrazo que me arma cuando estoy roto.

Gracias por ser mi mudosa, por enseñarme que el amor se construye con paciencia, ternura y verdad.  
Gracias por las risas, los silencios, los mensajes inesperados, los "te amo" al oído y las miradas que me salvan.

**Yo, tu mudoso, te amo con todo mi ser.**  
Y si me preguntaran si volvería a vivir todo esto contigo, la respuesta siempre será:  
**Mil veces sí.**

Tú y yo, mi chica... hasta donde nos lleve el amor.  
Con el corazón abierto,  
**Tu mudoso**
"""
st.markdown(f"<div style='background-color: #fff0f5; padding: 20px; border-radius: 10px;'><p style='font-size:18px'>{carta}</p></div>", unsafe_allow_html=True)

# ----- Canción de Spotify -----
st.markdown("## 🎵 Nuestra canción")

spotify_url = "https://open.spotify.com/embed/track/6Jiom35dhAYX6ohfwJkQEr?utm_source=generator"
components.iframe(spotify_url, width=700, height=152)
