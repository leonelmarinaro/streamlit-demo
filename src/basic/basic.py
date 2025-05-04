import streamlit as st

st.set_page_config(page_title="Page Title", layout="wide")

st.markdown(
    r"""
    <style>
    header {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def main() -> None:
    # --- Sidebar Menu ---
    st.sidebar.title("Menú")
    choice = st.sidebar.radio("Ir a:", ["Inicio", "Datos", "Ajustes"])

    if choice == "Inicio":
        st.title("Inicio")
        st.write("Bienvenido a la sección de inicio.")
    elif choice == "Datos":
        st.title("Datos")
        st.write("Aquí puedes visualizar tus datos.")
        # Ejemplo: st.dataframe(mi_dataframe)
    elif choice == "Ajustes":
        st.title("Ajustes")
        st.write("Configura tu aplicación aquí.")
        # Ejemplo: st.checkbox("Opción X")

    # --- Contenido común ---
    st.write("---")
    st.write("Puedes añadir más secciones o widgets según necesites.")


if __name__ == "__main__":
    main()
