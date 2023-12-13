from rutermextract import TermExtractor
term_extractor = TermExtractor()
text = 'Вопрос с Айхала, хотелось бы знать по поводу инвентаря и формы для волейбола, нет мячей специализированных, нет не одного комплекта формы, а даже если есть то разносол!!!'
for term in term_extractor(text):
       print (term.normalized, term.count)