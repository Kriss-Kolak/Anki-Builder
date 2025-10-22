import genanki

# Define deck
deck = genanki.Deck(
    2054000110,
    "Les loisirs – Hobby et temps libre (A1–A2)"
)

# Model for the cards
model = genanki.Model(
    1607392319,
    "Simple Model PL->FR",
    fields=[{"name":"Front"},{"name":"Back"},{"name":"Example"}],
    templates=[{
        "name":"PL->FR",
        "qfmt":"<b>{{Front}}</b>",                 # PL na przodzie
        "afmt":"{{FrontSide}}<hr id='answer'>{{Back}}<br><i>{{Example}}</i>"  # FR + przykład
    }],
)

# Vocabulary list with examples
vocab = [
    ("cuisiner", "gotować", "J’aime cuisiner le soir."),
    ("lire", "czytać", "Elle aime lire des livres."),
    ("écouter de la musique", "słuchać muzyki", "Il adore écouter de la musique."),
    ("regarder des séries / des films", "oglądać seriale / filmy", "On aime regarder des séries le week-end."),
    ("faire du sport", "uprawiać sport", "Je fais du sport trois fois par semaine."),
    ("aller à la salle de sport", "chodzić na siłownię", "Je vais à la salle de sport après le travail."),
    ("jouer à des jeux vidéo", "grać w gry wideo", "Nous jouons à des jeux vidéo ensemble."),
    ("sortir avec des amis", "wychodzić ze znajomymi", "Elle aime sortir avec des amis le samedi."),
    ("voyager", "podróżować", "J’adore voyager en Europe."),
    ("apprendre les langues", "uczyć się języków", "Il aime apprendre les langues étrangères."),
    ("faire la cuisine", "gotować (ogólnie)", "Ma mère fait la cuisine tous les jours."),
    ("faire du vélo", "jeździć na rowerze", "Je fais du vélo le dimanche."),
    ("faire une promenade", "iść na spacer", "On fait une promenade dans le parc."),
    ("regarder YouTube", "oglądać YouTube", "J’aime regarder YouTube le soir."),
    ("écouter des podcasts", "słuchać podcastów", "J’écoute des podcasts pendant que je cuisine."),
    ("jouer d’un instrument", "grać na instrumencie", "Elle joue du piano depuis cinq ans."),
    ("faire du shopping", "robić zakupy", "On fait du shopping en centre-ville."),
    ("dessiner / peindre", "rysować / malować", "J’aime dessiner quand il pleut."),
    ("faire du jardinage", "uprawiać ogród", "Mes parents aiment faire du jardinage le week-end."),
    ("regarder un match", "oglądać mecz", "Il aime regarder un match de foot le dimanche soir."),
]

# Add notes to deck
for fr, pl, ex in vocab:
    note = genanki.Note(
        model=model,
        fields=[pl, fr, ex]
    )
    deck.add_note(note)

# Create package
package = genanki.Package(deck)
output_path = "build_decks/les_loisirs_hobby_temps_libre.apkg"
package.write_to_file(output_path)

output_path
