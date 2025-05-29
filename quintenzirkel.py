import streamlit as st

# --- 1. Daten für Tonarten (vereinfacht) ---
# Hier erweitern wir die Daten um Moll-Tonarten
key_data = {
    # Dur-Tonarten
    'C Dur': {
        'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'accidentals': 'Keine',
        'chords': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim']
    },
    'G Dur': {
        'notes': ['G', 'A', 'B', 'C', 'D', 'E', 'F♯'],
        'accidentals': 'F♯',
        'chords': ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F♯dim']
    },
    'F Dur': {
        'notes': ['F', 'G', 'A', 'B♭', 'C', 'D', 'E'],
        'accidentals': 'B♭',
        'chords': ['F', 'Gm', 'Am', 'B♭', 'C', 'Dm', 'Edim']
    },
    # ... weitere Dur-Tonarten hier einfügen ...

    # Moll-Tonarten (natürliches Moll)
    'Am Moll': { # parallele Moll-Tonart zu C Dur
        'notes': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'accidentals': 'Keine',
        'chords': ['Am', 'Bdim', 'C', 'Dm', 'Em', 'F', 'G']
    },
    'Em Moll': { # parallele Moll-Tonart zu G Dur
        'notes': ['E', 'F♯', 'G', 'A', 'B', 'C', 'D'],
        'accidentals': 'F♯',
        'chords': ['Em', 'F♯dim', 'G', 'Am', 'Bm', 'C', 'D']
    },
    'Dm Moll': { # parallele Moll-Tonart zu F Dur
        'notes': ['D', 'E', 'F', 'G', 'A', 'B♭', 'C'],
        'accidentals': 'B♭',
        'chords': ['Dm', 'Edim', 'F', 'Gm', 'Am', 'B♭', 'C']
    }
    # ... weitere Moll-Tonarten hier einfügen ...
}

# Funktion zur Ermittlung gängiger Progressionen (vereinfacht)
def get_progressions(key_name, chords):
    if not chords:
        return []

    # Einfache römische Ziffern für die Darstellung
    roman_numerals = {
        'Dur': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°'],
        'Moll': ['i', 'ii°', 'III', 'iv', 'v', 'VI', 'VII']
    }

    key_type = 'Dur' if 'Dur' in key_name else 'Moll'
    numerals = roman_numerals[key_type]

    # Hier können wir die Progressionen auf Basis der Akkorde generieren
    progression_list = []

    # Beispiel-Progressionen (an Tonart-Typ angepasst)
    if key_type == 'Dur':
        if len(chords) >= 5: # Sicherstellen, dass genügend Akkorde vorhanden sind
            progression_list.append(f"{numerals[0]} - {numerals[3]} - {numerals[4]} - {numerals[0]}: {chords[0]} - {chords[3]} - {chords[4]} - {chords[0]}")
            progression_list.append(f"{numerals[1]} - {numerals[4]} - {numerals[0]}: {chords[1]} - {chords[4]} - {chords[0]}")
            progression_list.append(f"{numerals[0]} - {numerals[5]} - {numerals[3]} - {numerals[4]}: {chords[0]} - {chords[5]} - {chords[3]} - {chords[4]}")
    else: # Moll-Tonart
        if len(chords) >= 5:
            progression_list.append(f"{numerals[0]} - {numerals[3]} - {numerals[4]} - {numerals[0]}: {chords[0]} - {chords[3]} - {chords[4]} - {chords[0]}")
            progression_list.append(f"{numerals[0]} - {numerals[5]} - {numerals[6]} - {numerals[0]}: {chords[0]} - {chords[5]} - {chords[6]} - {chords[0]}")
            # Hinweis: Für Moll wird oft der V-Akkord als Dur-Akkord verwendet (Dominante).
            # Das ist im aktuellen 'chords'-Array nicht abgebildet, müsste für eine fortgeschrittene App zusätzlich berechnet werden.
            # Beispiel: Für Am wäre V-Dur E statt Em.
            if key_name == 'Am Moll' and 'E' in key_data['C Dur']['chords']:
                 progression_list.append(f"{numerals[0]} - {numerals[3]} - V (dur) - {numerals[0]}: {chords[0]} - {chords[3]} - E - {chords[0]}")


    return progression_list

# --- 2. Streamlit App Layout ---
st.set_page_config(page_title="Interaktiver Quintenzirkel", layout="centered")

st.title("🎼 Interaktiver Quintenzirkel")
st.write("Wähle eine Dur- oder Moll-Tonart, um ihre Details anzuzeigen.")

# Dropdown für die Tonartauswahl
selected_key_name = st.selectbox(
    "Wähle eine Tonart:",
    options=list(key_data.keys()),
    index=0 # Standardmäßig die erste Tonart auswählen (C Dur)
)

# --- 3. Anzeige der Details basierend auf Auswahl ---
if selected_key_name:
    st.markdown("---") # Trennlinie
    st.header(f"Details für **{selected_key_name}**")

    current_data = key_data[selected_key_name]

    # Noten der Tonleiter
    st.subheader("🎵 Noten der Tonleiter:")
    st.info(f"**{', '.join(current_data['notes'])}**")
    st.markdown(f"**Vorzeichen:** {current_data['accidentals']}")

    # Diatonische Akkorde
    st.subheader("🎸 Diatonische Akkorde:")
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]

    for i, chord in enumerate(current_data['chords']):
        with cols[i % 3]:
            # Hier müsste man die römischen Ziffern je nach Dur/Moll zuordnen
            # Für die Einfachheit nur die Akkorde
            st.code(chord, language='text')

    # Gängige Progressionen
    st.subheader("🎶 Gängige Akkordprogressionen:")
    progressions = get_progressions(selected_key_name, current_data['chords'])
    if progressions:
        for prog in progressions:
            st.write(f"- {prog}")
    else:
        st.write("Keine gängigen Progressionen verfügbar.")

st.markdown("---")
st.caption("Hinweis: Dies ist ein vereinfachtes Beispiel. Die Daten für alle Tonarten und komplexere Musiktheorie müssten erweitert werden.")
