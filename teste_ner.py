from gliner2 import GLiNER2

model = GLiNER2.from_pretrained("fastino/gliner2-privacy-filter-PII-multi")

text = "Email john.smith@acme.com or call +1 415 555 0199."
labels = ["email", "phone_number", "person"]

result = model.extract_entities(
    text,
    labels,
    threshold=0.5,
    include_confidence=True,
    include_spans=True,
)

def formatar_result(result):
    for label, entities in result["entities"].items():
        for entity in entities:
            text = entity["text"]
            confidence = entity["confidence"]
            start = entity["start"]
            end = entity["end"]

            print(
                f"Text: {text}, "
                f"Label: {label}, "
                f"Confidence: {confidence:.2f}, "
                f"Start: {start}, "
                f"End: {end}"
            )


formatar_result(result)
