import genanki

note_model_with_image = genanki.Model(
    11111111,
    "Basic Model with Image",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
        {"name": "Image"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Front}}<br>{{Image}}",  # Question format: Front text + image
            "afmt": '{{FrontSide}}<hr id="answer">{{Back}}',  # Answer format: Back text
        },
    ],
)

note_model_without_image = genanki.Model(
    22222222,
    "Basic Model without Image",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Front}}<br>{{Image}}",  # Question format: Front text + image
            "afmt": '{{FrontSide}}<hr id="answer">{{Back}}',  # Answer format: Back text
        },
    ],
)
